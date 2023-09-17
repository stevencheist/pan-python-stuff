#!/usr/bin/python
#pass creds and generate API key
def keymaker():
        import pan.xapi
        import os
        from cred import get_pan_credentials
        credentials = get_pan_credentials()
        host = str(credentials['hostname'])
        #print(host)
        user = str(credentials['api_username'])
        #print(user)
        passwd = str(credentials['api_password'])
        #print(passwd)
        xapi = pan.xapi.PanXapi(hostname=host, api_username=user, api_password=passwd)
        key = xapi.keygen()
        os.environ["pahostname"]=host
        os.environ["api_key"]=key
        return key
#use api to run show system info command and return in xml format
def getsysinfo():
        import pan.xapi
        import os
        keymaker()
        xapi = pan.xapi.PanXapi(hostname=os.environ["pahostname"],api_key=os.environ["api_key"])
        xapi.op(cmd='show system info', cmd_xml=True)
        return xapi.xml_result()
#use api to run show routing route command and pull back the routing table in xml format
def getroutes():
        import pan.xapi
        import os
        keymaker()
        xapi = pan.xapi.PanXapi(hostname=os.environ["pahostname"],api_key=os.environ["api_key"])
        xapi.op(cmd='show routing route', cmd_xml=True)
        return xapi.xml_result()
#use api to clear sessions from pan fw
def clearsesall():
        import pan.xapi
        import os
        keymaker()
        xapi = pan.xapi.PanXapi(hostname=os.environ["pahostname"],api_key=os.environ["api_key"])
        xapi.op(cmd='clear session all', cmd_xml=True)
        return xapi.xml_result()
#use api to get ntp configuration and status
def getntp():
        import pan.xapi
        import os
        keymaker()
        xapi = pan.xapi.PanXapi(hostname=os.environ["pahostname"],api_key=os.environ["api_key"])
        xapi.op(cmd='show ntp', cmd_xml=True)
        return xapi.xml_result()
#use api to pull pan administrators
def getusers():
        import pan.xapi
        import os
        keymaker()
        xapi = pan.xapi.PanXapi(hostname=os.environ["pahostname"],api_key=os.environ["api_key"])
        xpath = "/config/mgt-config/users"
        xapi.show(xpath)
        return xapi.xml_result()
#use api to pull pan admin roles
def getadminroles():
        import pan.xapi
        import os
        keymaker()
        xapi = pan.xapi.PanXapi(hostname=os.environ["pahostname"],api_key=os.environ["api_key"])
        xpath = "/config/shared/admin-role"
        xapi.show(xpath)
        return xapi.xml_result()
#use api to pull interface information
def getinterfaces():
        import pan.xapi
        import os
        keymaker()
        xapi = pan.xapi.PanXapi(hostname=os.environ["pahostname"],api_key=os.environ["api_key"])
        xpath = "/config/devices/entry[@name='localhost.localdomain']/network/interface"
        xapi.show(xpath)
        return xapi.xml_result()
