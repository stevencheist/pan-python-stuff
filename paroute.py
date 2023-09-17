#!/usr/bin/python
from apitesting import getroutes
object = getroutes()
print(object)
#myo = str(object)
import untangle
obj = untangle.parse(object)
print(obj.entry.virtual_router)

