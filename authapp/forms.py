from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm
from .models import CustomerUser


class CustomerUserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomerUser
        fields = ('username', 'gender', 'first_name', 'last_name', 'patronymic', 'email')
        labels = {
            'username': 'Никнейм',
            'first_name': 'Имя',
            'last_name': 'Фамилия'
        }

    def __init__(self, *args, **kwargs):
        super(CustomerUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class CustomerUserEditForm(UserChangeForm):
    class Meta:
        model = CustomerUser
        fields = ('username', 'first_name', 'last_name', 'patronymic', 'gender', 'email', 'about', 'avatar')
        labels = {
            'username': 'Никнейм',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }

    def __init__(self, *args, **kwargs):
        super(CustomerUserEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class CustomerUserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomerUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(CustomerUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''