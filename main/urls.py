
from django.urls import path, re_path
from . import views

app_name='main'

urlpatterns = [

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('app/<int:app_id>/', views.app_detail, name='app_detail'),
    path('category/<int:category_id>/', views.category_detail, name='category'),
    path('free/', views.free_apps, name='free'),
    path('new/', views.new, name='new'),
    path('top/', views.top, name='top'),
    path('nocategory/', views.no_category, name='nocategory'),
    path('/category_free/<int:category_id>/', views.category_free, name='category_free'),
    path('cheap/', views.cheap, name='cheap'),
    re_path(r'archive/(?P<year>[0-9]{4})/$', views.archive_year, name='archive'),
    path('developer/<str:name>/', views.developer, name='developer'),
    path('/app/secure/<uuid:key>/', views.secure, name='secure'),
]


