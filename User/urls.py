from django.urls import path 
from . import views 

urlpatterns =[
    path('', views.UserList.as_view(), name='user-list'),
    path('<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('login/', views.LoginView.as_view(), name='user-login'),
    path('register/', views.RegisterView.as_view(), name='user-register'),
    path('community-leader/', views.CommunityLeaderLoginView.as_view(), name='leader-login'),
]