from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wifi/', views.wifi_generator, name='wifi'),
    path('link/', views.generate_link_code, name='link'),
    path('social/twitter/', views.social_twitter, name='twitter'),
    path('social/telegram/', views.social_telegram, name='telegram'),
    path('social/instagram/', views.social_insta, name='instagram'),
]