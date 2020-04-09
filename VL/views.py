from django.shortcuts import render
from .models import VisualLocalization
from .forms import PhotoForm, TrueCountryForm
from django.shortcuts import redirect  # 특정 url로 이동 하고자 할 때 사용 - 임시로 사진이 업로드 되었을 때 board로 가게 하기
from django.db import transaction  # transaction.atomic() - 데이터베이스 트랜젝션 원자성을 위해 사용.


# VL
import efficientnet.keras
from keras import layers
from keras.models import load_model
from keras.preprocessing import image
from keras.backend import set_session
import time
import numpy as np
from keras import optimizers
import tensorflow as tf


'''
세션을 만들고 빈 그래프를 먼저 만들어 주지 않으면 오류가 난다.
As far as I understand, the problem is that tensorflow graphs and sessions are not thread safe.
So by default a new session (which does not contain any previously loaded weights, models a.s.o.) is created for each thread, i.e. for each request.
By saving the global session that contains all your models and setting it to be used by keras in each thread the problem is solved.
출처: https://github.com/tensorflow/tensorflow/issues/28287
'''

sess = tf.Session()
graph = tf.get_default_graph()
set_session(sess)
model = load_model('VL/Jetson_nano_gpu_efficientnetB0_5_classes_3.h5')  # 모델 로드
model.compile(loss='categorical_crossentropy', optimizer=optimizers.RMSprop(lr=2e-5), metrics=['acc'])  # 5개의 나라이기 때문에 모델을 학습 시킬 때 카테고리 분류 모델을 만들었다.
country = {0:'호주', 1:'프랑스', 2:'이탈리아', 3:'한국', 4:'미국'}  # 분류 값.

# Create your views here.
# 함수형 뷰 사용.
def prediction(photo_path):
    img = image.load_img((photo_path), target_size = (224, 224))  # 이미지를 모델 입력 크기에 맞게 리사이즈, EfficientNetB0 모델을 학습된 가중치를 제외하고 그대로 사용하기 때문에 EfficientNetB0모델의 입력 사이즈와 같아야 한다.
    img = image.img_to_array(img)  # 이미지를 배열로 변환
    img = np.array(img).astype('float32')/255  # 0~1의 값으로 리스케일
    img = np.expand_dims(img, axis = 0)  # 차원 추가
    global sess
    global graph
    with graph.as_default():
        set_session(sess)
        return model.predict_classes(img, verbose=1)[0]


# 사진을 업로드 받고, 사진과 분류 값을 저장한 후 사진과 분류 값을 리턴
def get_photo(request):
    # POST로 폼데이터를 입력받을 때
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)  # 사진, 파일 등을 가져올 때는 request.FILES가 필요하다! 
        # 유효성 검사
        if form.is_valid():
            # 유효성 검사 성공
            with transaction.atomic():  # 데이터베이스 트랜젝션 원자성을 보장하기 위한 사용 - with 블록 안에 있는 코드들이 하나의 트랜젝션으로 원자성이 보장된다. 
                obj = form.save(commit=False)  # commit=False
                obj.pred_country = prediction(obj.photo)  # 이미지 분류, 예측값 저장.
                obj.save()  # save
                #print(form.instance.id)  # form을 저장해야 생성된다(당연히 데이터를 저장하기도 전에 id값이 생길리 없다), 추가로 dafault id값을 써야한다. 모델에 id 를 명시(수동생성)하면 안된다. primary key를 직접 생성하면 안되는것 같다
                true_country_form = TrueCountryForm()
                return render(request, 'VL/prediction.html', {'photo_id': obj.id, 'photo': obj.photo, 'pred_country': country[obj.pred_country], 'true_country_form': true_country_form})
                
    # Get으로 받을 경우, 빈 Form을 템플릿에 출력한다
    else:
        form = PhotoForm()  # 빈 Form 생성
    return render(request, 'VL/photo_upload.html', {'form': form})


# 사진과 분류 값을 보여준 페이지에서 정답을 입력받아 정답과 분류 값을 비교한 후 분류가 맞았는지 틀렸는지 여부를 함께 저장하고, 사진 업로드 페이지로 리턴
# 모델에서 오브젝트를 가져와 값을 넣은 저장하는데, view에서 하는게 좋은가? 모델에서 하는게 좋은가?
def get_true_country(request, photo_id):
    photo = VisualLocalization.objects.get(id=photo_id)
    if request.method == 'POST':
        form = TrueCountryForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                photo.true_country = form.cleaned_data['true_country']
                #print(form.cleaned_data['true_country'])
                #print(photo.pred_country)
                if photo.pred_country == photo.true_country:
                    photo.correct=True
                else:
                    photo.correct=False
                photo.save()  # 업데이트가 필요?
                return redirect('VL:photo_upload')
