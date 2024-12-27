from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('schools/', views.getSchools),
    path('schools/<str:pk>', views.getSchool),
    path('profiles/', views.getProfiles),
    path('profiles/<str:pk>', views.getProfile),
]