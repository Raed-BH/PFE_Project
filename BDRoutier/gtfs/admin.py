from django.contrib import admin
from .models import Agency,Route,Service,ServiceDate,Stop,StopTime,Shape,ShapePoint,Trip
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
admin.site.register(Agency)
admin.site.register(Route)    
admin.site.register(Service)
admin.site.register(ServiceDate)
admin.site.register(Stop, LeafletGeoAdmin)
admin.site.register(StopTime)
admin.site.register(Shape, LeafletGeoAdmin)

admin.site.register(Trip, LeafletGeoAdmin)




