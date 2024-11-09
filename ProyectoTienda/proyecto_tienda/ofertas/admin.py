from django.contrib import admin
from django.forms import ModelForm
from django.http import HttpRequest
from .models import Oferta
from django.contrib.auth.models import Group, Permission

# Register your models here.
@admin.register(Oferta)

class OfertaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'porcentaje_descuento', 'fecha_inicio', 'fecha_fin')
    search_fields = ('producto__nombre', )
    
    #creamos permisos para distintos usuarios 
    #grupo administrador
    def save_model(self, request, obj, form, change):
        #creamos el grupo
        group_admin = Group.objects.get(name='Administradores')
        #creamos los permisos
        permisos= Permission.objects.filter(codename__in={'crear_ofertas','editar_ofertas', 'eliminar_ofertas'})
        group_admin.permissions.add(*permisos)
        
       # return super().save_model(request, obj, form, change)