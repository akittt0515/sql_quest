from django.db import models
from django.db.models.fields import BooleanField, IntegerField

#基本情報データ
class std_data(models.Model):
    name=models.CharField(max_length=100)
    Lv=models.IntegerField(default=1)
    job=models.CharField(max_length=50)
    tribe=models.CharField(max_length=50)
    job_change_count=models.IntegerField(default=0)


# Create your models here.
