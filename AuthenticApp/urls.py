from django.urls import path
from . import views

app_name = 'AuthenticApp'

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('user_login',views.user_login,name='user_login'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('special',views.special,name='special'),

]