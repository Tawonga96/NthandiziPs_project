from django.urls import path
from . import views

urlpatterns=[
    path('', views.CommunityList.as_view()),
    path('Community/<int:pk>/', views.CommunityDetail.as_view()),
    path('Community/', views.CommunityList.as_view()),
    path('CommunityCreate/', views.CommunityCreate.as_view(), name='community-create'),

    path('Citizen/<int:pk>/', views.CitizenDetail.as_view()),
    path('Citizen/', views.CitizenList.as_view()),
    path('CitizenRegister/', views.CitizenRegistration.as_view(), name='citizen-registration'),
    # path('CitizenLogin/', views.CitizenLogin.as_view(), name='citizen-login'),

    path('CommunityLeader/<int:pk>/', views.CommunityLeaderDetail.as_view()),
    path('CommunityLeader/', views.CommunityLeaderList.as_view()),
    path('CommunityLeaderCreate/', views.CommunityLeaderCreate.as_view()),

    path('Household/<int:pk>/', views.HouseholdDetail.as_view()),
    path('Household/', views.HouseholdList.as_view()),
    path('HouseMember/<int:pk>/', views.HousememberDetail.as_view()),
    path('HouseMember/', views.HousememberList.as_view()),
   
    path('Member/<int:pk>/', views.MemberDetail.as_view()),
    path('Member/', views.MemberList.as_view()),
    path('MemberCreate/', views.MemberCreate.as_view(), name='member-create'),

]

