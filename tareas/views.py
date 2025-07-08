from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Tarea
from .serializer import TareaSerializer


class TareaViewSet(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user).order_by('-fecha_creacion')

    def perform_create(self, serializer):
        serializer.save(usuario.self.request.user)

