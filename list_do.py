from dopy.manager import DoManager
from os import environ
do = DoManager(None, environ["DO_API_TOKEN"], api_version=2)
from pprint import PrettyPrinter as pp
p=pp()
p.pprint(do.all_active_droplets())
