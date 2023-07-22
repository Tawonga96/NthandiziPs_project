from django.urls import path 
from . import views 
from Community.views import CitizenDetail, CitizenList

urlpatterns =[
    path('', views.UserList.as_view(), name='user-list'),
    path('<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('register/', views.UserRegistration.as_view(), name='user-registration'),

]