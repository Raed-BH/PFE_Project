from django.conf import settings
from django.shortcuts import render
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
from gtfs.models import Agency,Service,ServiceDate,Shape,ShapePoint,Stop,StopTime,Trip,Route
# Create your views here.

#Login**********************************************



class Insert_Agency(APIView):
    def post(self, request, format=None):
        try:
            gname = request.POST.get('name', None)
            gurl= request.POST.get('url', None)
            gtimezone = request.POST.get('timezone', None)
            gphone = request.POST.get('phone', None)
            if Agency.objects.filter(name=gname,url=gurl,timezone=gtimezone,phone=gphone).first()==None:
                a=Agency.objects.create(name=gname,url=gurl,timezone=gtimezone,phone=gphone)
                serialized_obj = serializers.serialize('json', [ a, ])
                return Response({'Reponse':'Success','Agency':serialized_obj})
            return Response({'Reponse':'Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})        

class Insert_Service(APIView):
    def post(self, request, format=None):
        try:
            gserviceId = request.Post.get('service_id',None)
            gname = request.POST.get('name', None)
            gmonday= request.POST.get('monday', None)
            gtuesday = request.POST.get('tuesday', None)
            gwednesday = request.POST.get('wednesday', None)
            gthursday = request.POST.get('thursday', None)
            gfriday = request.POST.get('friday', None)
            gsaturday = request.POST.get('saturday', None)
            gsunday = request.POST.get('sunday', None)
            gstartDate = request.POST.get('start_date', None)
            gendDate = request.POST.get('end_date', None)

            if Service.objects.filter(service_id=gserviceId).first()==None:
                s=Service.objects.create(service_id=gserviceId,name=gname,monday=gmonday,tuesday=gtuesday,wednesday=gwednesday,thursday=gthursday,friday=gfriday,saturday=gsaturday,sunday=gsunday,start_date=gstartDate,end_date=gendDate)
                serialized_obj = serializers.serialize('json', [ s, ])
                return Response({'Reponse':'Success','Service':serialized_obj})
            return Response({'Reponse':'Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})  

class Insert_ServiceDate(APIView):
  def post(self, request, format=None):
        try:
            gidservice = Service.objects.filter(service_id=gidservice)
            gdate = request.POST.get('date', None)
            gexptype= request.POST.get('exception_type', None)
            
            if Service.objects.filter(service_id=gidservice).first()==None:
                sd=ServiceDate.objects.create(date=gdate,exception_type=gexptype)
                serialized_obj = serializers.serialize('json', [ sd, ])
                return Response({'Reponse':'Success','Service_date':serialized_obj})
            return Response({'Reponse':'Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})  
class Insert_Route(APIView):
    def post(self, request, format=None):
        try:
            grouteid = request.POST.get('route_id',None)
            gagencyid = Agency.objects.filter(agency=gagencyid)
            gshortname = request.POST.get('short_name',None)
            glongname = request.POST.get('long_name',None)
            gdesc = request.POST.get('desc',None) 
            if Route.objects.filter(route_id=grouteid).first()==None:
                r=Route.objects.create(route_id=grouteid,agency_id=gagencyid,short_name=gshortname,long_name=glongname,desc=gdesc)
                serialized_obj = serializers.serialize('json', [ r, ])
                return Response({'Reponse':'Success','Route':serialized_obj})
            return Response({'Reponse':'Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'}) 

class Insert_Trip(APIView):
    def post(self, request, format=None):
        try:
            grouteid = Route.objects.filter(stop_id=grouteid)
            gserviceid = Service.objects.filter(service_id=gserviceid)           
            gtripid = request.POST.get('trip_id',None)
            gheadsign = request.POST.get('headsign',None)
            gshortname = request.POST.get('short_name',None)
            gdir = request.POST.get('direction',None)
            gshape = request.POST.get('shape',None)
            ggeo = request.POST.get('geometry',None) 
 
            if Trip.objects.filter(trip_id=grouteid,).first()==None:
                tr=Trip.objects.create(trip_id=grouteid,service_id=gserviceid,trip_id=gtripid,headsign=gheadsign,short_name=gshortname,direction=gdir,shape=gshape,geometry=ggeo)
                serialized_obj = serializers.serialize('json', [ tr, ])
                return Response({'Reponse':'Success','Stop':serialized_obj})
            return Response({'Reponse':'Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})           
class Insert_Stop(APIView):
    def post(self, request, format=None):
        try:
            gstopid = request.POST.get('stop_id',None)
            gcode = request.POST.get('code',None)
            gname = request.POST.get('name',None)
            gpoint = request.POST.get('point',None)
            glocation = request.POST.get('location_type',None)
            gparentstation = request.POST.get('parent_station',None) 
            if Stop.objects.filter(stop_id=gstopid).first()==None:
                st=Stop.objects.create(stop_id=gstopid,code=gcode,name=gname,point=gpoint,location_type=glocation,parent_station=gparentstation)
                serialized_obj = serializers.serialize('json', [ st, ])
                return Response({'Reponse':'Success','Stop':serialized_obj})
            return Response({'Reponse':'Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'}) 

class Insert_StopTime(APIView):
    def post(self, request, format=None):
        try:
            gstopid = Stop.objects.filter(stop_id=gstopid)
            gtripid = Trip.objects.filter(trip_id=gtripid)
            garrtime = request.POST.get('arrival_time',None)
            gdeptime = request.POST.get('departure_time',None)
            gstopseq = request.POST.get('stop_sequence',None)
            gstophead = request.POST.get('stop_headsign',None) 
            if StopTime.objects.filter(stop_id=gstopid).first()==None:
                stt=StopTime.objects.create(stop_id=gstopid,trip_id=gtripid,arrival_time=garrtime,departure_time=gdeptime,stop_sequence=gstopseq,stop_headsign=gstophead)
                serialized_obj = serializers.serialize('json', [ stt, ])
                return Response({'Reponse':'Success','Stop':serialized_obj})
            return Response({'Reponse':'Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})  

class Insert_Shape(APIView):
    def post(self, request, format=None):
        try:
            gshapeid = request.POST.get('shape_id',None)
            ggeo = request.POST.get('geometry',None) 

            if Shape.objects.filter(shape_id=gshapeid).first()==None:
                shp=Shape.objects.create(shape_id=gshapeid,geometry=ggeo)
                serialized_obj = serializers.serialize('json', [ shp, ])
                return Response({'Reponse':'Success','Stop':serialized_obj})
            return Response({'Reponse':'Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'}) 

class Insert_shapePoint(APIView):
    def post(self, request, format=None):
        try:
            gshapeid = Shape.objects.filter(shape_id=gshapeid)
            gpoint = request.POST.get('point',None) 
            gseq = request.POST.get('sequence',None)
            gtraveled =request.POST.get('traveled',None)

            if ShapePoint.objects.filter(shape_id=gshapeid).first()==None:
                shpp=ShapePoint.objects.create(shape_id=gshapeid,point=gpoint,sequence=gseq,traveled=gtraveled)
                serialized_obj = serializers.serialize('json', [ shpp, ])
                return Response({'Reponse':'Success','Stop':serialized_obj})
            return Response({'Reponse':'Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'}) 
                                                                
#Update***************************************************

class Update_Agency(APIView):
    def post(self, request, format=None): 
        try:
            gid = request.POST.get('agency_id', None)
            gname = request.POST.get('name', None)
            gurl= request.POST.get('url', None)
            gtimezone = request.POST.get('timezone', None)
            gphone = request.POST.get('phone', None)


            if Agency.objects.filter(agency_id=gid).first()!=None:
                ag=Agency.objects.filter(agency_id=gid).update(name=gname,url=gurl,timezone=gtimezone,phone=gphone)
                return Response({'Reponse':'Success'})
            return Response({'Reponse':'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})
        
class Update_Service(APIView):
    def post(self, request, format=None): 
        try:
            gserviceid = request.Post.get('service_id',None)
            gname = request.POST.get('name', None)
            gmonday= request.POST.get('monday', None)
            gtuesday = request.POST.get('tuesday', None)
            gwednesday = request.POST.get('wednesday', None)
            gthursday = request.POST.get('thursday', None)
            gfriday = request.POST.get('friday', None)
            gsaturday = request.POST.get('saturday', None)
            gsunday = request.POST.get('sunday', None)
            gstartDate = request.POST.get('start_date', None)
            gendDate = request.POST.get('end_date', None)

            if Agency.objects.filter(service_id=gserviceid).first()!=None:
                s=Agency.objects.filter(service_id=gserviceid).update(name=gname,monday=gmonday,tuesday=gtuesday,wednesday=gwednesday,thursday=gthursday,friday=gfriday,saturday=gsaturday,sunday=gsunday,start_date=gstartDate,end_date=gendDate)
                return Response({'Reponse':'Success'})
            return Response({'Reponse':'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})  

class Update_ServiceDate(APIView):
  def post(self, request, format=None):
        try:
            gserviceid = request.Post.get('service_id',None)
            gdate = request.POST.get('date', None)
            gexptype= request.POST.get('exception_type', None)
            
            if Service.objects.filter(service_id=gserviceid).first()!=None:
                sd=ServiceDate.objects.filter(service_id=gserviceid).update(date=gdate,exception_type=gexptype)
                return Response({'Reponse':'Success'})
            return Response({'Reponse':'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})  
class Update_Route(APIView):
    def post(self, request, format=None):
        try:
            grouteid = request.POST.get('route_id',None)
            gagencyid = Agency.objects.filter(agency=gagencyid)
            gshortname = request.POST.get('short_name',None)
            glongname = request.POST.get('long_name',None)
            gdesc = request.POST.get('desc',None) 
            if Route.objects.filter(route_id=grouteid).first()!=None:
                r=Route.objects.filter(route_id=grouteid).update(route_id=grouteid,agency_id=gagencyid,short_name=gshortname,long_name=glongname,desc=gdesc)
                return Response({'Reponse':'Success'})
            return Response({'Reponse':'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'}) 

class Update_Trip(APIView):
    def post(self, request, format=None):
        try:
            grouteid = Route.objects.filter(stop_id=grouteid).first()
            gserviceid = Service.objects.filter(service_id=gserviceid)           
            gtripid = request.POST.get('trip_id',None)
            gheadsign = request.POST.get('headsign',None)
            gshortname = request.POST.get('short_name',None)
            gdir = request.POST.get('direction',None)
            gshape = request.POST.get('shape',None)
            ggeo = request.POST.get('geometry',None) 
 
            if Trip.objects.filter(trip_id=gtripid).first()!=None:
                tr=Trip.objects.filter(trip_id=gtripid).update(trip_id=grouteid,service_id=gserviceid,trip_id=gtripid,headsign=gheadsign,short_name=gshortname,direction=gdir,shape=gshape,geometry=ggeo)
                return Response({'Reponse':'Success'})
            return Response({'Reponse':'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})          
class Update_Stop(APIView):
    def post(self, request, format=None):
        try:
            gstopid = request.POST.get('stop_id',None)
            gcode = request.POST.get('code',None)
            gname = request.POST.get('name',None)
            gpoint = request.POST.get('point',None)
            glocation = request.POST.get('location_type',None)
            gparentstation = request.POST.get('parent_station',None) 
            if Stop.objects.filter(stop_id=gstopid).first()!=None:
                st=Stop.objects.filter(stop_id=gstopid).create(stop_id=gstopid,code=gcode,name=gname,point=gpoint,location_type=glocation,parent_station=gparentstation)
                return Response({'Reponse':'Success'})
            return Response({'Reponse':'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})

class Update_StopTime(APIView):
    def post(self, request, format=None):
        try:
            gstopid = Stop.objects.filter(stop_id=gstopid)
            gtripid = Trip.objects.filter(trip_id=gtripid)
            garrtime = request.POST.get('arrival_time',None)
            gdeptime = request.POST.get('departure_time',None)
            gstopseq = request.POST.get('stop_sequence',None)
            gstophead = request.POST.get('stop_headsign',None) 
            if StopTime.objects.filter(stop_id=gstopid).first()!=None:
                stt=StopTime.objects.filter(stop_id=gstopid).update(stop_id=gstopid,trip_id=gtripid,arrival_time=garrtime,departure_time=gdeptime,stop_sequence=gstopseq,stop_headsign=gstophead)
                return Response({'Reponse':'Success'})
            return Response({'Reponse':'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'}) 

class Update_Shape(APIView):
    def post(self, request, format=None):
        try:
            gshapeid = request.POST.get('shape_id',None)
            ggeo = request.POST.get('geometry',None) 

            if Shape.objects.filter(shape_id=gshapeid).first()!=None:
                shp=Shape.objects.filter(shape_id=gshapeid).update(shape_id=gshapeid,geometry=ggeo)
                return Response({'Reponse':'Success'})
            return Response({'Reponse':'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})

class Update_shapePoint(APIView):
    def post(self, request, format=None):
        try:
            gshapeid = Shape.objects.filter(shape_id=gshapeid)
            gpoint = request.POST.get('point',None) 
            gseq = request.POST.get('sequence',None)
            gtraveled =request.POST.get('traveled',None)

            if ShapePoint.objects.filter(shape_id=gshapeid).first()!=None:
                shpp=ShapePoint.objects.filter(shape_id=gshapeid).create(shape_id=gshapeid,point=gpoint,sequence=gseq,traveled=gtraveled)
                return Response({'Reponse':'Success'})
            return Response({'Reponse':'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})       
              
#Get***********************

class Get_Agency(APIView):
    def post(self, request, format=None):
        try:
            gidAgency = request.POST.get('agency_id', None)
            
            if Agency.objects.filter(agency_id=gidAgency).first()!=None:
                ag=Agency.objects.filter(agency_id=gidAgency).first()
                serialized_obj = serializers.serialize('json', [ ag, ])
                return Response({'Reponse':'Success','Agency':serialized_obj})
            return Response({'Reponse':'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})

class Get_Service(APIView):
    def post(self, request, format=None):
        try:
            gidservice = request.POST.get('service_id', None)
            
            if Service.objects.filter(service_id=gidservice).first()!=None:
                s=Service.objects.filter(service_id=gidservice).first()
                serialized_obj = serializers.serialize('json', [ s, ])
                return Response({'Reponse':'Success','Service':serialized_obj})
            return Response({'Reponse':'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})
          
class Get_Service_Date(APIView):
    def post(self, request, format=None):
        try:
            gidservice = request.POST.get('service_id', None)
            
            if ServiceDate.objects.filter(service_id=gidservice).first()!=None:
                sd=ServiceDate.objects.filter(service_id=gidservice).first()
                serialized_obj = serializers.serialize('json', [ sd, ])
                return Response({'Reponse':'Success','ServiceDate':serialized_obj})
            return Response({'Reponse':'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'}) 

class Get_Route(APIView):
    def post(self, request, format=None):
        try:
            gidroute = request.POST.get('route_id', None)
            
            if Route.objects.filter(route_id=gidroute).first()!=None:
                r=Route.objects.filter(route_id=gidroute).first()
                serialized_obj = serializers.serialize('json', [ r, ])
                return Response({'Reponse':'Success','Route':serialized_obj})
            return Response({'Reponse':'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})                       

class Get_Trip(APIView):
    def post(self, request, format=None):
        try:
            gidtrip = request.POST.get('route_id', None)
            
            if Trip.objects.filter(trip_id=gidtrip).first()!=None:
                t=Trip.objects.filter(trip_id=gidtrip).first()
                serialized_obj = serializers.serialize('json', [ t, ])
                return Response({'Reponse':'Success','Trip':serialized_obj})
            return Response({'Reponse':'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'}) 

class Get_Stop(APIView):
    def post(self, request, format=None):
        try:
            gidstop = request.POST.get('stop_id', None)
            
            if Stop.objects.filter(stop_id=gidstop).first()!=None:
                s=Stop.objects.filter(stop_id=gidstop).first()
                serialized_obj = serializers.serialize('json', [ s, ])
                return Response({'Reponse':'Success','Stop':serialized_obj})
            return Response({'Reponse':'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})  

class Get_StopTime(APIView):
    def post(self, request, format=None):
        try:
            gidstop = request.POST.get('route_id', None)
            
            if Trip.objects.filter(stop_id=gidstop).first()!=None:
                st=Trip.objects.filter(stop_id=gidstop).first()
                serialized_obj = serializers.serialize('json', [ st, ])
                return Response({'Reponse':'Success','StopTime':serialized_obj})
            return Response({'Reponse':'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})  
        
class Get_Shape(APIView):
    def post(self, request, format=None):
        try:
            gidshape = request.POST.get('shape_id', None)
            
            if Trip.objects.filter(shape_id=gidshape).first()!=None:
                sh=Trip.objects.filter(shape_id=gidshape).first()
                serialized_obj = serializers.serialize('json', [ sh, ])
                return Response({'Reponse':'Success','Shape':serialized_obj})
            return Response({'Reponse':'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})                       
#GetAll***********************************************************
class GetAll_Agency(APIView):
    def post(self, request, format=None):
        try:
            if Agency.objects.all()!=None:
                a=Agency.objects.all()
                serialized_obj = serializers.serialize('json',a )
                return Response({'Reponse':'Success','Agency':serialized_obj})
            return Response({'Reponse':'Not Exist'})   
        except:
            pass
            return Response({'Reponse':'Faild'})

class GetAll_Service(APIView):
     def post(self, request, format=None):
        try:
            if Service.objects.all()!=None:
                sr=Service.objects.all()
                serialized_obj = serializers.serialize('json',sr )
                return Response({'Reponse':'Success','Service':serialized_obj})
            return Response({'Reponse':'Not Exist'})   
        except:
            pass
            return Response({'Reponse':'Faild'})

class GetAll_ServiceDate(APIView):
    def post(self, request, format=None):
        try:
            if ServiceDate.objects.all()!=None:
                SD=ServiceDate.objects.all()
                serialized_obj = serializers.serialize('json',SD)
                return Response({'Reponse':'Success','ServiceDate':serialized_obj})
            return Response({'Reponse':'Not Exist'})   
        except:
            pass
            return Response({'Reponse':'Faild'})

class GetAll_Route(APIView):
    def post(self, request, format=None):
        try:
            if Route.objects.all()!=None:
                r=Route.objects.all()
                serialized_obj = serializers.serialize('json',r )
                return Response({'Reponse':'Success','Route':serialized_obj})
            return Response({'Reponse':'Not Exist'})   
        except:
            pass
            return Response({'Reponse':'Faild'})

class GetAll_Trip(APIView):
    def post(self, request, format=None):
        try:
            if Trip.objects.all()!=None:
                t=Trip.objects.all()
                serialized_obj = serializers.serialize('json',t )
                return Response({'Reponse':'Success','Trip':serialized_obj})
            return Response({'Reponse':'Not Exist'})   
        except:
            pass
            return Response({'Reponse':'Faild'})

class GetAll_Stop(APIView):
    def post(self, request, format=None):
        try:
            if Stop.objects.all()!=None:
                sp=Stop.objects.all()
                serialized_obj = serializers.serialize('json',sp )
                return Response({'Reponse':'Success','Stop':serialized_obj})
            return Response({'Reponse':'Not Exist'})   
        except:
            pass
            return Response({'Reponse':'Faild'})

class GetAll_StopTime(APIView):
    def post(self, request, format=None):
        try:
            if StopTime.objects.all()!=None:
                st=StopTime.objects.all()
                serialized_obj = serializers.serialize('json',st )
                return Response({'Reponse':'Success','StopTime':serialized_obj})
            return Response({'Reponse':'Not Exist'})   
        except:
            pass
            return Response({'Reponse':'Faild'})

class GetAll_Shape(APIView):
    def post(self, request, format=None):
        try:
            if Shape.objects.all()!=None:
                s=Shape.objects.all()
                serialized_obj = serializers.serialize('json',s )
                return Response({'Reponse':'Success','Shape':serialized_obj})
            return Response({'Reponse':'Not Exist'})   
        except:
            pass
            return Response({'Reponse':'Faild'})
        
#Delete***********************************************************

class Delete_Agency(APIView):
    def post(self, request, format=None):
        try:
            gidagency = request.POST.get('agency_id', None)
            
            if Agency.objects.filter(agency_id=gidagency).first()!=None:
                ag=Agency.objects.filter(agency_id=gidagency).delete()
                return Response({'Reponse':'Success'})
            return Response({'Reponse':'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})

class Delete_Service(APIView):
    def post(self, request, format=None):
        try:
            gidservice = request.POST.get('service_id', None)
            
            if Service.objects.filter(service_id=gidservice).first()!=None:
                s=Service.objects.filter(service_id=gidservice).delete()
                return Response({'Reponse':'Success'})
            return Response({'Reponse':'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})        

class Delete_ServiceDate(APIView):
    def post(self, request, format=None):
        try:
            gidservice = request.POST.get('service_id', None)
            
            if ServiceDate.objects.filter(service_id=gidservice).first()!=None:
                sd=ServiceDate.objects.filter(service_id=gidservice).delete()
                return Response({'Reponse':'Success'})
            return Response({'Reponse':'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})          

class Delete_Route(APIView):
    def post(self, request, format=None):
        try:
            gidroute = request.POST.get('route_id', None)
            
            if Route.objects.filter(route_id=gidroute).first()!=None:
                r=Route.objects.filter(route_id=gidroute).delete()
                return Response({'Reponse':'Success'})
            return Response({'Reponse':'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})          

class Delete_Trip(APIView):
    def post(self, request, format=None):
        try:
            gidtrip = request.POST.get('trip_id', None)
            
            if Trip.objects.filter(trip_id=gidtrip).first()!=None:
                t=Trip.objects.filter(trip_id=gidtrip).delete()
                return Response({'Reponse':'Success'})
            return Response({'Reponse':'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})          

class Delete_Stop(APIView):
    def post(self, request, format=None):
        try:
            gidstop = request.POST.get('stop_id', None)
            
            if Stop.objects.filter(stop_id=gidstop).first()!=None:
                s=Stop.objects.filter(stop_id=gidstop).delete()
                return Response({'Reponse':'Success'})
            return Response({'Reponse':'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})   

class Delete_StopTime(APIView):
    def post(self, request, format=None):
        try:
            gidstop = request.POST.get('stop_id', None)
            
            if StopTime.objects.filter(stop_id=gidstop).first()!=None:
                st=StopTime.objects.filter(stop_id=gidstop).delete()
                return Response({'Reponse':'Success'})
            return Response({'Reponse':'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})                  

class Delete_Shape(APIView):
    def post(self, request, format=None):
        try:
            gidshape = request.POST.get('shape_id', None)
            
            if Trip.objects.filter(shape_id=gidshape).first()!=None:
                s=Trip.objects.filter(shape_id=gidshape).delete()
                return Response({'Reponse':'Success'})
            return Response({'Reponse':'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})          