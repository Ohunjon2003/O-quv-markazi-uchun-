from django.dispatch import Signal,receiver
from django.db.models.signals import post_save,post_delete
from django.contrib.auth.models import User

from .models import Profil


@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    user = instance
    if created:
        Profil.objects.create(
            user=user
        )





@receiver(post_save,sender=Profil)
def user_edit(sender,instance,created,**kwargs):
    user = instance.user

    if instance.name and len(instance.name.split(" ")) == 2:
        user.first_name,user.last_name = instance.name.split(" ")
    if instance.email:
        user.email = instance.email
        user.save()



@receiver(post_delete,sender=Profil)
def delete_user(sender,instance,**kwargs):
    profile = instance
    user = instance.user
    user.delete()

#
# Signal.connect(post_save,create_profile,sender=User)
# Signal.connect(post_delete,delete_user,sender=Profil)