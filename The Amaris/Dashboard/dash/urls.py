from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Amaris'),
    path('logout', views.logout, name='logout'),
    path('entry', views.entry, name='newentry'),
    path('adddata', views.add, name='adddata'),
    path('datatable',views.data,name='table'),
    path('viewres<int:myid>',views.viewres,name='viewres'),
    path('chartjs',views.charts,name='charts'),
    path('deldata',views.deldata,name='deldata'),
]