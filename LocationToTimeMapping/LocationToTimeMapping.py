import xml
from datetime import datetime
import xml.dom.minidom
import time
import arrow
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
    coordA = []
    timeA = []
    for element in track:
        coordA.append(element.childNodes[0].data)
    for element in timeDD:
        dateTimeStamp = arrow.get(element.childNodes[0].data)
        timeA.append(dateTimeStamp.float_timestamp)

    return (timeA, coordA)

