from dotenv import load_dotenv
import os
import requests
import json
from datetime import datetime
import Adafruit_DHT as dht


now = datetime.now() # current date and time
load_dotenv()
accessToken = os.getenv('FAUNA_KEY')
endpoint = f"https://graphql.us.fauna.com/graphql"
headers = {
    'Authorization': f"Bearer {accessToken}"
}
DHT = 4
h,t = dht.read_retry(dht.DHT22, DHT)


current_time = now.strftime("%Y-%m-%dT%H:%M:%SZ")
date = now.strftime("%Y-%m-%d")
temp = t *1.8 + 32

query = """mutation {
  createTemperature(
    data: {
          temp: %s
          time: "%s"
          date: "%s"
        }
  ){
    temp
    time
    date
  }
}""" % (int(temp), current_time, date)

json_data = {
    'query': query
}

print(json_data)

r = requests.post(endpoint, headers=headers, json=json_data)
if r.status_code == 200:
    print(json.dumps(r.json(), indent=2))
else:
    raise Exception(f"Query failed to run with a {r.status_code}.")