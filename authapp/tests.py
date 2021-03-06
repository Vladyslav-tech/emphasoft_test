from django.test import TestCase
from django.test.client import Client
from authapp.models import CustomerUser


class TestUserManagement(TestCase):
   def setUp(self):
       self.client = Client()
       self.user = CustomerUser.objects.create_user('tarantino', \
                       'tarantino@test.local', 'tarantino_test')

   def test_user_login(self):
       # главная неавторизованного юзера
       response = self.client.get('/')
       self.assertEqual(response.status_code, 200)
       self.assertTrue(response.context['user'].is_anonymous)
       self.assertNotContains(response, 'Пользователь', status_code=200)

       self.client.login(username='tarantino', password='tarantino_test')

       # логинимся
       response = self.client.get('/auth/login/')
       self.assertFalse(response.context['user'].is_anonymous)
       self.assertEqual(response.context['user'], self.user)

       # главная после логина
       response = self.client.get('/')
       self.assertContains(response, 'Пользователь', status_code=200)
       self.assertEqual(response.context['user'], self.user)
       self.assertIn('Пользователь', response.content.decode())


   def test_user_logout(self):
       # данные пользователя
       self.client.login(username='tarantino', password='tarantino_test')

       # логинимся
       response = self.client.get('/auth/login/')
       self.assertEqual(response.status_code, 200)
       self.assertFalse(response.context['user'].is_anonymous)

       # выходим из системы
       response = self.client.get('/auth/logout/')
       self.assertEqual(response.status_code, 302)

       # главная после выхода
       response = self.client.get('/')
       self.assertEqual(response.status_code, 200)
       self.assertTrue(response.context['user'].is_anonymous)

   def test_user_register(self):
       # логин без данных пользователя
       response = self.client.get('/auth/register/')
       self.assertEqual(response.status_code, 200)
       self.assertEqual(response.context['title'], 'Регистрация')
       self.assertTrue(response.context['user'].is_anonymous)

       new_user_data = {
           'username': 'samuel',
           'first_name': 'Сэмюэл',
           'last_name': 'Джексон',
           'password1': 'samuelpass',
           'password2': 'samuelpass',
           'email': 'sumuel@geekshop.local',
            }

       response = self.client.post('/auth/register/', data=new_user_data)
       self.assertEqual(response.status_code, 302)

       # данные нового пользователя
       self.client.login(username=new_user_data['username'], \
                         password=new_user_data['password1'])

       # логинимся
       response = self.client.get('/auth/login/')
       self.assertEqual(response.status_code, 200)
       self.assertFalse(response.context['user'].is_anonymous)

       # проверяем главную страницу
       response = self.client.get('/')
       self.assertContains(response, text=new_user_data['first_name'], \
                           status_code=200)
