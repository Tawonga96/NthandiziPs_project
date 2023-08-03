from django.urls import path 
from . import views 


urlpatterns =[
    path('', views.AlertList.as_view()),
    path('Alert/<int:pk>/', views.AlertDetail.as_view()),
    path('Alert/', views.AlertList.as_view()),
    path('Create_alert/', views.AlertCreate.as_view(), name='create-alert'),  


    path('Alerttext/<int:pk>/', views.AlertTextDetail.as_view()),
    path('Alerttext/', views.AlertTextList.as_view()),
    # path('CreateAlert_text/', views.AlertTextCreate.as_view(), name='create-alert-text'),


    path('Alertmultimedia/<int:pk>/', views.AlertTextMultimediaDetail.as_view()),
    path('Alertmultimedia/', views.AlertTextMultimediaList.as_view()),
    # path('CreateAlert_multimedia/', views.AlertMultimediaCreate.as_view(), name='create-alert-multimedia'),


]
