import requests as r



def get_location(ip):
    """Get the location of the ip address"""
    
    # make ip a string
    ip = str(ip)
    location = r.get("http://ipinfo.io/{}/json".format(ip)).json()
    # nicely print the location
    for i in location:
        print("{}: {}".format(i, location[i]))
    # return the location
    return 0


