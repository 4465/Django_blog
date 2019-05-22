

from django.db import models
import datetime
# Create your models here.


class User(models.Model):
    '''用户表'''
    gender = (
        ('male','男'),
        ('female', '女'),
    )
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'

class Category(models.Model):
    name = models.TextField()

    def __unicode__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(null=True)
    created_by = models.ForeignKey(User,related_name='post',on_delete=models.CASCADE)
    username = models.CharField(max_length=128,null=True)

    def __unicode__(self):
        return self.title

