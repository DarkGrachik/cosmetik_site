import random

from django.core import management
from django.core.management.base import BaseCommand
from production.models import *
from .utils import random_date, random_timedelta


def add_substances():
    Substance.objects.create(
        name="4-терт-бутил циклогексанол",
        description="Он является инновационным синтетическим соединением с выраженной противовоспалительной активностью.",
    )
    Substance.objects.create(
        name="Massocare",
        description="'Жидкий неионногенный ПАВ для гидрофильных масел, со-эмульгатор для эмульсий вода-в-масле.",
    )
    Substance.objects.create(
        name="Protein HPTW",
        description="Гидролизованные протеины пшеницы обладают сродством к кератину из которого состоит волос.",
    )
    Substance.objects.create(
        name="Ацетил тетрапептид-40",
        description="Ацетил тетрапептид-40 обладает противовоспалительным эффектом.",
    )
    Substance.objects.create(
        name="Гидроксипинаколона ретиноат",
        description="Гидроксипинаколона ретиноат – одна из наиболее современных форм ретиноидов.",
    )
    Substance.objects.create(
        name="Protein VEG",
        description="Гидролизованные растительные протеины обладают сродством к кератину из которого состоит волос.",
    )
    Substance.objects.create(
        name="Тетрабутан",
        description="Технологичный акрилатный эмульгатор и загуститель.",
    )

    print("Услуги добавлены")


def add_cosmetics():
    owners = User.objects.filter(is_superuser=False)
    moderators = User.objects.filter(is_superuser=True)

    if len(owners) == 0 or len(moderators) == 0:
        print("Заявки не могут быть добавлены. Сначала добавьте пользователей с помощью команды add_users")
        return

    substances = Substance.objects.all()

    for _ in range(30):
        cosmetic = Cosmetic.objects.create()
        cosmetic.name = "Косметика №" + str(cosmetic.pk)
        cosmetic.status = random.randint(2, 5)

        if cosmetic.status in [3, 4]:
            cosmetic.closed_date = random_date()
            cosmetic.formated_date = cosmetic.closed_date - random_timedelta()
            cosmetic.created_date = cosmetic.formated_date - random_timedelta()
        else:
            cosmetic.formated_date = random_date()
            cosmetic.created_date = cosmetic.formated_date - random_timedelta()

        cosmetic.owner = random.choice(owners)
        cosmetic.moderator = random.choice(moderators)

        for i in range(random.randint(1, 3)):
            try:
                item = SubCosm.objects.create()
                item.cosmetic = cosmetic
                item.substance = random.choice(substances)
                item.save()
            except Exception as e:
                print(e)

        cosmetic.save()

    print("Заявки добавлены")


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        management.call_command("clean_db")

        add_substances()
        add_cosmetics()









