import requests
import sys
import json

url = ('http://srv-victoria-test:8428/api/v1/query?query=pg_database_size_size')
r = requests.get(url)
data_parse = r.json()
hosts = data_parse["data"] ["result"]


url2 = ('http://srv-victoria-test:8428/api/v1/query?query=pg_static')
r2 = requests.get(url2)
data_parse2 = r2.json()
hosts2 = data_parse2["data"] ["result"]



sys.stdout=open("hosts.csv","w")
print("host,database_name,version")
for i in hosts:
    for a in hosts2:
        if i["metric"] ["instance"] == a["metric"] ["instance"]:

            print(i["metric"] ["instance"].replace(':9187', ''), (i["metric"] ["datname"]), (a["metric"] ["short_version"]))

sys.stdout.close()
