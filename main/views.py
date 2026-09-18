from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import App, Category, Review

from django.db.models import Q
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST

from django.http import JsonResponse, HttpResponse

from django.views.generic import TemplateView, ListView, DetailView
from .forms import ReviewForm
SORTS = {
    'new': '-created_at',
    'name': 'name',
    'price': 'price',
    'expensive': '-price'
}

def index(request):
    q = request.GET.get('q', '')
    sort = request.GET.get('sort', 'new')

    if q:
        apps = App.objects.filter(Q(name__icontains=q) | Q(description__icontains=q))
    else:
        apps = App.objects.all()

    apps = apps.order_by(SORTS.get(sort, '-created_at'))
    featured = App.objects.order_by('-price').first()
    categories = Category.objects.all()

    paginator = Paginator(apps, 3)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    return render(request, 'main/index.html', {
        'q': q,
        'sort': sort,
        'page_obj': page_obj,
        'featured': featured,
    })


# @require_GET
# def about(request):
#     return render(request, 'main/about.html')


class AboutView(TemplateView):
    template_name = 'main/about.html'

# def app_detail(request,app_id):
#     app = get_object_or_404(App, id=app_id)
#     similar=App.objects.filter(price__gte=app.price - 30, price__lte=app.price + 30).exclude(id=app.id)[:3]
#     return render(request,'main/app_detail.html',{'app':app, 'similar':similar})

class AppDetailView(DetailView):
    model = App
    template_name = 'main/app_detail.html'
    context_object_name = 'app'
    pk_url_kwarg = 'app_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        app = self.object

        context['similar'] = (
            App.objects.filter(
                price__gte=app.price - 10,
                price__lte=app.price + 10,
            )
            .exclude(id=app.id)[:3]
        )
        context['form']=ReviewForm()
        context['reviews']=app.review_set.order_by('-created_at')
        return context

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


class NewAppView(ListView):
    model=App
    template_name = 'main/new.html'
    context_object_name = 'apps'
    ordering = ['-created_at']
    paginate_by = 3

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



class AppsIsFreeListView(ListView):
    model = App
    template_name = 'main/apps_list.html'
    context_object_name = 'apps'

    def get_queryset(self):
        if self.kwargs.get('is_free'):
            return App.objects.filter(price=0)
        return App.objects.filter(price__gt=0)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs.get('is_free'):
            context['title'] = 'Бесплатные приложения'
        else:
            context['title'] = 'Платные приложения'
        return context

@require_POST
def add_review(request, app_id):
    app = get_object_or_404(App, id=app_id)
    form = ReviewForm(request.POST)

    if form.is_valid():
        review = form.save(commit=False)
        review.app = app
        review.save()
        return redirect('main:app_detail', app_id=app.id)

    reviews = app.review_set.order_by('-created_at')
    similar_apps = (
        App.objects.filter(
            price__gte=app.price - 10,
            price__lte=app.price + 10,
        )
        .exclude(id=app.id)[:3]
    )
    return render(request, 'main/app_detail.html', {
        'app': app,
        'form': form,
        'reviews': reviews,
        'similar_apps': similar_apps,
    })


def api_app_detail(request, app_id):
    app= get_object_or_404(App, id=app_id)
    data={
        'id': app_id,
        'name': app.name,
        'description': app.description,
        'price': app.price,
    }
    return JsonResponse(data)




