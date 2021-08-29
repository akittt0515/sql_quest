from django.db import models
from django.db.models.fields import BooleanField, IntegerField

#基本情報データ
class std_data(models.Model):
    name=models.CharField(max_length=100)
    Lv=models.IntegerField(default=1)
    job=models.CharField(max_length=50)
    tribe=models.CharField(max_length=50)
    job_change_count=models.IntegerField(default=0)

class QA_data(models.Model):
    QA_No=models.CharField(max_length=100)
    OV=models.TextField(
        blank=True,
        null=True,
        max_length=1000,
    )

class SQL_syntax(models.Model):
    syntax=models.TextField(
        
        blank=True,
        null=True,
        max_length=1000,
    )
    sub=models.TextField(
        
        blank=True,
        null=True,
        max_length=1000,
    )
    sub2=models.TextField(
        
        blank=True,
        null=True,
        max_length=1000,
    )
class QA(models.Model):
    quest=models.TextField(
        
        blank=True,
        null=True,
        max_length=1000,
    )
    sql_syn=models.TextField(
        
        blank=True,
        null=True,
        max_length=1000,
    )
    quest_table=models.TextField(
        
        blank=True,
        null=True,
        max_length=1000,
    )
    answer_table=models.TextField(
        
        blank=True,
        null=True,
        max_length=1000,
    )
class QC(models.Model):
    s=models.TextField(
        
        blank=True,
        null=True,
        max_length=1000,
    )
    h=models.TextField(
        
        blank=True,
        null=True,
        max_length=1000,
    )
    z=models.TextField(
        
        blank=True,
        null=True,
        max_length=1000,
    )

# Create your models here.
