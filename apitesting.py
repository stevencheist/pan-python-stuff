#!/usr/bin/python
#pass creds and generate API key
def keymaker():
	import pan.xapi
	from cred import get_pan_credentials
	credentials = get_pan_credentials()
	host = credentials['hostname']
	user = credentials['api_username']
	passwd = credentials['api_password']
	xapi = pan.xapi.PanXapi(hostname=host, api_username=user, api_password=passwd)
	key = xapi.keygen()
	return key
#use api to run show system info command and return in xml format
def getsysinfo():
	import pan.xapi
	from cred import get_pan_credentials
	credentials = get_pan_credentials()
	apikey = credentials['api_key']
	host = credentials['hostname']
	xapi = pan.xapi.PanXapi(hostname=host,api_key=apikey)
	xapi.op(cmd='show system info', cmd_xml=True)
	return xapi.xml_result()
#use api to run show routing route command and pull back the routing table in xml format
def getroutes():
	import pan.xapi
        from cred import get_pan_credentials
        credentials = get_pan_credentials()
        apikey = credentials['api_key']
        host = credentials['hostname']
        xapi = pan.xapi.PanXapi(hostname=host,api_key=apikey)
        xapi.op(cmd='show routing route', cmd_xml=True)
        return xapi.xml_result()
#use api to clear sessions from pan fw
def clearsesall():
	import pan.xapi
        from cred import get_pan_credentials
        credentials = get_pan_credentials()
        apikey = credentials['api_key']
        host = credentials['hostname']
        xapi = pan.xapi.PanXapi(hostname=host,api_key=apikey)
        xapi.op(cmd='clear session all', cmd_xml=True)
        return xapi.xml_result()
#use api to get ntp configuration and status
def getntp():
	import pan.xapi
        from cred import get_pan_credentials
        credentials = get_pan_credentials()
        apikey = credentials['api_key']
        host = credentials['hostname']
        xapi = pan.xapi.PanXapi(hostname=host,api_key=apikey)
        xapi.op(cmd='show ntp', cmd_xml=True)
        return xapi.xml_result()
#use api to pull pan administrators
def getusers():
	import pan.xapi
	from cred import get_pan_credentials
	credentials = get_pan_credentials()
	apikey = credentials['api_key']
	host = credentials['hostname']
	xapi = pan.xapi.PanXapi(hostname=host, api_key=apikey)
	xpath = "/config/mgt-config/users"
	xapi.show(xpath)
	return xapi.xml_result()
#use api to pull pan admin roles
def getadminroles():
	import pan.xapi
        from cred import get_pan_credentials
        credentials = get_pan_credentials()
        apikey = credentials['api_key']
        host = credentials['hostname']
        xapi = pan.xapi.PanXapi(hostname=host, api_key=apikey)
        xpath = "/config/shared/admin-role"
        xapi.show(xpath)
        return xapi.xml_result()
#use api to pull interface information
def getinterfaces():
	import pan.xapi
        from cred import get_pan_credentials
        credentials = get_pan_credentials()
        apikey = credentials['api_key']
        host = credentials['hostname']
        xapi = pan.xapi.PanXapi(hostname=host, api_key=apikey)
        xpath = "/config/devices/entry[@name='localhost.localdomain']/network/interface"
        xapi.show(xpath)
        return xapi.xml_result()
