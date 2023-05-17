from django.urls import path 
from . import views 

urlpatterns =[
    path('', views.AlertList.as_view()),
    path('Alert/<int:pk>/', views.AlertDetail.as_view()),
    path('Alert/', views.AlertList.as_view()),

    path('Alerttext/<int:pk>/', views.AlertTextDetail.as_view()),
    path('Alerttext/', views.AlertTextList.as_view()),

    path('Alertmultimedia/<int:pk>/', views.AlertTextMultimediaDetail.as_view()),
    path('Alertmultimedia/', views.AlertTextMultimediaList.as_view())

]