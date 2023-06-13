from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.gis.db import models as gis_models
from django.core.exceptions import ValidationError
from gtfs.fields import SecondsField

# Create your models here.

#Table employee******************************
class Employee(models.Model):
    idEmployee=models.AutoField(primary_key=True,auto_created=True,unique=True,verbose_name="Identifiant Employee")
    name = models.CharField(max_length=200)
    email= models.EmailField(max_length=254,unique=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    password = models.CharField(max_length=254)

    def __str__(self):
        return '({}) {}'.format(self.idEmployee,self.name)


#Table Agency*********************************
class Agency(models.Model):
    agency_id = models.AutoField(auto_created=True,
        primary_key=True,
        help_text="Unique identifier for transit agency")
    agency_name = models.CharField(
        max_length=255,
        help_text="Full name of the transit agency")
    url = models.URLField(
        blank=True, help_text="URL of the transit agency")
    timezone = models.CharField(
        max_length=255,
        help_text="Timezone of the agency")
    phone = PhoneNumberField(
        max_length=255, blank=True,
        help_text="telephone number")
    
    def clean(self):
        # Vérifier si un enregistrement avec un même name existe déjà
        existing_agency = Agency.objects.filter(agency_name=self.agency_name,phone=self.phone).exclude(agency_id=self.agency_id).first()
        if existing_agency:
            raise ValidationError("agency with the same name or phone already exists.")
  
    def __str__(self):
        return '({}) {}'.format(self.phone,self.agency_name)
 

#Table Service*********************************

class Service(models.Model):
    """Dates that a route is active.
    """

    service_id = models.AutoField(auto_created=True,
        primary_key=True, 
        help_text="Unique identifier for service dates.")
    name = models.CharField(
        max_length=255, db_index=True,
        help_text="name of the service .")
    agency_name = models.ForeignKey('Agency', on_delete=models.CASCADE,blank=False,)
    monday = models.BooleanField(
        default=True,
        help_text="Is the route active on Monday?")
    tuesday = models.BooleanField(
        default=True,
        help_text="Is the route active on Tuesday?")
    wednesday = models.BooleanField(
        default=True,
        help_text="Is the route active on Wednesday?")
    thursday = models.BooleanField(
        default=True,
        help_text="Is the route active on Thursday?")
    friday = models.BooleanField(
        default=True,
        help_text="Is the route active on Friday?")
    saturday = models.BooleanField(
        default=True,
        help_text="Is the route active on Saturday?")
    sunday = models.BooleanField(
        default=True,
        help_text="Is the route active on Sunday?")
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def clean(self):
            if self.start_date and self.end_date:
                if self.start_date <= self.end_date:
                    raise ValidationError("End date must be greater than the start date.")

    def clean(self):
        # Vérifier si un enregistrement avec un même name existe déjà
        existing_service = Service.objects.filter(name=self.name).exclude(service_id=self.service_id).first()
        if existing_service:
            raise ValidationError("A service with the same name already exists.")
            
    def __str__(self):
        return '({}) {}'.format(self.service_id,self.name)
 

#Table Service_date*********************************

class ServiceDate(models.Model):
    """Dates that a service is active.
    """
    service_id = models.ForeignKey('Service', on_delete=models.CASCADE)
    date = models.DateField(
        help_text="Date that the service differs from the norm.")
    exception_type = models.IntegerField(
        default=1, choices=((1, 'Added'), (2, 'Removed')),
        help_text="Is service added or removed on this date?")

    def __str__(self):
        return "{}-{} {}".format(self.service_id, self.date, 'Added' if self.exception_type == 1 else 'Removed')
    

#Table route*********************************
class Route(models.Model):
    """A transit route
    """
    route_id = models.AutoField(auto_created=True,
        primary_key=True,
        help_text="Unique identifier for route.")
    stop_times = models.ManyToManyField(
        'StopTime',
        related_name='services',
        help_text="List of stop times associated with this service.")     
    agency_id = models.ForeignKey(
        'Agency',null=True, blank=True,on_delete=models.SET_NULL,
        help_text="Agency for this route.")
    short_name = models.CharField(
        max_length=63,
        help_text="Short name of the route")
    long_name = models.CharField(
        max_length=255,
        help_text="Long name of the route")
    desc = models.TextField(
        "description",
        blank=True,
        help_text="Long description of a route")

    def clean(self):
        # Vérifier si un enregistrement avec un même name existe déjà
        existing_route = Route.objects.filter(short_name=self.short_name).exclude(route_id=self.route_id).first()
        if existing_route:
            raise ValidationError("A route with the same name already exists.")
    
   
    def __str__(self):
        return '({}) {}'.format(self.long_name,self.short_name)
   
#Table Trip*********************************


class Trip(gis_models.Model):
    """A trip along a route
    """

    route_id = models.ForeignKey('Route', on_delete=models.CASCADE,)
    name = models.ForeignKey(
        'Service', null=True, blank=True, on_delete=models.SET_NULL)
    trip_id = models.AutoField(
        auto_created=True,primary_key=True,
        help_text="Unique identifier for a trip.")
    point = models.ManyToManyField(
        'Stop',
        related_name='Stop',
        help_text="Lon/Lat for insertion the stop location.")     
    headsign = models.CharField(
        max_length=255, blank=True,
        help_text="Destination identification for passengers.")
    short_name = models.CharField(
        max_length=63, blank=True,
        help_text="Short name used in schedules and signboards.")
    direction = models.CharField(
        max_length=1, blank=True,
        choices=(('0', '0'), ('1', '1')),
        help_text="Direction for bi-directional routes.")
    shape_id = models.ForeignKey(
        'Shape', null=True, blank=True, on_delete=models.SET_NULL,
        help_text="Shape used for this trip")
    departure_time = models.TimeField(
        null=True, blank=True,
        help_text="Time of the departure of a trip from a station")
    end_time = models.TimeField(
        null=True, blank=True,
        help_text="Time of the end of a trip to a station"    
    )
    def clean(self):
            if self.departure_time and self.end_time:
                if self.departure_time <= self.end_time:
                    raise ValidationError("End date must be greater than the start date.")

    def clean(self):
        # Vérifier si un enregistrement avec un même name existe déjà
        existing_trip = Service.objects.filter(headsign =self.headsign).exclude(trip_id=self.trip_id).first()
        if existing_trip:
            raise ValidationError("A Trip with the same name already exists.")
        
    def __str__(self):
        return '({}) {}'.format(self.route_id, self.trip_id)
    

#Table Stop*********************************

class Stop(gis_models.Model):
    """A stop or station
    """
    stop_id = models.AutoField(auto_created=True,
        primary_key=True,
        help_text="Unique identifier for a stop or station.")
    code = models.CharField(
        max_length=255, blank=True,
        help_text="Uniquer identifier (short text or number) for passengers.")
    name = models.CharField(
        max_length=255,
        help_text="Name of stop in local vernacular.")
    point = gis_models.PointField(
        help_text='WGS 84 latitude/longitude of stop or station')
    location_type = models.CharField(
        max_length=1, blank=True, choices=(('0', 'Stop'), ('1', 'Station')),
        help_text="Is this a 0:stop or 1:station?")

    def __str__(self):
        return '({}) {} {}'.format(self.name,self.point,self.location_type)

   
        
#Table Stop_Time*********************************

class StopTime(models.Model):
    """A specific stop on a route on a trip.
    """
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    arrival_time = models.TimeField(
        default=None, null=True, blank=True,
        help_text="Arrival time. Must be set for start stops of trip.")
    departure_time = models.TimeField(
        default=None, null=True, blank=True,
        help_text='Departure time. Must be set for end stops of trip with seconds.')
    stop_sequence = models.IntegerField()

    def __str__(self):
        return '({}) {}'.format(self.stop,self.stop_sequence)


#Table Shape*********************************

class Shape(models.Model):
    """The path the vehicle takes along the route.
    """
    shape_id = models.AutoField(
        primary_key=True,
        help_text="Unique identifier for a shape.")
    name = models.CharField(null=False,blank=False,
        help_text="Name of the shape of a trip")
    geometry = gis_models.LineStringField(
        null=True, blank=True,
        help_text='Geometry cache of ShapePoints')

    def __str__(self):
        return '({}) {}'.format(self.shape_id,self.name)

    
#Table ShapePoint*********************************


class ShapePoint(models.Model):
    """A point along the shape"""

    point = gis_models.PointField(
        help_text='WGS 84 latitude/longitude of shape point')
    sequence = models.IntegerField()
    traveled = models.FloatField(
        null=True, blank=True,
        help_text='Distance of point from start of shape')




