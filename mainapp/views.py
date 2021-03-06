from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from authapp.models import CustomerUser


class UsersList(ListView):
    model = CustomerUser
    template_name = 'mainapp/main.html'

class UserDetailView(DetailView):
    model = CustomerUser
    template_name = 'mainapp/user_detail.html'
