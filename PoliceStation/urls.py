from django.urls import path 
from . import views 


urlpatterns =[
    path('', views.PolicestationList.as_view()),
    path('Policestation/<int:pk>/', views.PolicestationDetail.as_view()),
    path('Policestation/', views.PolicestationList.as_view()),

    path('Jobposting/<int:pk>/', views.JobPostingDetail.as_view()),
    path('Jobposting/', views.JobPostingList.as_view()),

    path('Policeofficer/<int:pk>/', views.PoliceofficerDetail.as_view()),
    path('Policeofficer/', views.PoliceofficerList.as_view()),

    path('Subscriber/<int:pk>/', views.SubscribeDetail.as_view()),
    path('Subscriber/', views.SubscribeList.as_view()),



]