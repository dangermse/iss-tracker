""" get capital of country and map it on
    a raspberry pi with python basemap - save the image and tweet
"""

__author__ = '@damianmooney'

import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from datetime import datetime
import time
import urllib2
import json
import random


def do_import_cities(fname):
    """grab our list of cities and locations"""
    citylist = []
    f = open(fname, 'r')
    while True:
        buff = f.readline()
        if buff == '':
            break
        # our file should be comma delimited country,city,lat,long
        citylist.append(buff.strip().split(','))
    f.close()
    return citylist


cities = do_import_cities('capitals.txt')
# print cities
while True:
    for i in cities:
        print i
        country = i[0]
        capital = i[1]
        lat = float(i[2])
        lon = float(i[3])


        map = Basemap(projection='ortho',lon_0=lon,lat_0=lat)
        map.drawmapboundary(fill_color='aqua')
        map.fillcontinents(color='coral',lake_color='aqua')
        map.drawcoastlines()
        map.drawcountries()
        map.drawparallels(np.arange(-90,90,30),labels=[1,0,0,0])
        map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,60),labels=[0,0,0,1])

 
        date = datetime.now()
        plt.title('The Capital of %s is %s\nLat: %.2f Long: %.2f' % (country,capital,lat,lon),color='white')

        x,y = map(lon, lat)
        map.plot(x, y, 'ro', markersize=12)  # plot the city on the map
        
        plt.ion()
        plt.draw()
        plt.show(block=False)
        time.sleep(100)
        

        try:
          
            plt.savefig('/home/pi/iss/iss-tracker/city.jpg',facecolor='black',edgecolor='black')  # location of image to tweet
            # time.sleep(200)
            f = open('/home/pi/iss/iss-tracker/answer.txt', 'w')
            f.write('%s is the capital of %s @ %d %d \n' % (capital, country, lat, lon))
            f.close()
            time.sleep(200)
        except KeyboardInterrupt:
            plt.close()  # clean up when the command line gets ctrl + c
            exit()

        plt.clf()
