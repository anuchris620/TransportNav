from django.shortcuts import render

# Create your views here.
from datetime import datetime, time
from busnavigation.models import Stops_time,CET_PATTOM_EASTFORT,Stops
import folium,json,os
from django.views import View
import asyncio

import winsdk.windows.devices.geolocation as wdg 
#import winsdk.windows.devices.geolocation as wdg



def index(request):
    return render(request,'index.html')
     
def Route_Load(request):
    Departure = request.GET.get('start')
    Destination = request.GET.get('destination')
    Route1=["CET","Sreekaryam","Ulloor","Medical college","Kumarapuram","Kannamoola","General Hospital","Palayam","Statue","East fort"]    
    Route2=["CET","Sreekaryam","Ulloor","Medical college","Pottakuzhi","Pattom","PMG","Palayam","Statue","East fort"]
    Route3=["CET","Sreekaryam","Ulloor","Kesavadasapuram","Pattom","PMG","Palayam","Statue","East fort"]
    Db_Route=Stops_time.objects.all()
    current_time = datetime.now()
    formatted_time_check = current_time.strftime("%I:%M %p")
    t1 = datetime.strptime(formatted_time_check, '%I:%M %p')
    #Sel_Route=[]

    if not Departure or not Destination:
        msg = "Departure and Destination are required."
        return render(request, 'index.html', {'msg': msg})

    if Departure in Route1 and Destination in Route1:
        if Departure in Route2 and Destination in Route2:
            if Departure in Route3 and Destination in Route3:
                start_position= Route1.index(Departure)
                end_position=Route1.index(Destination)
                if start_position < end_position: 
                    Route_sel=["CET KANNAMOOLA EASTFORT","CET MEDICALCOLLEGE EASTFORT","CET PATTOM EASTFORT"]
                        
                else:    
                    Route_sel=["EASTFORT KANNAMOOLA CET","EASTFORT MEDICALCOLLEGE CET","EASTFORT PATTOM CET"]
        
                time=[]
                Route=[]
                for Route_name in Db_Route:
                    if Route_name.Routes in Route_sel:
                        time2=Route_name.time1
                        t2 = datetime.strptime(time2, '%I:%M %p')
                        diff=t2-t1
                        hours, remainder = divmod(diff.seconds, 3600)
                        minutes, _ = divmod(remainder, 60)
                    
                        if float(str(hours)+"."+str(minutes))<=0.59:
                            #print( float(str(hours)+"."+str(minutes)))
                            time.append(Route_name)
                       
                        else:
                            Route.append(Route_name)
                        #Sel_Route.append(Route_name)
                if time:   
                    return render(request,'Route_load.html',{'time':time,'Route':Route})
                else:
                    msg="Currently busses are not available,you can check for available buses"
                    return render(request,'Route_load.html',{'time':time,'Route':Route,'msg':msg})


    if Departure in Route1 and Destination in Route1:
        if Departure in Route2 and Destination in Route2:
                start_position= Route1.index(Departure)
                end_position=Route1.index(Destination)
                if start_position < end_position: 
                    Route_sel=["CET KANNAMOOLA EASTFORT","CET MEDICALCOLLEGE EASTFORT"]
                        
                else:    
                    Route_sel=["EASTFORT KANNAMOOLA CET","EASTFORT MEDICALCOLLEGE CET"]
        
                time=[]
                Route=[]
                for Route_name in Db_Route:
                    if Route_name.Routes in Route_sel:
                        time2=Route_name.time1
                        t2 = datetime.strptime(time2, '%I:%M %p')
                        diff=t2-t1
                        hours, remainder = divmod(diff.seconds, 3600)
                        minutes, _ = divmod(remainder, 60)
                    
                        if float(str(hours)+"."+str(minutes))<=0.59:
                            #print( float(str(hours)+"."+str(minutes)))
                            time.append(Route_name)
                         
                        else:
                            Route.append(Route_name)
                        #Sel_Route.append(Route_name)
                if time:   
                    return render(request,'Route_load.html',{'time':time,'Route':Route})
                else:
                    msg="Currently busses are not available,you can check for available buses"
                    return render(request,'Route_load.html',{'time':time,'Route':Route,'msg':msg})


  
    if Departure in Route2 and Destination in Route2:
        if Departure in Route3 and Destination in Route3:
            start_position= Route3.index(Departure)
            end_position=Route3.index(Destination)
            if start_position < end_position: 
                Route_sel=["CET MEDICALCOLLEGE EASTFORT","CET PATTOM EASTFORT"]
                        
            else:    
                Route_sel=["EASTFORT MEDICALCOLLEGE CET","EASTFORT PATTOM CET"]
        
            time=[]
            Route=[]
            for Route_name in Db_Route:
                if Route_name.Routes in Route_sel:
                    time2=Route_name.time1
                    t2 = datetime.strptime(time2, '%I:%M %p')
                    diff=t2-t1
                    hours, remainder = divmod(diff.seconds, 3600)
                    minutes, _ = divmod(remainder, 60)
                    
                    if float(str(hours)+"."+str(minutes))<=0.59: 
                        time.append(Route_name)
                  
                    else:
                        Route.append(Route_name)
                        #Sel_Route.append(Route_name)
            if time:   
                return render(request,'Route_load.html',{'time':time,'Route':Route})
            else:
                msg="Currently busses are not available,you can check for available buses"
                return render(request,'Route_load.html',{'time':time,'Route':Route,'msg':msg})

    
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
                hours, remainder = divmod(diff.seconds, 3600)
                minutes, _ = divmod(remainder, 60)
            
                if float(str(hours)+"."+str(minutes))<=0.59:
                    time.append(Route_name)
                else:
                    Route.append(Route_name)
                #Sel_Route.append(Route_name)
    
        if time:   
            return render(request,'Route_load.html',{'time':time,'Route':Route})
        else:
            msg="Currently busses are not available,you can check for available buses"
            return render(request,'Route_load.html',{'time':time,'Route':Route,'msg':msg})


    if Departure in Route2 and Destination in Route2:
        start_position= Route2.index(Departure)
        end_position=Route2.index(Destination)
        if start_position < end_position: 
            Route_sel=["CET MEDICALCOLLEGE EASTFORT"]
                        
        else:    
            Route_sel=["EASTFORT MEDICALCOLLEGE CET"]
        
        time=[]
        Route=[]
        for Route_name in Db_Route:
            if Route_name.Routes in Route_sel:
                time2=Route_name.time1
                t2 = datetime.strptime(time2, '%I:%M %p')
                diff=t2-t1
                hours, remainder = divmod(diff.seconds, 3600)
                minutes, _ = divmod(remainder, 60)
            
                if float(str(hours)+"."+str(minutes))<=0.59:
                    time.append(Route_name)
              
                else:
                    Route.append(Route_name)
                #Sel_Route.append(Route_name)


        if time:   
            return render(request,'Route_load.html',{'time':time,'Route':Route})
        else:
            msg="Currently busses are not available,you can check for available buses"
            return render(request,'Route_load.html',{'time':time,'Route':Route,'msg':msg})


    if Departure in Route3 and Destination in Route3:
        start_position= Route3.index(Departure)
        end_position=Route3.index(Destination)
        if start_position < end_position: 
            Route_sel=["CET PATTOM EASTFORT"]
                        
        else:    
            Route_sel=["EASTFORT PATTOM CET"]
        
        time=[]
        Route=[]
        for Route_name in Db_Route:
            if Route_name.Routes in Route_sel:
                time2=Route_name.time1
                t2 = datetime.strptime(time2, '%I:%M %p')
                diff=t2-t1
             
                hours, remainder = divmod(diff.seconds, 3600)
                minutes, _ = divmod(remainder, 60)
            
                if float(str(hours)+"."+str(minutes))<=0.59:
                  

                
                    time.append(Route_name)
                 
                else:
                    Route.append(Route_name)
                #Sel_Route.append(Route_name)

        if time:   
            return render(request,'Route_load.html',{'time':time,'Route':Route})
        else:
            msg="Currently busses are not available,you can check for available buses"
            return render(request,'Route_load.html',{'time':time,'Route':Route,'msg':msg})
    else:
        msg="Try Typing Genuine Route"
        return render(request,'index.html',{'msg':msg})

    
