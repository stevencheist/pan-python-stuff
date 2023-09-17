def get_pan_credentials():
	u=input("User:")
	p=input("Password:")
	h=input("Hostname:")
	cred = {}
	cred['api_username'] = str(u) 
	cred['api_password'] = str(p)
	cred['hostname'] = str(h)
	cred['api_key'] = ""
	return cred
