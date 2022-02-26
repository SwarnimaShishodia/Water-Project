from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    
    path('addplan', views.addplan,name='addplan'),
    path('companyregister', views.companyregister,name='companyregister'),
    path('admindashboard', views.admin_dashboard_view,name='admindashboard'),
    path('deletesupplier/<pk>', views.delete_supplier_view,name='deletesupplier'),
    path('delete-complain/<int:pk>', views.delete_complain_view,name='delete-complain'),
    path('complains', views.admin_complains,name='complains'),
    path('login_business', views.user_login,name='login_business'),
    path('signup_business', views.user_register,name='signup_business'),
    #path('adminclick', views.adminclick_view),
    #path('adminlogin', LoginView.as_view(template_name='adminlogin.html'),name='adminlogin'),
    
]