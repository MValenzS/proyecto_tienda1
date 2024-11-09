from typing import Any
from django.contrib.auth.models import User, Group, Permission
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Crea usuario de prueba para la app. y asigna permisos'
    
    def asignar_permisos_grupo(self, grupo_nombre, permisos):
        grupo, creado = Group.objects.get_or_create(name=grupo_nombre)
        
        for permiso in permisos:
            grupo.permissions.add.objects.get(codename=permiso)
            
    # def handle(self):
         