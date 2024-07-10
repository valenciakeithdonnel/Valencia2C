from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='registration'),
    path('logout/', views.logout_user, name="logout"),
]