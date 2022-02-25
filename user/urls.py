from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('', views.index,name='index'),
    #path('companyregister', views.companyregister,name='companyregister'),
    path('register', views.user_register,name='register'),
    path('login', views.user_login,name='login'),
    path('logout', views.user_logout,name='logout'),
    path('feedback', views.feedback,name='feedback'),
    path('subscribe/<int:id>', views.user_subscribe,name='subscribe'),
    path('payment', views.user_payment,name='payment'),
    path('plan', views.user_plan,name='plan'),
    path('subscribe/subscribe', views.details,name='subscribedetails'),
    path('reviews', views.reviews,name="reviews")
]