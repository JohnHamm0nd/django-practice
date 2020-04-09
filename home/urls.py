from django.urls import path
from home import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='home'), # HOME 앱에서 뒤에 아무 주소 입력이 없을 때 views에 index 호출, 메인 프로젝트에서 주소 뒤에 아무 입력이 없을 시에 home앱의 url로 연결해 놓았음.
]
