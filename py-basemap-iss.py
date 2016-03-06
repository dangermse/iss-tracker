""" plot the ISS and update every 60 seconds"""
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from datetime import datetime
import time
import urllib2
import json

def getiss():
    """ call where the iss at api thanks to Bill Shupp"""
    response = urllib2.urlopen('https://api.wheretheiss.at/v1/satellites/25544')
    mydata = response.read()
    return mydata


while True:
    iss = getiss()
    pos = json.loads(iss)
    lat = pos['latitude']
    lon = pos['longitude']

    # miller projection
    map = Basemap(projection='mill',lon_0=0)
    # plot coastlines, draw label meridians and parallels.
    map.drawcoastlines()
    map.drawparallels(np.arange(-90,90,30),labels=[1,0,0,0])
    map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,60),labels=[0,0,0,1])
    # fill continents 'coral' (with zorder=0), color wet areas 'aqua'
    map.drawmapboundary(fill_color='aqua')
    map.fillcontinents(color='coral',lake_color='aqua')
    # shade the night areas, with alpha transparency so the
    # map shows through. Use current time in UTC.
    date = datetime.now()
    CS=map.nightshade(date)
    plt.title('ISS Location For for %s Lat: %.2f Long: %.2f' % (date.strftime("%d %b %Y %H:%M:%S"),lat,lon))

    x,y = map(lon, lat)
    map.plot(x, y, 'bo', markersize=12)  # plot the station on the map
    plt.ion()
    plt.draw()
    plt.show(block=False)
    try:
        time.sleep(60) # --only update once per minute - dont be greedy with api
    except KeyboardInterrupt:
        plt.close()  # clean up when the command line gets ctrl + c
        exit()

    plt.clf()
