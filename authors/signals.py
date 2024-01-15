#  são uma forma de enviar sinais ou notificações
# quando ocorre uma determinada ação no banco de dados ou em algum modelo específico


from authors.models import User, Profile
from django.db.models.signals import post_save  # post_save é dps que salvar e pre_save é antes de salvar
from django.dispatch import receiver  # é basicamente conectar seu model em um sinal qualquer


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        profile = Profile.objects.create(authors=instance)
        profile.save()