def Map_Load(request):
    if request.method=="GET":
        Route_name=request.GET['routes']
        Start_time=request.GET['departure_times']
        Db_Route=Stops_time.objects.all()
        Db_Stops=Stops.objects.all()
        print(Route_name)
                
        for i in Db_Route:
                   
            if i.Routes==Route_name:
                if i.time1==Start_time:
                    timevalue=i
               

                        #time_start.append(i.time1)
                        #time_end.append(i.time10)
        for y in Db_Stops:

            if y.Route==Route_name:
                stops=y

    #data=FACILITIES.objects.get(BlockName=name)
    shp_dir = os.path.join(os.getcwd(), 'static', 'shp', Route_name)
    m = folium.Map(location=[8.531355038, 76.92165681], zoom_start=13)
    
        
    async def getCoords():
        locator = wdg.Geolocator()
        pos = await locator.get_geoposition_async()
        return [pos.coordinate.latitude, pos.coordinate.longitude]

# Wrapper function to run the async function and handle errors
    def getLoc():
        try:
            return asyncio.run(getCoords())
        except PermissionError:
            print("ERROR: You need to allow applications to access your location in Windows settings")

# Get the current location
    current_location = getLoc()

# Add current location to the map
    if current_location:
        folium.Marker(
            location=current_location,
            popup=folium.Popup("<b>Current Location</b>", max_width=300),
            icon=folium.Icon(color='red', icon='info-sign',)
        ).add_to(m)
    custom_icon_path = os.path.join(os.getcwd(),'static','pic', 'bus-stop.png')
    # Define a style for your GeoJSON features
    style_basin = {'fillColor': 'transparent', 'color': '#003d99'}
    
    # Specify the stop and time for comparison
   
    given_time = Start_time
    print(given_time)
    # Iterate over each file in the jsonfiles folder
    for filename in os.listdir(shp_dir):
        if filename.endswith('.geojson'):
            geojson_file_path = os.path.join(shp_dir, filename)
            with open(geojson_file_path, 'r') as f:
                data = f.read()
                geojson_data = folium.GeoJson(data)
                
                # Check if the first feature in the GeoJSON file matches the given stop and time
                first_feature_properties = geojson_data.data['features'][0]['properties']
                if first_feature_properties.get('TIME') == given_time:
                    for feature in geojson_data.data['features']:
                        properties = feature['properties']
                        popup_content = "<h4>{}</h4>".format(properties['BUS STOP'])  # Adjust this according to your GeoJSON properties
                        for key, value in properties.items():
                            popup_content += "<b>{}</b>: {}<br>".format(key, value)
                        # Create a custom icon with no default popup
                        custom_icon = folium.Icon(color='blue', icon='info-sign')
                        folium.Marker(
                            location=[feature['geometry']['coordinates'][1], feature['geometry']['coordinates'][0]],
                            popup=folium.Popup(popup_content, max_width=300),
                            icon=custom_icon
                        ).add_to(m)
                    break  # Stop searching after finding the matching file
        
    shp_route=os.path.join(os.getcwd(), 'static', 'shp')
    # Load the GeoJSON file representing a road without pop-ups
    if Route_name=="EASTFORT PATTOM CET" or Route_name=="CET PATTOM EASTFORT":
        geojson_file_with_road_popup = os.path.join(shp_route, 'EASTFORT PATTOM CET ROAD.geojson')
    elif Route_name=="EASTFORT KANNANMOOLA CET" or Route_name=="CET KANNAMOOLA EASTFORT":
        geojson_file_with_road_popup = os.path.join(shp_route, 'EASTFORT KANNANMOOLA CET ROAD.geojson')
    else:
        geojson_file_with_road_popup = os.path.join(shp_route, 'EASTFORT MEDICALCOLLEGE CET ROAD.geojson')



    # Add GeoJSON features representing road with a popup for the road name
    with open(geojson_file_with_road_popup, 'r') as f:
        data = f.read()
        geojson_with_road_popup = folium.GeoJson(data)
        
        # Extract road name
        road_name = geojson_with_road_popup.data['features'][0]['properties']['ROUTE']
        
        # Add road GeoJSON to the map with a popup for road name
        folium.GeoJson(
            data,
            name='Road',
            style_function=lambda x: {'color': '#FF5733'},
            tooltip=road_name  # Display road name as tooltip
        ).add_to(m)
        
    folium.LayerControl().add_to(m)
    
    # Export the map to HTML
    m_html = m._repr_html_()
    
    context = {'my_map': m_html}
    
    # Render the map using a template
    return render(request,'map_load2.html',{'timevalue':timevalue, 'Db_Stops': Db_Stops,'stops':stops,'context':context,'Route_name':Route_name})
    icon=folium.CustomIcon(custom_icon_path, icon_size=(20, 40))





    
    """shp_dir = os.path.join(os.getcwd(), 'static', 'shp')
    m = folium.Map(location=[8.545355038, 76.90665681], zoom_start=13)

    custom_location = [8.546, 76.908]

# Create a marker at the custom location
    marker = folium.Marker(
    location=custom_location,
    popup="Custom Location Popup",  # Popup content
    icon=folium.Icon(color='red')   # Customize marker icon if needed
        )

# Add the marker to the map
    marker.add_to(m)
    # Function to generate popup content

    def popup_content(properties):
        popup_html = '<table>'
        for key,value in properties.items():
            popup_html += f'<tr><td>{key} : {value}</td></tr>'
        popup_html += '</table>'
            #popup_html += f"<img src='{properties['img']}' alt='Image' width='200'>"
        return popup_html

    # Adding GeoJSON layer
    
    geojson_files = ['CET-KANNAMOOLA-EASTFORT(1.15PM-1.57PM).geojson']
    geojson_file=os.path.join(shp_dir,'CET-KANNAMOOLA-EASTFORT(1.15PM-1.57PM).geojson')
    with open(geojson_file, 'r') as f:
        data = f.read()
        geojson = folium.GeoJson(data)
        m.add_child(geojson)
        
    folium.LayerControl().add_to(m)
        
    for geojson_file in geojson_files:
        geojson_path =os.path.join(shp_dir, geojson_file)
        geojson_layer = folium.GeoJson(
            geojson_path,
            name='CET-KANNAMOOLA-EASTFORT',
            style_function=lambda x: {'fillColor': 'blue', 'color': '#003d99'}
        ).add_to(m)

        # Adding popup to each feature
        #with open(geojson_path) as f:
        with open(os.path.join(shp_dir, geojson_file)) as f:
            geojson_data = json.load(f)
            for feature in geojson_data['features']:
                feature_properties = feature['properties']
                popup_html = popup_content(feature_properties)
                folium.Popup(popup_html, max_width=300).add_to(geojson_layer)

            folium.LayerControl().add_to(m)

    
    # Exporting the map as HTML
    m= m._repr_html_()
    context = {'my_map': m}
    
    return render(request,'map_load2.html',{'timevalue':timevalue, 'Db_Stops': Db_Stops,'stops':stops,'context':context})"""


