# Generated by Django 2.0.6 on 2019-05-23 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20190523_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.TextField(max_length=128, unique=True),
        ),
    ]
