# Generated by Django 2.0.6 on 2019-05-24 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_post_total_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.TextField(max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]