from django.urls import path
from .views import SignUp
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    path('signup', SignUp.as_view(), name='signup'),
    path('signin/', auth_views.LoginView.as_view(template_name="accounts/signin.html"), name='signin'),
    path('signout/', auth_views.LogoutView.as_view(), name="signout"),
    ]

