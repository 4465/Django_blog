# login/views.py
from django.shortcuts import render, redirect
from login.models import User,Category,Post
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.paginator import Paginator


def index(request):
    post = Post.objects.all().order_by('-created_at')
    for i in post:
        i.body = i.body[0:20]
    return render(request, 'login/index.html',{'post': post})


def login(request):
    if request.method == "POST":
        message = "请检查填写内容"
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(name=username)
            if user.password == password:
                print("登录成功")
                request.session['username'] = username
                return redirect('/index/')
            else:
                message = "密码不正确"
                print(message)
                return HttpResponse(message)
        except:
            message = '用户名不存在'
            print(message)
            return HttpResponse(message)
    else:
        return render(request, 'login/login.html')


def register(request):
    if request.method == "POST":
        dic = request.POST
        message = "请检查你的输入"
        sql = User.objects.create(name=dic['username'],password=dic['password'],email=dic['email'],sex=dic['sex'])
        sql.save()
        return redirect('/index/')
    else:
        return render(request, 'login/register.html')


def logout(request):
    del request.session['username']
    return redirect('/index/')


def userPage(request,username):
    return render(request, 'login/user.html', {'user': username})
