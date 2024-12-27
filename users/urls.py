
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [    
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
    path('account/', views.userAccount, name='account'),

    path('edit-account/', views.editAccount, name='edit-account'),
    path('create-child/', views.createChild, name='create-child'),
    path('update-child/<uuid:pk>/', views.updateChild, name='update-child'),
    path('delete-child/<uuid:pk>/', views.deleteChild, name='delete-child'),

    path('inbox/', views.inbox, name='inbox'),
    path('message/<str:pk>', views.viewMessage, name='message'),
    path('send-message/<str:pk>', views.createMessage, name='create-message'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)