from django.urls import path
from .views import *
urlpatterns = [
   path('',profiles,name='profiles'),
   path('login/',login_user,name='login'),
   path('register/',register_user,name='register'),
   path('logout/',logout_user,name='logout'),
   path('account/',account_user,name='account'),
   path('account_edit/',account_edit,name='account_edit'),
   path('profile/<str:id>/',profile,name='profile'),
]