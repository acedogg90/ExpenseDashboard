from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('logout_user/', views.logout_user, name='logout'),
]