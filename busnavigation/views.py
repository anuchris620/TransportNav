from django.shortcuts import render

# Create your views here.
from datetime import datetime, time
from busnavigation.models import Stops_time,CET_PATTOM_EASTFORT,Stops


def index(request):
    return render(request,'index.html')
     
def Route_Load(request):
    Departure=request.GET['start']
    Destination=request.GET['destination']
    Route1=["CET","Sreekaryam","Ulloor","Medical college","Kumarapuram","Kannamoola","General Hospital","Palayam","Statue","East fort"]    
    Route2=["CET","Sreekaryam","Ulloor","Medical college","Pottakuzhi","Pattom","PMG","Palayam","Statue","East fort"]
    Route3=["CET","Sreekaryam","Ulloor","Kesavadasapuram","Pattom","PMG","Palayam","Statue","East fort"]
    Db_Route=Stops_time.objects.all()
    current_time = datetime.now()
    formatted_time_check = current_time.strftime("%I:%M %p")
    t1 = datetime.strptime(formatted_time_check, '%I:%M %p')
    #Sel_Route=[]
    
    if  Departure in Route1 and Destination in Route1:
        start_position= Route1.index(Departure)
        end_position=Route1.index(Destination)
        if start_position < end_position: 
            Route_sel=["CET KANNAMOOLA EASTFORT"]
                        
        else:    
            Route_sel=["EASTFORT KANNAMOOLA CET"]
        
        time=[]
        Route=[]
        for Route_name in Db_Route:
            if Route_name.Routes in Route_sel:
                time2=Route_name.time1
                t2 = datetime.strptime(time2, '%I:%M %p')
                diff=t2-t1
                print(diff)
                hours, remainder = divmod(diff.seconds, 3600)
                minutes, _ = divmod(remainder, 60)
            
                if float(str(hours)+"."+str(minutes))<=0.59:
                    print( float(str(hours)+"."+str(minutes)))
                    print(t2)

                
                    time.append(Route_name)
                    print(time)
                else:
                    Route.append(Route_name)
                #Sel_Route.append(Route_name)
    if time:   
        return render(request,'Route_load.html',{'time':time,'Route':Route})
    else:
        msg="Currently busses are not available,you can check for available buses"
        return render(request,'Route_load.html',{'time':time,'Route':Route,'msg':msg})
    
def Map_Load(request):
    if request.method=="GET":
        Route_name=request.GET['routes']
        Start_time=request.GET['departure_times']
        Db_Route=Stops_time.objects.all()
        Db_Stops=Stops.objects.all()
                
        for i in Db_Route:
                   
            if i.Routes==Route_name:
                if i.time1==Start_time:
                    timevalue=i
                    print(timevalue)

                        #time_start.append(i.time1)
                        #time_end.append(i.time10)
        for y in Db_Stops:

            if y.Route==Route_name:
                stops=y

    return render(request,'map_load.html',{'timevalue':timevalue, 'Db_Stops': Db_Stops,'stops':stops})