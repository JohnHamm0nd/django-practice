"""django_practice_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static  # media url 추가를 위해 static함수 임포트
from django.conf import settings  # media url 추가를 위해 settings함수 임포트

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),  # home app urls
    path('board/', include('board.urls', namespace='board')),  # board app urls
    path('VL/', include('VL.urls', namespace='VL')),  # VL app urls
    path('accounts/', include('accounts.urls', namespace='accounts')),  # accounts app urls
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # media url, root 추가
