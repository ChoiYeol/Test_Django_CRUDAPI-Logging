from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Post, City
import logging
logger = logging.getLogger('my')
# Create your views here.
def index(request):
    return render(request,'main/index.html')

def blog(request):
    postlist = Post.objects.all()
    return render(request,'main/blog.html', {'postlist':postlist})

def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'main/posting.html', {'post':post})

def new_post(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        else:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        return redirect('/blog/')
    return render(request, 'main/new_post.html')

def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/blog/')
    return render(request, 'main/remove_post.html', {'Post': post})


def signIn_views(request):  
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
    return render(request, 'main/signIn.html') 
 

def signOut_views(request):
    logout(request) 
    return render(request, 'main/signIn.html') 

def post_view(request): 
    logger.info("INFO 레벨로 출력")
    # logger.in("INFO 레벨로 출력")
    logger.debug("debug 레벨로 출력")
    posts = City.objects.all().order_by('-id') #Post테이블의 모든 객체 불러와서 posts변수에 저장
    return render(request, 'main/post_view.html',{"posts": posts})

def post_view_insert(request):
    # if request.method == 'City':
    # print(request.POST['name'])
    if request.POST['name']:
        City.objects.create(
            name=request.POST['name'],
            countryCode=request.POST['countryCode'],
            district=request.POST['district'],
            population=request.POST['population'],
        )

    return render(request, 'main/post_view.html')
 