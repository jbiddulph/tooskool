from django.urls import path
from . import views

urlpatterns = [
    path('', views.schools, name='schools'),
    path('school/<uuid:pk>/', views.school, name='school'),
    path('create-school/', views.createSchool, name='create-school'),
    path('update-school/<uuid:pk>/', views.updateSchool, name='update-school'),
    path('delete-school/<uuid:pk>/', views.deleteSchool, name='delete-school'),
]