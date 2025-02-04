import requests
from datetime import datetime
'''
https://latlongdata.com/latitude-longitude-lookup/
'''
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code)
# # response.raise_for_status()
# data = response.json()
# print(data)
# latitude = data['iss_position']['latitude']
# longitude = data['iss_position']["longitude"]
# print(latitude)
# print(longitude)
# iss_position = (latitude, longitude)
# print(iss_position)

parameters = {
    "lat": 00.00000,
    "lng": 00.00000,
    "formatted": 0,
    "tzid": "Asia/Taipei"
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
data = response.json()
print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
# print(sunrise.split("T")[1].split(":")[0])
print(sunset)

time_now = datetime.now()
print(time_now.hour)