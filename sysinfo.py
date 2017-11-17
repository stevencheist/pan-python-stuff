#!/usr/bin/python
from apitesting import getsysinfo
object = getsysinfo()
myo = str(object)
import untangle
obj = untangle.parse(myo)
hostname = obj.system.hostname.cdata
ip = obj.system.ip_address.cdata
netmask = obj.system.netmask.cdata
uptime = obj.system.uptime.cdata
mac = obj.system.mac_address.cdata
tm = obj.system.time.cdata
devicename = obj.system.devicename.cdata
swver = obj.system.sw_version.cdata
model = obj.system.model.cdata
sn = obj.system.serial.cdata
appver = obj.system.app_version.cdata
apprel = obj.system.app_release_date.cdata
avver = obj.system.av_version.cdata
avrel = obj.system.av_release_date.cdata
tver = obj.system.threat_version.cdata
trel = obj.system.threat_release_date.cdata
wfpver = obj.system.wf_private_version.cdata
wfprel = obj.system.wf_private_release_date.cdata
wfver = obj.system.wildfire_version.cdata
wfrel = obj.system.wildfire_release_date.cdata
urlver = obj.system.url_filtering_version.cdata
logdbver = obj.system.logdb_version.cdata

print "Host Name | Uptime | SW Version | App Version | AV Version | Threat Version | Wildfire Version | URL Version | Logdb Version"
print hostname + " | " + uptime + " | " + swver + " | " + appver + " | " + avver + " | " + tver + " | " + wfver + " | " + urlver + " | " + logdbver
