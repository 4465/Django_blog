# Generated by Django 2.0.6 on 2019-05-24 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20190524_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.TextField(),
        ),
    ]
