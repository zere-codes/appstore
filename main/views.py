from django.shortcuts import render
from .models import App


def index(request):
    apps = App.objects.all()
    return render(request, 'main/index.html', {
        'apps': apps,
        'apps_count': App.objects.count(),
    })

def about(request):
    return render(request, 'main/about.html')