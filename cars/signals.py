from django.db.models.signals import (
    pre_save, pre_delete, post_save, post_delete)
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory


def car_inventory_update():
    # cria uma query que retorna a quantidade de itens na tabela
    cars_count = Car.objects.all().count()
    # cria uma query que retorna a somatória do campo value
    cars_value = Car.objects.aggregate(
        total_value=Sum('value')
    ).get('total_value', 0)

    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    ...


@receiver(pre_delete, sender=Car)
def car_pre_delete(sender, instance, **kwargs):
    ...


# Se quisermos distinguir se o evento é de criação ou atualização
# nós podemos adicionar o campo "create" na criação do método ou
# pegar ele do kwargs e ele vai ser True se for uma criação.
@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()
