from dopy.manager import DoManager
from os import environ
do = DoManager(None, environ["DO_API_TOKEN"], api_version=2)
a=[]
for d in do.all_active_droplets():
    do.destroy_droplet(d['id'])
