#  são uma forma de enviar sinais ou notificações
# quando ocorre uma determinada ação no banco de dados ou em algum modelo específico


from receitas.models import receita
from django.db.models.signals import pre_save, pre_delete  # post_save é dps que salvar e pre_save é antes de salvar
from django.dispatch import receiver  # é basicamente conectar seu model em um sinal qualquer
import os


# esse signal faz com que quando eu apago uma receita a imagem apaga junto na fica no servidor.
def delete_cover(instance):
    try:
        os.remove(instance.cover.path)
    except (ValueError, FileNotFoundError):
        ...


@receiver(pre_delete, sender=receita)
def receita_cover_delete(sender, instance, *args, **kwargs):
    old_instance = receita.objects.filter(pk=instance.pk).first()

    if old_instance:
        delete_cover(old_instance)


@receiver(pre_save, sender=receita)
def receita_cover_edit(sender, instance, *args, **kwargs):
    old_instance = receita.objects.filter(pk=instance.pk).first()

    if not old_instance:
        return

    is_new_cover = old_instance != instance.cover

    if is_new_cover:
        delete_cover(old_instance)
