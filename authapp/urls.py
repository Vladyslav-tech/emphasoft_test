from django.urls import path
from .views import register, edit, logout, login

app_name = 'authapp'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('edit/', edit, name='edit'),
]