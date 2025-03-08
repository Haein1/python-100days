import requests

api_key = "908d7e714d720c4836ce15c2e933d9d0"
lat = 34.2583
lon = 108.9286
end_point = "http://api.openweathermap.org/data/2.5/forecast"
w_params = {
"lat": 34.2583,
"lon": 108.9286,
"appid" : api_key
}



response = requests.get(end_point, params=w_params)

data = response.json()
print(type(data))
print(data)
print(response.status_code)