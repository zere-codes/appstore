from django.db.models import Count
from django.core.cache import cache
from .models import App, Category, Review


def store_menu(request):
    categories=cache.get('menu_categories')
    if categories is None:
        categories = list(
            Category.objects
            .annotate(apps_count=Count('app')).filter(apps_count__gt =0)
            .order_by('name')
        )
        cache.set('menu_categories', categories, 60*3)
    featured = App.objects.order_by('-price').first()

    favorites_count=0
    if request.user.is_authenticated:
        favorites_count=request.user.favorite_apps.count()

    apps_count = cache.get('apps_count')
    if apps_count is None:
        apps_count = App.objects.count()

    cache.set('apps_count', apps_count, 60 * 10)


    return {
        'categories': categories,
        'apps_total': apps_count,
        'categories_total': len(categories),
        'reviews_total': Review.objects.count(),
        'featured': featured,
        'favorites_count': favorites_count,
    }





