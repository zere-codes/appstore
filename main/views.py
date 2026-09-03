from django.shortcuts import render, get_object_or_404
from .models import App, Category
from django.http import HttpResponse


def index(request):
    apps = App.objects.order_by('name')

    featured = App.objects.order_by('-price').first()
    category=Category.objects.all()

    return render(request, 'main/index.html', {
        'apps': apps,
        'apps_count': App.objects.count(),
        'featured': featured,
        'categories': category,
    })


def about(request):
    return render(request, 'main/about.html')


def app_detail(request,app_id):
    app = get_object_or_404(App, id=app_id)
    similar=App.objects.filter(price__gte=app.price - 30, price__lte=app.price + 30).exclude(id=app.id)[:3]
    return render(request,'main/app_detail.html',{'app':app, 'similar':similar})


def category_detail(request,category_id):
    category=get_object_or_404(Category, id=category_id)
    apps=App.objects.filter(category=category)
    top_app=apps.order_by('-price').first()
    return render(request, 'main/category.html', {
        'category':category,
        'apps':apps,
        'top_app': top_app
    })

def free_apps(request):
    apps = App.objects.filter(price=0)
    return render(request, 'main/free.html', {
        'apps':apps
    })

def new(request):
    apps = App.objects.order_by('-created_at')[:5]
    return render(request,'main/new.html',{'apps':apps})

def top(request):
    apps = App.objects.exclude(price=0).order_by('-price')[:11]
    return render(request,'main/top.html',{'apps':apps})

def no_category(request):
    apps = App.objects.filter(category=None)
    return render(request,'main/nocategory.html',{'apps':apps})

def category_free(request, category_id):
    category = Category.objects.get(id=category_id)
    apps = App.objects.filter(category=category, price=0)
    return render(request, 'main/category_free.html', {'apps': apps})

def cheap(request):
    apps = App.objects.filter(price__gt=0, price__lt=100).order_by('price')
    return render(request, 'main/cheap.html', {'apps': apps})






