from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Adv
from django.db.models import Q

def get_random_advs(count=4):
    return Adv.objects.order_by('?')[:4]

def home_page(request):
    hot_posts = Post.objects.all().order_by('-created_at')[:4]
    posts = Post.objects.all().order_by('-created_at')
    advs = get_random_advs(request)
    context = {
        'hot_posts': hot_posts,
        'posts': posts,
        'advs': advs
    }
    return render(request, "index.html", context)

def all_news_page(request):
    posts = Post.objects.all().order_by('-created_at')
    advs = get_random_advs(request)
    context = {
        'advs': advs,
        'posts': posts
    }
    return render(request, "all-news.html", context)


def news_by_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category=category).order_by('-created_at')
    advs = get_random_advs(request)
    context = {
        'advs': advs,
        'category': category,
        'posts': posts
    }
    return render(request, "news-by-category.html", context)


def search_page(request):
    advs = get_random_advs(request)
    context = {
        'advs': advs
    }
    return render(request, "search.html", context)

def search_results(request):
    query = request.GET.get('q')
    advs = get_random_advs(request)
    results = []
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    context = {
        'advs': advs,
        'query': query,
        'results': results
    }
    return render(request, "search-results.html", context)

def read_news_page(request, pk):
    post = get_object_or_404(Post, pk=pk)
    advs = get_random_advs(request)
    context = {
        'advs': advs,
        'post': post
    }
    return render(request, "read-news.html", context)