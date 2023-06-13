from rest_framework import serializers
from .models import Employee,Agency,Route,Trip,ServiceDate,Service,Stop,StopTime,Shape,ShapePoint

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields =(     
        'idEmployee',
        'name', 
        'email',
        'phone',
        'password' 

        )
        
class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields =('agency_id','agency_name','url','timezone','phone')

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = (
        'service_id',
        'name', 
        'agency_name', 
        'monday',
        'tuesday', 
        'wednesday', 
        'thursday', 
        'friday', 
        'saturday', 
        'sunday', 
        'start_date', 
        'end_date', 

        )        

class ServiceDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceDate
        fields = (
        'service_id', 
        'date',
        'exception_type' 

        ) 

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = (
    'route_id', 
    'stop_times',     
    'agency_id',
    'short_name',
    'long_name',
    'desc ',
 
        )         