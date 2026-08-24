from django.shortcuts import render
from .models import App


def index(request):
    apps = App.objects.order_by('name')

    featured = App.objects.order_by('-price').first()

    return render(request, 'main/index.html', {
        'apps': apps,
        'apps_count': App.objects.count(),
        'featured': featured,
    })


def about(request):
    return render(request, 'main/about.html')