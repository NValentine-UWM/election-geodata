#!/usr/bin/env python
import mapnik, sys, os

conus_path, alaska_path, hawaii_path, render_path = map(os.path.abspath, sys.argv[1:])
os.chdir(os.path.dirname(__file__))

map1 = mapnik.Map(1780, 1250)
mapnik.load_map(map1, 'style.xml')
bbox=(mapnik.Box2d(-2700000, -2800000, 2570000, 770000))
map1.zoom_to_box(bbox)
mapnik.render_to_file(map1, conus_path)

map2 = mapnik.Map(580, 480)
mapnik.load_map(map2, 'style.xml')
# switch to http://spatialreference.org/ref/epsg/3338/
map2.srs = '+proj=aea +lat_1=55 +lat_2=65 +lat_0=50 +lon_0=-154 +x_0=0 +y_0=0 +ellps=GRS80 +datum=NAD83 +units=m +no_defs'
bbox=(mapnik.Box2d(-1250000, 380000, 1550000, 2400000))
map2.zoom_to_box(bbox)
mapnik.render_to_file(map2, alaska_path)

map3 = mapnik.Map(360, 290)
mapnik.load_map(map3, 'style.xml')
# switch to http://spatialreference.org/ref/epsg/2783/
map3.srs = '+proj=tmerc +lat_0=20.33333333333333 +lon_0=-156.6666666666667 +k=0.999966667 +x_0=500000 +y_0=0 +ellps=GRS80 +units=m +no_defs'
bbox=(mapnik.Box2d(40000, -170000, 700000, 220000))
map3.zoom_to_box(bbox)
mapnik.render_to_file(map3, hawaii_path)
