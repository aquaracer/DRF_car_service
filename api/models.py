from django.contrib.auth.models import User
from django.core import validators
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group

from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def assign_group(sender, instance, created, **kwargs):
    """Сигнал, добавляющий созданного пользователя в группу editors"""

    if created:
        editors_group = Group.objects.get(name='editors')
        instance.groups.add(editors_group)


class Employee(models.Model):
    """Сотрудники"""

    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", validators=[validators.MaxValueValidator(120),
                                                                  validators.MinValueValidator(18)])
    position = models.CharField("Должность", max_length=60)
    photo = models.ImageField("Фото", upload_to="employees/")
    achievements = models.TextField("Достижения", max_length=2000,
                                    help_text="Информация об образовании, опыте, квалификации и профессиональных достижениях")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class Category(models.Model):
    """Категории"""

    name = models.CharField("Категория", max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Service(models.Model):
    """Услуга"""

    PERIOD = (
        (0, ''),
        (1, '6'),
        (2, '12'),
        (3, '24'),
    )

    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Фото", upload_to="services/", null=True, blank=True)
    employee = models.ManyToManyField(Employee, verbose_name="Cотрудник", related_name="service_employee")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    warranty = models.PositiveSmallIntegerField("Гарантийный срок", choices=PERIOD, help_text="Указать в месяцах")
    price = models.DecimalField("Стоимость услуги", max_digits=9, decimal_places=2, default=0,
                                help_text="Указывать сумму в рублях", validators=[validators.MinValueValidator(0)])
    url = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
