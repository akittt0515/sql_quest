from django.db import models
from django.db.models.fields import BooleanField, IntegerField

#基本情報データ
class QA(models.Model):
    quest=models.TextField(
        verbose_name='',
        blank=True,
        null=True,
        max_length=1000,
    )
    answer=models.TextField(
        verbose_name='',
        blank=True,
        null=True,
        max_length=1000,
    )


# Create your models here.
