from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Tarea
from rest_framework_simplejwt.tokens import RefreshToken

class TareaTests(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(username='usuario1', password='password123')
        refresh = RefreshToken.for_user(self.usuario)
        self.token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_crear_tarea(self):
        data = {'titulo': 'Tarea de prueba'}
        response = self.client.post('/api/tareas/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tarea.objects.count(), 1)

    def test_listar_tareas(self):
        Tarea.objects.create(usuario=self.usuario, titulo='Tarea 1')
        response = self.client.get('/api/tareas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_actualizar_tarea(self):
        tarea = Tarea.objects.create(usuario=self.usuario, titulo='Tarea vieja')
        data = {'titulo': 'Tarea actualizada'}
        url = f'/api/tareas/{tarea.id}/'
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['titulo'], 'Tarea actualizada')

    def test_borrar_tarea(self):
        tarea = Tarea.objects.create(usuario=self.usuario, titulo='Tarea a eliminar')
        url = f'/api/tareas/{tarea.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tarea.objects.count(), 0)















