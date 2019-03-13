from django.shortcuts import render
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('home/', views.index, name='index'),
	path('submit/', views.submit, name='submit'),
	path('view/', views.view, name='view'),
	path('edit/', views.edit, name='edit'),
	path('delete/', views.delete, name='delete'),
	]