def home(request):
    
    shp_dir = os.path.join(os.getcwd(), 'static', 'shp')
    m = folium.Map(location=[8.545355038, 76.90665681], zoom_start=7)
    
    # Define a style for your GeoJSON features
    style_basin = {'fillColor': 'transparent', 'color': '#003d99'}
    
    # Load the GeoJSON file
    geojson_file = os.path.join(shp_dir, 'CET-KANNAMOOLA-EASTFORT(1.15PM-1.57PM).geojson')
    
    # Add GeoJSON features to the map
    with open(geojson_file, 'r') as f:
        data = f.read()
        geojson = folium.GeoJson(data)
        m.add_child(geojson)
        
    folium.LayerControl().add_to(m)
    
    # Export the map to HTML
    m_html = m._repr_html_()
    
    context = {'my_map': m_html}
    
    # Render the map using a template

    ## rendering
    return render(request,'map_load2.html',{'context':context})





"""class RouteLoadView(View):
    def get(self, request):
        Departure = request.GET.get('start')
        Destination = request.GET.get('destination')
        
        if not Departure or not Destination:
            msg = "Departure and Destination are required."
            return render(request, 'index.html', {'msg': msg})

        Route1 = ["CET", "Sreekaryam", "Ulloor", "Medical college", "Kumarapuram", "Kannamoola", "General Hospital", "Palayam", "Statue", "East fort"]
        Route2 = ["CET", "Sreekaryam", "Ulloor", "Medical college", "Pottakuzhi", "Pattom", "PMG", "Palayam", "Statue", "East fort"]
        Route3 = ["CET", "Sreekaryam", "Ulloor", "Kesavadasapuram", "Pattom", "PMG", "Palayam", "Statue", "East fort"]
        Db_Route = Stops_time.objects.all()
        current_time = datetime.now()
        formatted_time_check = current_time.strftime("%I:%M %p")
        t1 = datetime.strptime(formatted_time_check, '%I:%M %p')

        Route_sel, time, Route = self.find_routes(Departure, Destination, Route1, Route2, Route3, Db_Route, t1)

        if time:
            return render(request, 'Route_load.html', {'time': time, 'Route': Route})
        else:
            msg = "Currently buses are not available, you can check for available buses"
            return render(request, 'Route_load.html', {'time': time, 'Route': Route, 'msg': msg})

    def find_routes(self, Departure, Destination, Route1, Route2, Route3, Db_Route, t1):
        Route_sel = []
        time = []
        Route = []

        if Departure in Route1 and Destination in Route1:
            if Departure in Route2 and Destination in Route2:
                if Departure in Route3 and Destination in Route3:
                    Route_sel = self.get_route_selection(Departure, Destination, Route1, Route2, Route3)
                    time, Route = self.get_time_and_routes(Route_sel, Db_Route, t1)

                else:
                    Route_sel = self.get_route_selection(Departure, Destination, Route1, Route2)
                    time, Route = self.get_time_and_routes(Route_sel, Db_Route, t1)

            elif Departure in Route2 and Destination in Route2:
                Route_sel = self.get_route_selection(Departure, Destination, Route1, Route2)
                time, Route = self.get_time_and_routes(Route_sel, Db_Route, t1)

            else:
                Route_sel = self.get_route_selection(Departure, Destination, Route1)
                time, Route = self.get_time_and_routes(Route_sel, Db_Route, t1)

        elif Departure in Route2 and Destination in Route2:
            if Departure in Route3 and Destination in Route3:
                Route_sel = self.get_route_selection(Departure, Destination, Route2, Route3)
                time, Route = self.get_time_and_routes(Route_sel, Db_Route, t1)
            else:
                Route_sel = self.get_route_selection(Departure, Destination, Route2)
                time, Route = self.get_time_and_routes(Route_sel, Db_Route, t1)

        elif Departure in Route3 and Destination in Route3:
            Route_sel = self.get_route_selection(Departure, Destination, Route3)
            time, Route = self.get_time_and_routes(Route_sel, Db_Route, t1)

        return Route_sel, time, Route

    def get_route_selection(self, Departure, Destination, *routes):
        Route_sel = []
        for route in routes:
            if Departure in route and Destination in route:
                start_position = route.index(Departure)
                end_position = route.index(Destination)
                if start_position < end_position:
                    Route_sel.append(f"CET {route[-3]} EASTFORT")
                else:
                    Route_sel.append(f"EASTFORT {route[-3]} CET")
        return Route_sel

    def get_time_and_routes(self, Route_sel, Db_Route, t1):
        time = []
        Route = []
        for Route_name in Db_Route:
            if Route_name.Routes in Route_sel:
                time2 = Route_name.time1
                t2 = datetime.strptime(time2, '%I:%M %p')
                diff = t2 - t1
                hours, remainder = divmod(diff.seconds, 3600)
                minutes, _ = divmod(remainder, 60)

                if float(f"{hours}.{minutes}") <= 0.59:
                    time.append(Route_name)
                else:
                    Route.append(Route_name)
        return time, Route"""