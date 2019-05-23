from django.shortcuts import render, redirect
from login.models import User,Category,Post
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from markdown import  markdown
from datetime import datetime


@csrf_exempt
def article_create(request):
    if request.method == 'POST':
        category = request.POST['category']
        title = request.POST['title']
        body = request.POST['body']
        username = request.session['username']
        try:
            list = Category.objects.get(name=category)
            user = User.objects.get(name=username)
            user_id = user.id
            cate =  Category.objects.get(name=category)
            cate_id = cate.id
            sql = Post.objects.create(title=title, body=body,category_id=cate_id,author_id=user_id, author=user,category=cate, updated_at=datetime.now())
            sql.save()
        except:
            sql = Category.objects.create(name=category)
            sql.save()
            user = User.objects.get(name=username)
            user_id = User.objects.get(name=user).id
            cate = Category.objects.get(name=category)
            cate_id = cate.id
            sql = Post.objects.create(title=title,body=body,category_id=cate_id,author_id=user_id, author=user, category=cate,updated_at=datetime.now())
            sql.save()
        return redirect('/index/')
    else:
        return render(request,'article/article_edit.html')


def article_del(request,id):
    #根据id获取需要删除的文章
    print("删除的文章id为：",id)
    article = Post.objects.get(id=id)
    #调用.delete()方法删除文章
    article.delete()
    #完成删除后返回首页
    return redirect('/index/')


def getUpdateArticle(request,id):
    print("编辑的文章id为",id)
    article = Post.objects.get(id=id)
    context = {'article':article}
    return render(request,'article/article_update.html',context)


def article_update(request, id):
    if request.method == 'POST':
        print("POST")
        title = request.POST['title']
        category = request.POST['category']
        body = request.POST['body']
        print(category)
        try:
            print(category)
            print("更新数据库")
            #查询修改后的目录
            cat = Category.objects.get(name=category)
            #查询修改后的文章
            article = Post.objects.get(id=id)
            article.category = cat
            article.title = title
            article.body = body
            article.updated_at = datetime.now()
            print(body)
            article.save(update_fields=['updated_at'])
        except:
            print("新建目录")
            sql = Category.objects.create(name=category)
            sql.save()
            cate_id = Category.objects.get(name=category).id
            sql.save()
        return redirect('/article/'+request.session['username']+'/'+id +'/')
    else:
        print("错误")
        return render(request,'article/article_edit.html')


def postPage(request, username, postID):
    p = Post.objects.get(id=int(postID))
    p.total_view += 1
    p.save(update_fields=['total_view'])
    p.body = markdown(p.body,extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    return render(request, 'article/postPage.html', {'user': username, 'postID': postID, 'post': p})