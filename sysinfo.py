#!/usr/bin/python
from apitesting import getsysinfo
object = getsysinfo()
myo = str(object)
#print(myo)
import untangle
obj = untangle.parse(myo)
#print(str(obj.system.hostname))
if obj.system.hostname in obj.system.get_elements():
    hostname = obj.system.hostname.cdata
    #print(hostname)
else:
    hostname = "Hostname not present in configuration"
if obj.system.ip_address.cdata in obj.system.get_elements():
    ip = obj.system.ip_address.cdata
else:
    ip = "IP address not present in configuration"
if obj.system.public_ip_address.cdata in obj.system.get_elements():
    pubip = obj.system.public_ip_address.cdata
else:
    pubip = "public IP address not present in data"
if obj.system.netmask.cdata in obj.system.get_elements():
    netmask = obj.system.netmask.cdata
else: 
    netmask = "Subnet mask not present in configuration"
if obj.system.default_gateway.cdata in obj.system.get_elements():
    dgw = obj.system.default_gateway.cdata
else:
    dgw = "default gateway not present in configuration"
if obj.system.is_dhcp.cdata in obj.system.get_elements():
    isdhcp = obj.system.is_dhcp.cdata
else:
    isdhcp = "DHCP Setting not present in data"
if obj.system.ipv6_address.cdata in obj.system.get_elements():
    ipv6a = obj.system.ipv6_address.cdata
else:
    ipv6a = "IPv6 Address not present in config"
if obj.system.ipv6_link_local_address.cdata in obj.system.get_elements():
    ipv6ll = obj.system.ipv6_link_local_address.cdata
else:
    ipv6ll = "IPv6 Local Link address not present in config"
if obj.system.uptime.cdata in obj.system.get_elements():
    uptime = obj.system.uptime.cdata
else:
    uptime = "System uptime not present in data"
if obj.system.mac_address.cdata in obj.system.get_elements():
    mac = obj.system.mac_address.cdata
else:
    mac = "mac address not present in data"
if obj.system.time.cdata in obj.system.get_elements():
    tm = obj.system.time.cdata
else:
    tm = "system time not present in data"
if obj.system.devicename.cdata in obj.system.get_elements():
    devicename = obj.system.devicename.cdata
else:
    devicename = "Device name not present in configuration"
if obj.system.sw_version.cdata in obj.system.get_elements():
    swver = obj.system.sw_version.cdata
else:
    swver = "Software version not present in data"
if obj.system.model.cdata in obj.system.get_elements():
    model = obj.system.model.cdata
else:
    model = "Platform Model not present in data"
if obj.system.serial.cdata in obj.system.get_elements():
    sn = obj.system.serial.cdata
else:
    sn = "Serial Number not present in data"
if obj.system.family.cdata in obj.system.get_elements():
    family = obj.system.family.cdata
else:
    family = "Platform family not in data"
if obj.system.app_version.cdata in obj.system.get_elements():
    appver = obj.system.app_version.cdata
else:
    appver = "App-ID version not present in data"
if obj.system.app_release_date.cdata in obj.system.get_elements():
    apprel = obj.system.app_release_date.cdata
else:
    apprel = "App-ID release date not present in data"
if obj.system.cloud_mode.cdata in obj.system.get_elements():
    cloudmode = obj.system.cloud_mode.cdata
else:
    cloudmode = "Cloud Mode not present in data"
if obj.system.global_protect_client_package_version.cdata in obj.system.get_elements():
    gppkgver = obj.system.global_protect_client_package_version.cdata
else:
    gppkgver = "gp client package version not present in data"
if obj.system.device_dictionary_version.cdata in obj.system.get_elements():
    devdictver = obj.system.device_dictionary_version.cdata
else:
    devdictver = "device dictionary version not present in data"
if obj.system.device_dictionary_release_date.cdata in obj.system.get_elements():
    devdictreldt = obj.system.device_dictionary_release_date.cdata
else:
    devdictreldt = "device dictionary release date not present in data"
if obj.system.av_version.cdata in obj.system.get_elements():
    avver = obj.system.av_version.cdata
else: 
    avver = "Antivirus version not present in data"
if obj.system.av_release_date.cdata in obj.system.get_elements():
    avrel = obj.system.av_release_date.cdata
else:
    avrel = "AV Release date not present in data"
if obj.system.threat_version.cdata in obj.system.get_elements():
    tver = obj.system.threat_version.cdata
else:
    tver = "Threat version not present in data"
if obj.system.threat_release_date.cdata in obj.system.get_elements():
    trel = obj.system.threat_release_date.cdata
else:
    trel = "Threat release date not present in data"
if obj.system.wf_private_version.cdata in obj.system.get_elements():
    wfpver = obj.system.wf_private_version.cdata
else:
    wfpver = "Wildfire Private Version not present in data"
if obj.system.wf_private_release_date.cdata in obj.system.get_elements():
    wfprel = obj.system.wf_private_release_date.cdata
else:
    wfprel = "Wildfire Private Release Date not present in data"
if obj.system.wildfire_version.cdata in obj.system.get_elements():
    wfver = obj.system.wildfire_version.cdata
else:
    wfver = "Wildfire version not present in data"
if obj.system.wildfire_rt in obj.system.get_elements():
    wfrel = obj.system.wildfire_rt.cdata
else:
    wfrel = "Wildfire release date not present in data"
if obj.system.url_db.cdata in obj.system.get_elements():
    urldb = obj.system.url_db.cdata
else:
    urldb = "URL DB source not present in data"
if obj.system.url_filtering_version.cdata in obj.system.get_elements():
    urlver = obj.system.url_filtering_version.cdata
else:
    urlver = "URL DB Version not present in data"
if obj.system.logdb_version.cdata in obj.system.get_elements():
    logdbver = obj.system.logdb_version.cdata
else:
    logdbver = "Log DB version not present in data"
print ("Host Name | MGT IP Address | Public IP | Netmask | Default Gateway | Is DHCP? | MGT IPV6 Address | MGT IPV6 Link Local | Uptime | MAC Address | System Time | Device Name | SW Version | Model | Serial Number | Family | App Version | App Release Date | Cloud Mode | Global Protect PKG Version | Device Dictionary Version | Device Dictionary Release Date | AV Version | AV Release Date | Threat Version | Threat Release Date | Private Wildfire Version | Wildfire Private Release Date | Wildfire Version | Wildfire Release Date | URL DB | URL Version | Logdb Version")
print (hostname +  " | " + ip + " | " + pubip + " | " + netmask + " | " + dgw +  " | " + isdhcp + " | " + ipv6a + " | " + ipv6ll +" | " + uptime +
       " | " + mac +
       " | " + tm +
       " | " + devicename +
       " | " + swver + 
       " | " + model +
       " | " + sn +
       " | " + family +
       " | " + appver +
       " | " + apprel +
       " | " + cloudmode +
       " | " + gppkgver +
       " | " + devdictver +
       " | " + devdictreldt + 
       " | " + avver + 
       " | " + avrel +
       " | " + tver + 
       " | " + trel +
       " | " + wfpver +
       " | " + wfprel +
       " | " + wfver + 
       " | " + wfrel +
       " | " + urldb +
       " | " + urlver + 
       " | " + logdbver)
