from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Work, MyBio

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'page_title': 'Блог'})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def works_list(request):
    works = Work.objects.all()
    return render(request, 'blog/works_list.html', {'works': works, 'page_title': 'Мои работы'})

def info(request):
    my_autobio = MyBio.objects.get()
    return render(request, 'blog/info.html', {'info': my_autobio, 'page_title': 'Обо мне'})
