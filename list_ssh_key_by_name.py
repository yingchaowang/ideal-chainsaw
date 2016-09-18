from dopy.manager import DoManager
from os import environ
do = DoManager(None, environ["DO_API_TOKEN"], api_version=2)
from pprint import PrettyPrinter as pp
p=pp()
#p.pprint([x for x in do.all_ssh_keys() if x['name'] == 'xps 13 bootcamp'])
p.pprint([x for x in do.all_ssh_keys() if 'boot' in x['name']])
