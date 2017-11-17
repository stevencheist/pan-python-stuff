#!/usr/bin/python
from apitesting import getroutes
object = getroutes()
print object
myo = str(object)
import untangle
obj = untangle.parse(myo)
print obj.entry.virtual_router.cdata

