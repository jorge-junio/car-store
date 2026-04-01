from django.db.models.signals import (
    pre_save, pre_delete, post_save, post_delete)
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory
from openai_api.client import get_car_ai_bio


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
    create = kwargs.get('create')
    # não vamos gerar bio em updates, só nos creates
    if create is True and not instance.bio:
        instance.bio = 'SEM BIO'
        # Essa linha foi comentada pois não temos tokens da plataforma
        # para testar a função, mas a ideia era ter a bio gerada
        # automaticamente pela IA.
        # instance.bio = get_car_ai_bio(
        #     model=instance.model,
        #     brand=instance.brand,
        #     year=instance.year
        # )


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
