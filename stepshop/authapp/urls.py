from django.urls import path

from authapp.views import login, logout, register, edit

app_name = 'auth'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('edit/', edit, name='edit'),
]
