from django.urls import path 
from . import views 


urlpatterns =[
    # Police Station URLs
    path('', views.PolicestationList.as_view()),
    path('Policestation/<int:pk>/', views.PolicestationDetail.as_view()),
    path('Policestation/', views.PolicestationList.as_view()),
    path('Policestationcreate/', views.PolicestationCreate.as_view(), name='policestation-create'),


    # Job Posting URLs
    path('Jobposting/<int:pk>/', views.JobPostingDetail.as_view()),
    path('Jobposting/', views.JobPostingList.as_view()),
    path('create_jobposting/', views.JobPostingCreate.as_view(), name='create-jobposting'),

    # Police Officer URLs
    path('Policeofficer/<int:pk>/', views.PoliceofficerDetail.as_view()),
    path('Policeofficer/', views.PoliceofficerList.as_view()),
    path('Create_policeofficer/', views.PoliceofficerCreate.as_view(), name='create-police-officer'),

    # Subscribe URLs
    path('Subscriber/<int:pk>/', views.SubscribeDetail.as_view()),
    path('Subscriber/', views.SubscribeList.as_view()),
    path('SubscribeCreate/', views.SubscribeCreate.as_view(), name='subscribe-create'),




]