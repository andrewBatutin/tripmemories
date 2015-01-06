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
- 2 hours to convert to to unix time
"""

def playground():
    """
    >>> playground()
    """
    (time, x, y) = parseKMLFile()
    refTime = 1419509129.0
    point = interpPosition(time, x, y, refTime)
    print point

def parseKMLFile():
    """
    >>> parseKMLFile()
    """
    DOMTree = xml.dom.minidom.parse("history-12-24-2014.kml")
    collection = DOMTree.documentElement
    track = collection.getElementsByTagName("gx:coord")
    timeDD = collection.getElementsByTagName("when")
    coordX = []
    coordY = []
    timeA = []
    for element in track:
        (x, y, z) = element.childNodes[0].data.split()
        (x, y, z) = (float(x), float(y), float(z))
        coordX.append(x)
        coordY.append(y)
    for element in timeDD:
        dateTimeStamp = arrow.get(element.childNodes[0].data)
        timeA.append(dateTimeStamp.float_timestamp)

    return (timeA, coordX, coordY)


def findTimeSpaceIndexs(a, timeToSearch):
    """
    >>> findTimeSpaceIndexs([1,2,3], 3.6)
    (2, 2)
    >>> findTimeSpaceIndexs([1,2,3], 2.6)
    (1, 2)
    >>> findTimeSpaceIndexs([1,2,3], 0.6)
    (0, 0)
    """
    (i, v) = min(enumerate(a), key=lambda x: abs(x[1] - timeToSearch))
    if v > timeToSearch:
        if i > 0:
            return (i - 1, i)
        else:
            return (i, i)
    else:
        if i < len(a) -1:
            return (i, i+1)
        else:
            return (i,i)


def interpPosition(x, y, z, timeToSearch):
    """
    >>> interpPosition([1,2,3], [10,20,30], [100,200,300], 2.5)
    x 25.0 y 250.0
    """
    (i1, i2) = findTimeSpaceIndexs(x, timeToSearch)
    a = Point(y[i1], z[i1])
    b = Point(y[i2], z[i2])
    l = Line(a, b)
    res = l.midpoint()
    return res


class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x " + str(self.x) + " y " + str(self.y)

    def __repr__(self):
        return "x " + str(self.x) + " y " + str(self.y)

class Line:
    a = Point(0, 0)
    b = Point(0, 0)

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def midpoint(self):
        resX = (self.a.x + self.b.x) * 0.5
        resY = (self.a.y + self.b.y) * 0.5
        return Point(resX, resY)