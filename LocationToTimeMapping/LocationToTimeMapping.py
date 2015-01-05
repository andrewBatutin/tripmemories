import xml
from datetime import datetime
import xml.dom.minidom
import time
import numpy
import arrow
from scipy import interpolate

__author__ = 'andriy.batutin'


"""
1. build function from KML file. x -time, y - location
2. create interpolation alg to search by time the coordinate
3. get wiki description by coordinate
"""


def parseKMLFile():
    """
    >>> parseKMLFile()
    """
    DOMTree = xml.dom.minidom.parse("history-01-04-2015.kml")
    collection = DOMTree.documentElement
    track = collection.getElementsByTagName("gx:coord")
    timeDD = collection.getElementsByTagName("when")
    coordX = []
    coordY = []
    timeA = []
    for element in track:
        (x,y,z) = element.childNodes[0].data.split()
        (x,y,z) = (float(x), float(y), float(z))
        coordX.append(x)
        coordY.append(y)
    for element in timeDD:
        dateTimeStamp = arrow.get(element.childNodes[0].data)
        timeA.append(dateTimeStamp.float_timestamp)

    return (timeA, coordX, coordY)

def interpPosition(x,y,z, timeToSearch):
    """
    >>> (x,y,z) = parseKMLFile()
    >>> interpPosition(x,y,z, 1420457111.000012)
    """
    f = interpolate.interp2d(x, y, z, kind='linear')
    print f