# Generated by Django 3.0.4 on 2021-08-23 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sql_quest_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sql_syntax',
            name='sub2',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]