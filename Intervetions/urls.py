from django.urls import path 
from . import views 

urlpatterns =[
    path('', views.InterventionList.as_view()),
    path('Users/<int:pk>/', views.InterventionDetail.as_view()),
    path('Users/', views.InterventionList.as_view()),
]