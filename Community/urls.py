from django.urls import path
from . import views

urlpatterns=[
    path('', views.CommunityList.as_view()),
    path('Community/<int:pk>/', views.CommunityDetail.as_view()),
    path('Community/', views.CommunityList.as_view()),
    path('Citizen/<int:pk>/', views.CitizenDetail.as_view()),
    path('Citizen/', views.CitizenList.as_view()),
    path('CommunityLeader/<int:pk>/', views.CommunityLeaderDetail.as_view()),
    path('CommunityLeader/', views.CommunityLeaderList.as_view()),
    path('Household/<int:pk>/', views.HouseholdDetail.as_view()),
    path('Household/', views.HouseholdList.as_view()),
    path('HouseMember/<int:pk>/', views.HousememberDetail.as_view()),
    path('HouseMember/', views.HousememberList.as_view()),
    path('Member/<int:pk>/', views.MemberDetail.as_view()),
    path('Member/', views.MemberList.as_view()),
]

