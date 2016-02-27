""" Get current ISS position from http://wheretheiss.at/ and map it on
    a raspberry pi with minecraft
"""
__author__ = '@damianmooney'
from mcpi import minecraft as minecraft
from mcpi import block as block
from datetime import datetime
import time
import urllib2
import json


def getiss():
    """ call where the iss at api thanks to Bill Shupp"""
    response = urllib2.urlopen('https://api.wheretheiss.at/v1/satellites/25544')
    mydata = response.read()
    return mydata


def do_coord(longitude):
    """ longitude: convert our longitude to a minecraft co-ordinate"""
    mine_long = longitude * -.55
    return mine_long


if __name__ == "__main__":
    mc = minecraft.Minecraft.create()
    mc.postToChat("   Minecraft ISS Tracker for @naascoderdojo")
    mc.camera.setFollow()
    mc.player.setting("autojump", False)
    mc.player.setPos(6, 20, 50)
    while True:
        iss = getiss()
        pos = json.loads(iss)
        lat = pos['latitude']
        lon = pos['longitude']

        mc.postToChat('   ISS Location Lat: %.2f Long: %.2f' % (lat,lon))
        new_long = do_coord(lon)
        mc.player.setPos(int(new_long),  20, int(lat))
        print('lon %d lat %d' % (new_long, lat))
        time.sleep(60)  # -- update once per minute - don't be greedy with api