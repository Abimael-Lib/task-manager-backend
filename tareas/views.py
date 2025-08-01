from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Tarea
from .serializers import TareaSerializer


def index(request):
    return render(request, 'index.html')



class TareaViewSet(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user).order_by('-fecha_creacion')

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def prueba_auth(request):
    return Response({"mensaje": "Autenticación OK"})
    
