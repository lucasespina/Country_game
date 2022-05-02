
import math
def haversine(r, lat1, long1, lat2, long2):
    
    d = (r*2*math.atan2(math.sqrt(math.sin(math.radians(lat2-lat1)/2.0)**2+math.cos(math.radians(lat1))*math.cos(math.radians(lat2))*math.sin(math.radians(long2-long1)/2.0)**2),math.sqrt(1-(math.sin(math.radians(lat2-lat1)/2.0)**2+math.cos(math.radians(lat1))*math.cos(math.radians(lat2))*math.sin(math.radians(long2-long1)/2.0)**2))))
    
    return d

