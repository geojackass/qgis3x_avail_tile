"""
This script should be run from the Python consol inside QGIS.

It adds online sources to the QGIS Browser.
Each source should contain a list with the folowing items (string type):
[sourcetype, title, authconfig, password, referer, url, username, zmax, zmin]

You can add or remove sources from the sources section of the code.

Script by Klas Karlsson
Sources from https://qms.nextgis.com/

Licence GPL-3
Copyright (c) 2018 Shoichi Otomo [@geojackass](https://twitter.com/geojackass)
"""


# Sources
sources = []
sources.append(["connections-xyz","Google Maps","","","","https://mt1.google.com/vt/lyrs=m&x=%7Bx%7D&y=%7By%7D&z=%7Bz%7D","","19","0"])
sources.append(["connections-xyz","Google Satellite", "", "", "", "https://mt1.google.com/vt/lyrs=s&x=%7Bx%7D&y=%7By%7D&z=%7Bz%7D", "", "19", "0"])
sources.append(["connections-xyz","Google Terrain", "", "", "", "https://mt1.google.com/vt/lyrs=t&x=%7Bx%7D&y=%7By%7D&z=%7Bz%7D", "", "19", "0"])
sources.append(["connections-xyz","Google Terrain Hybrid", "", "", "", "https://mt1.google.com/vt/lyrs=p&x=%7Bx%7D&y=%7By%7D&z=%7Bz%7D", "", "19", "0"])
sources.append(["connections-xyz","Google Satellite Hybrid", "", "", "", "https://mt1.google.com/vt/lyrs=y&x=%7Bx%7D&y=%7By%7D&z=%7Bz%7D", "", "19", "0"])
sources.append(["connections-xyz","Stamen Terrain", "", "", "Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL", "http://tile.stamen.com/terrain/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "20", "0"])
sources.append(["connections-xyz","Stamen Toner", "", "", "Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL", "http://tile.stamen.com/toner/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "20", "0"])
sources.append(["connections-xyz","Stamen Toner Light", "", "", "Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL", "http://tile.stamen.com/toner-lite/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "20", "0"])
sources.append(["connections-xyz","Stamen Watercolor", "", "", "Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL", "http://tile.stamen.com/watercolor/%7Bz%7D/%7Bx%7D/%7By%7D.jpg", "", "18", "0"])
sources.append(["connections-xyz","Wikimedia Map", "", "", "OpenStreetMap contributors, under ODbL", "https://maps.wikimedia.org/osm-intl/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "20", "1"])
sources.append(["connections-xyz","Wikimedia Hike Bike Map", "", "", "OpenStreetMap contributors, under ODbL", "http://tiles.wmflabs.org/hikebike/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "17", "1"])
sources.append(["connections-xyz","Esri Boundaries Places", "", "", "", "https://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "20", "0"])
sources.append(["connections-xyz","Esri Gray (dark)", "", "", "", "http://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "16", "0"])
sources.append(["connections-xyz","Esri Gray (light)", "", "", "", "http://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "16", "0"])
sources.append(["connections-xyz","Esri National Geographic", "", "", "", "http://services.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "12", "0"])
sources.append(["connections-xyz","Esri Ocean", "", "", "", "https://services.arcgisonline.com/ArcGIS/rest/services/Ocean/World_Ocean_Base/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "10", "0"])
sources.append(["connections-xyz","Esri Satellite", "", "", "", "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "17", "0"])
sources.append(["connections-xyz","Esri Standard", "", "", "", "https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "17", "0"])
sources.append(["connections-xyz","Esri Terrain", "", "", "", "https://server.arcgisonline.com/ArcGIS/rest/services/World_Terrain_Base/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "13", "0"])
sources.append(["connections-xyz","Esri Transportation", "", "", "", "https://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Transportation/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "20", "0"])
sources.append(["connections-xyz","Esri Topo World", "", "", "", "http://services.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "20", "0"])
sources.append(["connections-xyz","OpenStreetMap Standard", "", "", "OpenStreetMap contributors, CC-BY-SA", "http://tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "19", "0"])
sources.append(["connections-xyz","OpenStreetMap H.O.T.", "", "", "OpenStreetMap contributors, CC-BY-SA", "http://tile.openstreetmap.fr/hot/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "19", "0"])
sources.append(["connections-xyz","OpenStreetMap Monochrome", "", "", "OpenStreetMap contributors, CC-BY-SA", "http://tiles.wmflabs.org/bw-mapnik/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "19", "0"])
sources.append(["connections-xyz","Strava All", "", "", "OpenStreetMap contributors, CC-BY-SA", "https://heatmap-external-b.strava.com/tiles/all/bluered/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "15", "0"])
sources.append(["connections-xyz","Strava Run", "", "", "OpenStreetMap contributors, CC-BY-SA", "https://heatmap-external-b.strava.com/tiles/run/bluered/%7Bz%7D/%7Bx%7D/%7By%7D.png?v=19", "", "15", "0"])
sources.append(["connections-xyz","Open Weather Map Temperature", "", "", "Map tiles by OpenWeatherMap, under CC BY-SA 4.0", "http://tile.openweathermap.org/map/temp_new/%7Bz%7D/%7Bx%7D/%7By%7D.png?APPID=1c3e4ef8e25596946ee1f3846b53218a", "", "19", "0"])
sources.append(["connections-xyz","Open Weather Map Clouds", "", "", "Map tiles by OpenWeatherMap, under CC BY-SA 4.0", "http://tile.openweathermap.org/map/clouds_new/%7Bz%7D/%7Bx%7D/%7By%7D.png?APPID=ef3c5137f6c31db50c4c6f1ce4e7e9dd", "", "19", "0"])
sources.append(["connections-xyz","Open Weather Map Wind Speed", "", "", "Map tiles by OpenWeatherMap, under CC BY-SA 4.0", "http://tile.openweathermap.org/map/wind_new/%7Bz%7D/%7Bx%7D/%7By%7D.png?APPID=f9d0069aa69438d52276ae25c1ee9893", "", "19", "0"])
sources.append(["connections-xyz","CartoDb Dark Matter", "", "", "Map tiles by CartoDB, under CC BY 3.0. Data by OpenStreetMap, under ODbL.", "http://basemaps.cartocdn.com/dark_all/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "20", "0"])
sources.append(["connections-xyz","CartoDb Positron", "", "", "Map tiles by CartoDB, under CC BY 3.0. Data by OpenStreetMap, under ODbL.", "http://basemaps.cartocdn.com/light_all/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "20", "0"])
sources.append(["connections-xyz","Bing VirtualEarth", "", "", "", "http://ecn.t3.tiles.virtualearth.net/tiles/a{q}.jpeg?g=1", "", "19", "1"])
sources.append(["connections-xyz","MIERUNE_Color", "", "", "Maptiles by MIERUNE, under CC BY. Data by OpenStreetMap contributors, under ODbL.","https://tile.mierune.co.jp/mierune/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "15", "0"])
sources.append(["connections-xyz","MIERUNE_MONO", "", "", "Maptiles by MIERUNE, under CC BY. Data by OpenStreetMap contributors, under ODbL.","https://tile.mierune.co.jp/mierune_mono/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "15", "0"])
sources.append(["connections-xyz","OpenStreetMap", "", "", "OpenStreetMap contributors","http://tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "19", "0"])
sources.append(["connections-xyz","日本CS立体図（5mメッシュあり）", "", "", "国土地理院（承認番号　平29情使、第77号）","http://kouapp.main.jp/csmap/tile/japan/%7Bz%7D/%7Bx%7D/%7By%7D.jpg", "", "15", "5"])
sources.append(["connections-xyz","北海道CS立体図(10mメッシュのみ）", "", "", "国土地理院（承認番号　平28情使、第830号）","http://kouapp.main.jp/csmap/tile/hokkaido/%7Bz%7D/%7Bx%7D/%7By%7D.jpg", "", "15", "7"])
sources.append(["connections-xyz","九州沖縄CS立体図（10mメッシュのみ）", "", "", "国土地理院（承認番号　平28情使、第912号）","http://kouapp.main.jp/csmap/tile/kyuoki/%7Bz%7D/%7Bx%7D/%7By%7D.jpg", "", "15", "7"])
sources.append(["connections-xyz","地理院標準地図", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/std/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "18", "2"])
sources.append(["connections-xyz","地理院淡色地図", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/pale/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "18", "12"])
sources.append(["connections-xyz","地理院白地図", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/blank/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "14", "5"])
sources.append(["connections-xyz","地理院English", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/english/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "11", "5"])
sources.append(["connections-xyz","地理院色別標高図", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/relief/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "15", "5"])
sources.append(["connections-xyz","地理院写真", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/ort/%7Bz%7D/%7Bx%7D/%7By%7D.jpg", "", "18", "2"])
sources.append(["connections-xyz","国土画像情報（第一期：1974～1978年撮影）", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/gazo1/%7Bz%7D/%7Bx%7D/%7By%7D.jpg", "", "17", "10"])
sources.append(["connections-xyz","国土画像情報（第二期：1979～1983年撮影）", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/gazo2/%7Bz%7D/%7Bx%7D/%7By%7D.jpg", "", "17", "15"])
sources.append(["connections-xyz","国土画像情報（第三期：1984～1986年撮影）", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/gazo3/%7Bz%7D/%7Bx%7D/%7By%7D.jpg", "", "17", "15"])
sources.append(["connections-xyz","国土画像情報（第四期：1988～1990年撮影）", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/gazo4/%7Bz%7D/%7Bx%7D/%7By%7D.jpg", "", "17", "15"])
sources.append(["connections-xyz","空中写真（1961～1964年）", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/ort_old10/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "17", "15"])
sources.append(["connections-xyz","空中写真（1945～1950年）", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/ort_USA10/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "17", "15"])
sources.append(["connections-xyz","簡易空中写真（2004年～）", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/airphoto/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "18", "5"])
sources.append(["connections-xyz","数値地図5000（土地利用）", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/lum4bl_capital2005/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "17", "15"])
sources.append(["connections-xyz","土地利用図", "", "", "地理院タイル","http://cyberjapandata.gsi.go.jp/xyz/lum200k/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "17", "15"])

# Add sources to browser
for source in sources:
   connectionType = source[0]
   connectionName = source[1]
   QSettings().setValue("qgis/%s/%s/authcfg" % (connectionType, connectionName), source[2])
   QSettings().setValue("qgis/%s/%s/password" % (connectionType, connectionName), source[3])
   QSettings().setValue("qgis/%s/%s/referer" % (connectionType, connectionName), source[4])
   QSettings().setValue("qgis/%s/%s/url" % (connectionType, connectionName), source[5])
   QSettings().setValue("qgis/%s/%s/username" % (connectionType, connectionName), source[6])
   QSettings().setValue("qgis/%s/%s/zmax" % (connectionType, connectionName), source[7])
   QSettings().setValue("qgis/%s/%s/zmin" % (connectionType, connectionName), source[8])

# Update GUI
iface.reloadConnections()