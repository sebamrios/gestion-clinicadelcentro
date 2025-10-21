from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Usuario


@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    print("Signals de usuarios cargados!") 

    if created:
        print(f"Creando perfil para {instance.username}")
        Usuario.objects.create(usuario=instance,nombre='',apellido='',)
        print(f"Perfil Usuario creado para {instance.username}")

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.usuario.save()

