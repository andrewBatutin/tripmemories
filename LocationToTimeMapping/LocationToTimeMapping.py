__author__ = 'andriy.batutin'
from os import path
from xml.dom.minidom import parse
import xml.dom.minidom

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
    time = collection.getElementsByTagName("when")
    coordA = []
    timeA = []
    for element in track:
        coordA.append(element.childNodes[0].data)
    for element in time:
        timeA.append(element.childNodes[0].data)
    res = []
    for i in range(0, len(coordA)):
        res.append((timeA[i], coordA[i]))
    return res
