from django.urls import path, include
from .views import UsersList, UserDetailView

app_name = 'mainapp'

urlpatterns = [
    path('', UsersList.as_view(), name='main'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
]