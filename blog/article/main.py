from django.shortcuts import render, redirect
from login.models import User,Category,Post
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from markdown import  markdown

@csrf_exempt
def article_create(request):
    if request.method == 'POST':
        category = request.POST['category']
        print(category)
        #print(category_list.name)
        try:
            print("目录已存在")
            category_list = Category.objects.get(name=category)
            title = request.POST['title']
            body = request.POST['body']
            user = request.session['username']
            user_id = User.objects.get(name=user).id
            print(user_id)
            cate_id = Category.objects.get(name=category).id
            print(cate_id)
            sql = Post.objects.create(title=title, body=body, category_id=cate_id, created_by_id=user_id,username=user)
            sql.save()
        except:
            print("新建目录")
            sql = Category.objects.create(name=category)
            sql.save()
            title = request.POST['title']
            body = request.POST['body']
            user = request.session['username']
            user_id = User.objects.get(name=user).id
            cate_id = Category.objects.get(name=category).id
            sql = Post.objects.create(title=title,body=body,category_id=cate_id,created_by_id=user_id,username=user)
            sql.save()
        return redirect('/index/')
    else:
        return render(request,'article/article_edit.html')


def postPage(request, username, postID):
    post = {}
    print(username)
    print(postID)
    p = Post.objects.get(id=int(postID))
    c = Category.objects.get(id=int(p.category_id))
    u = User.objects.get(name=username)
    print(p.category_id)
    post['title'] = p.title
    post['body'] = markdown(p.body)
    post['created_at'] = p.created_at
    post['category'] = c.name
    post['username'] = u.name
    return render(request, 'article/postPage.html', {'user': username, 'postID': postID, 'post': post})