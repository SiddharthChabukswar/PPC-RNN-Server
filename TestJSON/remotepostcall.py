import json
import numpy as np
import requests
import time

f = open('response.json')

data = json.load(f)

print("Started")

start_time = time.time()

r = requests.post('http://127.0.0.1:8000/grade/', json={"Type": "Type1", "Data" : data["Type1"]})
print(r.json())

r = requests.post('http://127.0.0.1:8000/grade/', json={"Type": "Type2", "Data" : data["Type2"]})
print(r.json())

r = requests.post('http://127.0.0.1:8000/grade/', json={"Type": "Type3", "Data" : data["Type3"]})
print(r.json())

r = requests.post('http://127.0.0.1:8000/grade/', json={"Type": "Type4", "Data" : data["Type4"]})
print(r.json())

r = requests.post('http://127.0.0.1:8000/grade/', json={"Type": "Type5", "Data" : data["Type5"]})
print(r.json())

r = requests.post('http://127.0.0.1:8000/grade/', json={"Type": "Type6", "Data" : data["Type6"]})
print(r.json())

print("--- %s seconds ---" % (time.time() - start_time))

f.close() 