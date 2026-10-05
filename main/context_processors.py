from django.db.models import Count
from .models import App, Category, Review


def store_menu(request):
    categories = list(
        Category.objects
        .annotate(apps_count=Count('app')).filter(apps_count__gt =0)
        .order_by('name')
    )
    featured = App.objects.order_by('-price').first()

    favorites_count=0
    if request.user.is_authenticated:
        favorites_count=request.user.favorite_apps.count()
    return {
        'categories': categories,
        'apps_total': App.objects.count(),
        'categories_total': len(categories),
        'reviews_total': Review.objects.count(),
        'featured': featured,
        'favorites_count': favorites_count,
    }

