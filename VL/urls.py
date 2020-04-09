from django.urls import path
from VL import views

app_name = 'VL'
urlpatterns = [
    path('', views.get_photo, name='photo_upload'),  # VL 앱에서 뒤에 아무 주소 입력이 없을 때 views 의 get_photo 함수 호출(이름을 photo_upload로 지정).
    path('<int:photo_id>/true_country', views.get_true_country, name='get_true_country'),  # VL/photo_id/get_true_country 로 요청이 오면 views get_true_country(이름을 get_true_country로 지정)
]
