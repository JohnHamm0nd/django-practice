from django.db import models
from imagekit.models import ProcessedImageField
# Create your models here.

class VisualLocalization(models.Model):
    photo = ProcessedImageField(format='JPEG',                           
                                options={'quality':90},
                                )  # 이미지를 손실압축하여 이미지 크기를 줄임
    pred_country = models.CharField(max_length=20, blank=True)
    true_country_choice = [('0', '호주'), ('1', '프랑스'), ('2', '이탈리아'), ('3', '한국'), ('4', '미국')]
    true_country = models.CharField(max_length=20, choices=true_country_choice, blank=True)
    correct = models.NullBooleanField(blank=True) 
'''
null, blank
null은 데이터베이스와 관련되어 있고 blank는 유효성과 관련이 있다고 한다.
null은 데이터베이스 컬럼이 null 값을 가질수 있는지 없는지, blank는 입력된 폼이 비어있는지 아닌지를 검사하는데 사용된다.
blank가 False값을 가지면 폼이 채워지지 않았을 때 fomr.is_valid()를 통과하지 못하기 때문에 True값을 주었다.
form 에서 이미지를 업로드 할떄에는 필드를 photo만 주었고, 정답 값을 입력 받을 때에는 true_country만 주었기 때문에 True값을 주지 않아도 작동하게 되었다.
'''
