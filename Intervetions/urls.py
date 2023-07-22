from django.urls import path 
from . import views 

urlpatterns =[
    path('', views.InterventionList.as_view()),
    path('Interventions/<int:pk>/', views.InterventionDetail.as_view()),
    path('Interventions/', views.InterventionList.as_view()),

    path('CommunityCcreate/', views.InterventionCreate.as_view(), name='intervention-create'),
    path('PoliceInterventions/', views.PoliceInterventionCreate.as_view(), name='police-intervention'),

    # Status URLs
    path('', views.StatusList.as_view(), name='status-list'),
    path('status/<int:pk>/', views.StatusDetail.as_view()),
    path('StatusCreate/', views.StatusCreate.as_view(), name='status-create'),
]