
from django.urls import path, re_path
from . import views

app_name='main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('app/<int:app_id>/', views.AppDetailView.as_view(), name='app_detail'),
    path('app/<int:app_id>/edit/', views.edit_app, name='edit_app'),
    path('app/<int:app_id>/review/', views.add_review, name='add_review'),
    path('category/<int:category_id>/', views.category_detail, name='category'),
    path('free/', views.free_apps, name='free'),
    path('new/', views.NewAppView.as_view(), name='new'),
    path('top/', views.top, name='top'),
    path('nocategory/', views.no_category, name='nocategory'),
    path('category_free/<int:category_id>/', views.category_free, name='category_free'),
    path('cheap/', views.cheap, name='cheap'),

    path('free-apps/', views.AppsIsFreeListView.as_view(), {'is_free': True}, name='free_apps'),
    path('paid-apps/', views.AppsIsFreeListView.as_view(), {'is_free': False}, name='paid_apps'),

    path('api/app/<int:app_id>/', views.api_app_detail, name='api_app_detail'),
    path('apps_list/', views.AppsIsFreeListView.as_view(), name='apps_list'),
    path('add_app/', views.add_app, name='add_app'),
    path('my_apps/', views.my_apps, name='my_apps'),



    path('register/', views.register, name='register'),
    path('login/', views.StrongLoginView.as_view(), name='login'),
    path('logout/', views.StrongLogoutView.as_view(), name='logout'),
    path('password-reset/', views.StorePasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.StorePasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.StorePasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/complete/', views.StorePasswordResetCompleteView.as_view(), name='password_reset_complete'),

]


