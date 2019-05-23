

from django.db import models
import datetime
# Create your models here.


class User(models.Model):
    '''用户表'''
    gender = (
        ('male','男'),
        ('female', '女'),
    )
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=128, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    #目录
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    #文章题目
    title = models.CharField(max_length=128)
    #文章主体
    body = models.TextField()
    #创建时间
    created_at = models.DateTimeField(auto_now_add=True)
    #更新时间
    updated_at = models.DateTimeField(null=True)
    #作者
    author = models.ForeignKey(User,related_name='post',on_delete=models.CASCADE)
    total_view = models.PositiveIntegerField(default=0)
    total_comment = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.title

