
from django.urls import path, re_path
from . import views

app_name='main'

urlpatterns = [

    path('', views.index, name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('app/<int:app_id>/', views.AppDetailView.as_view(), name='app_detail'),
    path('category/<int:category_id>/', views.category_detail, name='category'),
    path('free/', views.free_apps, name='free'),
    path('new/', views.NewAppView.as_view(), name='new'),
    path('top/', views.top, name='top'),
    path('nocategory/', views.no_category, name='nocategory'),
    path('category_free/<int:category_id>/', views.category_free, name='category_free'),
    path('cheap/', views.cheap, name='cheap'),
    path('free-apps/', views.apps_list, {'is_free': True}, name='free_apps'),
    path('paid-apps/', views.apps_list, {'is_free': False}, name='paid_apps'),
    path('api/app/<int:app_id>/', views.api_app_detail, name='api_app_detail'),
]


