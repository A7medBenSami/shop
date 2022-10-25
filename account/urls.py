from django.urls import path
from . import views

urlpatterns = [
    path('',views.account,name='account'),
    path('reg/',views.reg,name='reg'),
    path('logout/', views.logout, name='logout'),
]
