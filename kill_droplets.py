from dopy.manager import DoManager
from os import environ
do = DoManager(None, environ["DO_API_TOKEN"], api_version=2)
for x in do.all_active_droplets():
    a.append(x['id'])
for id in a:
    do.destroy_droplet(id)

