# Dynamic Traffic Assignment Using Open Street Map and Simulation of Urban MObility</strong>

Generate Network Topology
=============================================================================
To generate the network topology of our point of interest area, we can use OSMWebWizard. Users can invoke the OSMWebWizard by clicking "%SUMO_HOME%\tools\osmWebWizard.py". Once the script is running, a web browser will open showing a map excerpt of central Berlin. Users can type any city name that you want.

![alt text](https://github.com/IoTcloudServe/Rama4-Model/tree/main/dynamic-traffic-assignment-kasemrat/2021-02-05-09-37-42/osmBangkok_1.PNG)

![alt text](https://github.com/IoTcloudServe/Rama4-Model/tree/main/dynamic-traffic-assignment-kasemrat/2021-02-05-09-37-42/osmBangkok_2.PNG)

The generated folder is with the name of "yyyy-mm-dd-hh-mm-ss". For more detail, you can go this link https://sumo.dlr.de/docs/Tutorials/OSMWebWizard.html.

Remove Edges
=============================================================================
Users can remove all edges which can not be used by passenger vehicles: 

netconvert --sumo-net-file osm.net.xml --lefthand --remove-edges.by-vclass hov,taxi,bus,delivery,transport,lightrail,cityrail,rail_slow,rail_fast,motorcycle,bicycle,pedestrian -o osm_netconvert.net.xml

Reduce Network
=============================================================================
Users can also reduce the network size with the following options:

--no-internal-links --keep-edges.by-vclass passenger --remove-edges.by-type highway.track,highway.services,highway.unsurfaced

 For more detail, you can go this link, https://sumo.dlr.de/docs/Networks/Import/OpenStreetMap.html#dismissing_unwanted_traffic_modes
  
Generate Routes in build.bat file
=============================================================================
python "%SUMO_HOME%\tools\randomTrips.py" -n osm_netconvert.net.xml --seed 42 --fringe-factor 300 -p 0.253626 -o osm.passenger.trips.xml -e 3600 --vehicle-class passenger --vclass passenger --prefix veh --min-distance 300 --trip-attributes "departLane=\"best\"" --fringe-start-attributes "departSpeed=\"max\"" --allow-fringe.min-length 1000 --lanes --validate

Here, input net file is osm_netconvert.net.xml that is converted by using netconvert. The option --fringe-factor is used to increase the probability that trips will start/end at the fringe (boundary) of the network. Output files are routes.rou.xml and routes.rou.alt.xml. For more detail, you can go this link, https://sumo.dlr.de/docs/Tools/Trip.html#randomtripspy and https://sumo.dlr.de/docs/Tools/Trip.html#edge_probabilities.

Remove Common Routes
=============================================================================
If users want to reduce some routes that are duplicated, users can use remove_commonRoutes.py. Input file is the generated route file from randomTrips.py.
Output file is removeCommonRoutes.rou.xml.

![alt text](https://github.com/IoTcloudServe/Rama4-Model/tree/main/dynamic-traffic-assignment-kasemrat/2021-02-05-09-37-42/removeRoutes_1.PNG)

![alt text](https://github.com/IoTcloudServe/Rama4-Model/tree/main/dynamic-traffic-assignment-kasemrat/2021-02-05-09-37-42/removeRoutes_2.PNG)

Sampling using routeSampler
=============================================================================
The routeSampler script can generate routes from turn-count data, edge-count and even origin-destination-count data. It requires a route file as input that defines possible routes.

python "%SUMO_HOME%\tools\routeSampler.py" -r removeCommonRoutes.rou.xml --turn-files turn3_modified_31122020.xml -o routesWithTurnRatioData.rou.xml. For more detail, you can go this link, https://sumo.dlr.de/docs/Tools/Turns.html#routesamplerpy

Setting in osm.sumoconfig
=============================================================================
User needs to change route file and net file in osm.sumoconfig file as shown in the following figure.

![alt text](https://github.com/IoTcloudServe/Rama4-Model/tree/main/dynamic-traffic-assignment-kasemrat/2021-02-05-09-37-42/setting_in_sumoconfig.PNG)

run.bat
=============================================================================
Now, user can run by clicking run.bat file.
