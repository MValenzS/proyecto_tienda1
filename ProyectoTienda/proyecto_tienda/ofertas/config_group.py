from django.contrib.auth.models import User, Group, Permission

def crear_usuario():
    admin_usuario = User.objects.create_user(username='admin12', password='admin123')
    admin_group = Group.objects.create_user(name='Administradores')
    
    admin_usuario.groups.add(admin_group)
    admin_usuario.save()
    
    visitante_usuario=User.objects.create_user(username='visitante', password='visitante123')
    visitante_usuario.groups.add(admin_group)
    visitante_usuario.save()
    
    visitante_group=Group.objects.create_user(name='Visitantes')
    visitante_group.groups.add(admin_group)
    visitante_group.save()
   