from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='registration'),
    path('logout/', views.logout_user, name="logout"),
    path('add_records/', views.add_record, name="add_records"),
    path('update_records/<int:pk>', views.update_record, name='update_records'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),

]