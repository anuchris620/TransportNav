from django.shortcuts import render

# Create your views here.
from datetime import datetime, time
from busnavigation.models import Stops_time,CET_PATTOM_EASTFORT,Stops


def index(request):
    return render(request,'index.html')




"""def Route_Load(request):
    if request.method=="GET":
        Start=request.GET['start']
        Destination=request.GET['destination']
        # Get the current time
        current_time = datetime.now()

        # Format the current time to display in AM/PM
        formatted_time = current_time.strftime("%H.%M")
        current_format_time=float(formatted_time)
        

        common=["CET","Sreekaryam","Pongumoodu","ulloor","Palayam","Statue","Ayurvedic college","East fort"]
        #Route1=["CET","Sreekaryam","Pongumoodu","ulloor","Medical college","Kumarapuram","Kannamoola","General Hospital","Palayam","Statue","Ayurvedic college","East fort"] 
        Route1=["CET","Sreekaryam","ulloor","Medical college","Kumarapuram","Kannamoola","General Hospital","Palayam","Statue","East fort"]    
        Route2=["CET","Sreekaryam","Pongumoodu","ulloor","Medical college","Pottakuzhi","Pattom","Plamoodu","Palayam","Statue","Ayurvedic college","East fort"]
        Route3=["CET","Sreekaryam","Pongumoodu","ulloor","Kesavadasapuram","Pattom","Plamoodu","Palayam","Statue","Ayurvedic college","East fort"]


        if Start in  common and Destination in common: 
            start_position = common.index(Start)             #1= cet to eastfort, 2= eastfort to cet
            end_postion=common.index(Destination)
            if start_position < end_postion:
                direction=1
                Db_Route=Stops_time.objects.all()
                Route_val=["CET KANNAMOOLA EASTFORT","CET PATTOM EASTFORT","CET MEDICALCOLLEGE EASTFORT"]
                for i in Db_Route:
                    if i in Route_val:
                        print(i)


            if start_position > end_postion:
                direction=2







        if Start in  Route1 and Destination in Route1: 
            start_position = Route1.index(Start)             #1= cet to eastfort, 2= eastfort to cet
            end_postion = Route1.index(Destination)  

            
              
            if start_position < end_postion:
                direction=1
                #Route=["CET KANNAMOOLA EASTFORT","CET MEDICALCOLLEGE EASTFORT","CET PATTOM EASTFORT"]
                #for Route_val in Route:
                Route_val="CET KANNAMOOLA EASTFORT"

                Db_Route=Stops_time.objects.all()
                Db_Stops=CET_PATTOM_EASTFORT.objects.all()
                
                time=[]
                
                

                for i in Db_Route:
                   
                        
                    
                    
                    if i.Routes=="CET PATTOM EASTFORT":
                        if i.time1=="7:10PM":
                            timevalue=i
                            print(timevalue)

                        #time_start.append(i.time1)
                        #time_end.append(i.time10)
                for y in Db_Stops:
                    stops=y



                        


            
                #return render(request,'Route_load.html',{'timevalue':timevalue, 'time': time})
               

            else:
                direction=2
                Route=["EASTFORT KANNAMOOLA CET","EASTFORT MEDICALCOLLEGE CET","EASTFORT PATTOM CET"]

        elif Start in Route1 and Destination in Route1:
            start_position=Route1.index(Start)
            end_position=Route1.index(Destination)
            if start_position < end_position:
                direction=1
                Route="CET KANNAMOOLA EASTFORT"
                
            else:
                direction=2
                Route=["EASTFORT KANNAMOOLA CET"]

        elif Start in Route2 and Destination in Route2:
            start_position=Route2.index(Start)
            end_position=Route2.index(Destination)
            if start_position < end_position:
                direction=1
                Route=["CET MEDICALCOLLEGE EASTFORT"]
                
            else:
                direction=2
                Route=["EASTFORT MEDICALCOLLEGE CET"]

        elif Start in Route3 and Destination in Route3:
            start_position=Route3.index(Start)
            end_position=Route3.index(Destination)
            if start_position < end_position:
                direction=1
                Route=["CET PATTOM EASTFORT"]
                
            else:
                direction=2
                Route=["EASTFORT PATTOM CET"]"""

def Route_Load(request):
    Departure=request.GET['start']
    Destination=request.GET['destination']

    current_time = datetime.now()
    formatted_time_check = current_time.strftime("%I:%M%p").lstrip('0').replace(' 0', ' ')
    formatted_time_condition = float(current_time.strftime("%H.%M"))
    condition_time_1=float(current_time.strftime("%H.%M")) - 00.30 
    condition_time_2=float(current_time.strftime("%H.%M")) + 00.30 
    

    Db_Route=Stops_time.objects.all()
    for time in  Db_Route:
        timevalue=time.time1

        #if timevalue>formatted_time_condition:
    

        # Format the current time to display in AM/PM
    
           # current_format_time=float(formatted_time)

    time=[]
    for i in Db_Route:
        time.append(i)
    return render(request,'Route_load.html',{'time':time})
    


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

            if y.Route== Route_name:
                stops=y

        return render(request,'map_load.html',{'timevalue':timevalue, 'Db_Stops': Db_Stops,'stops':stops})