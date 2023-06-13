from django.shortcuts import render
from django.urls import path
from django.conf.urls import *
from . import views

urlpatterns = [


    #Insert Api**************************************************
    
    path('Insert_Agency', views.Insert_Agency.as_view(), name='Insert_Agency'),
    path('Insert_Route', views.Insert_Route.as_view(), name='Insert_Route'),
    path('Insert_Trip', views.Insert_Trip.as_view(), name='Insert_Trip'),
    path('Insert_Stop', views.Insert_Stop.as_view(), name='Insert_Stop'),
    path('Insert_StopTime', views.Insert_StopTime.as_view(), name='Insert_StopTime'),
    path('Insert_Service', views.Insert_Service.as_view(), name='Insert_Service'),
    path('Insert_Service_Date', views.Insert_ServiceDate.as_view(), name='***Insert_ServiceDate'),
    path('Insert_Shape', views.Insert_Shape.as_view(), name='Insert_Shape'),
 
    #GetAll Api***********************************************************
    
    path('GetAll_Agency', views.GetAll_Agency.as_view(), name='GetAll_Agency'),
    path('GetAll_Route', views.GetAll_Route.as_view(), name='GetAll_Route'),
    path('GetAll_Trip', views.GetAll_Trip.as_view(), name='GetAll_Trip'),
    path('GetAll_Stop', views.GetAll_Stop.as_view(), name='GetAll_Stop'),
    path('GetAll_StopTime', views.GetAll_StopTime.as_view(), name='GetAll_StopTime'),
    path('GetAll_Service', views.GetAll_Service.as_view(), name='GetAll_Service'),
    path('GetAll_Service_Date', views.GetAll_ServiceDate.as_view(), name='GetAll_Service_Date'),
    path('GetAll_Shape', views.GetAll_Shape.as_view(), name='GetAll_Shape'),

  
    #Get Api**************************************************

    path('Get_Agency', views.Get_Agency.as_view(), name='Get_Agency'),
    path('Get_Route', views.Get_Route.as_view(), name='Get_Route'),
    path('Get_Trip', views.Get_Trip.as_view(), name='Get_Trip'),
    path('Get_Stop', views.Get_Stop.as_view(), name='Get_Stop'),
    path('Get_StopTime', views.Get_StopTime.as_view(), name='Get_StopTime'),
    path('Get_Service', views.Get_Service.as_view(), name='Get_Service'),
    path('Get_Service_Date', views.Get_Service_Date.as_view(), name='Get_Service_Date'),
    path('Get_Shape', views.Get_Shape.as_view(), name='Get_Shape'),

 
    #Update Api***********************************************************

    path('Update_Agency', views.Update_Agency.as_view(), name='Update_Agency'),
    path('Update_Route', views.Update_Route.as_view(), name='Update_Route'),
    path('Update_Trip', views.Update_Trip.as_view(), name='Update_Trip'),
    path('Update_Stop', views.Update_Stop.as_view(), name='Update_Stop'),
    path('Update_StopTime', views.Update_StopTime.as_view(), name='Update_StopTime'),
    path('Update_Service', views.Update_Service.as_view(), name='Update_Service'),
    path('Update_Service_Date', views.Update_ServiceDate.as_view(), name='Update_ServiceDate'),
    path('Update_Shape', views.Update_Shape.as_view(), name='Update_Shape'),

    #Delete Api***********************************************************
 
    path('Update_Agency', views.Delete_Agency.as_view(), name='Update_Agency'),
    path('Update_Route', views.Delete_Route.as_view(), name='Update_Route'),
    path('Update_Trip', views.Delete_Trip.as_view(), name='Update_Trip'),
    path('Update_Stop', views.Delete_Stop.as_view(), name='Update_Stop'),
    path('Update_StopTime', views.Delete_StopTime.as_view(), name='Update_StopTime'),
    path('Update_Service', views.Delete_Service.as_view(), name='Update_Service'),
    path('Update_Service_Date', views.Delete_ServiceDate.as_view(), name='Update_ServiceDate'),
    path('Update_Shape', views.Delete_Shape.as_view(), name='Update_Shape'),





]