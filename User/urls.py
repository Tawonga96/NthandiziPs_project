from django.urls import path 
from . import views 

urlpatterns =[
    path('', views.UserList.as_view()),
    path('Users/<int:pk>/', views.UserDetail.as_view()),
    path('Users/', views.UserList.as_view()),
]