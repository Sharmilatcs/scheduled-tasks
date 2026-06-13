from multiprocessing.connection import Client
from twilio.rest import Client
import os

import requests

# with open(file="api_key.txt", mode="r") as file:
#     api_key = file.read().strip()

api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat" : 27.664827,
    "lon": -81.515755,
    "cnt": "4",
    "appid": api_key

}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data=response.json()
item = 0
will_rain = False
for item in range(len(data["list"])):
     code = data["list"][item]["weather"][0]["id"]
     if code < 700:
        will_rain = True

if will_rain:

    client = Client(account_sid, auth_token)
    message = client.messages.create(body = "Rain Rain!. Pls dont forget to take Umbrella",
                                     from_="+18443525310",
                                     to="+17797745994")
    print(message.status)




# print(data["list"][0]["weather"][0]["id"])
# print(data["list"][1]["weather"][0]["id"])
# print(data["list"][2]["weather"][0]["id"])
# print(data["list"][3]["weather"][0]["id"])
