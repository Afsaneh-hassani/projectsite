from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category, Comment
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def blog_view(request,**kwargs):
    posts=Post.objects.filter(published_date__lte=timezone.now(),status=1)
    if kwargs.get('cat_name')!=None:
        posts=posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username')!=None:
        posts=posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name')!=None:
        posts=posts.filter(tags__name__in=[kwargs['tag_name']])
        
    posts=Paginator(posts,3)    
    try:
        page_number=request.GET.get('page')
        posts=posts.get_page(page_number)
    except PageNotAnInteger:
        posts=posts.get_page(1)       
    except EmptyPage:
        posts=posts.get_page(1)
    context={'posts': posts}
    return render(request,'blog/blog-home.html',context)








def blog_single(request,pid):
    posts=Post.objects.filter(status=1)
    post=get_object_or_404(posts,pk=pid)
    
    comments=Comment.objects.filter(post=post.id, approved=True)
    previous_post=Post.objects.filter(created_date__gt=post.created_date,published_date__lte=timezone.now(),status=1 ).order_by('created_date').first()
    next_post=Post.objects.filter(created_date__lt=post.created_date,published_date__lte=timezone.now(),status=1 ).order_by('-created_date').first()

    context={'post': post, 'previous_post':previous_post , 'next_post':next_post, 'comments':comments}
    return render(request,'blog/blog-single.html',context)

# Create your views here.



def test_view(request):
    return render(request,'blog/test.html')

def blog_category(request,cat_name):
    posts=Post.objects.filter(status=1)
    posts=posts.filter(category__name=cat_name)
    context={'posts': posts}
    return render(request,'blog/blog-home.html',context)


def blog_search(request):
    posts=Post.objects.filter(status=1)
    if request.method=='GET':
        if s:=request.GET.get('s'):
            posts=posts.filter(content__contains=s)
            
    context={'posts': posts}
    return render(request,'blog/blog-home.html',context)
