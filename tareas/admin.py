from django.contrib import admin
from .models import Tarea

# Register your models here.
@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'usuario', 'completada', 'creado')
    list_filter = ('completada', 'creado')
    search_fields = ('titulo', 'descripcion')
    ordering = ('creado',)



# Titulo y cabecera
from django.contrib import admin

admin.site.site_header = "Task Manager Admin"
admin.site.site_title = "Panel de Administración"
admin.site.index_title = "Bienvenido al Administrador de Tareas"



