import requests

api_key = 'e951f560283cca984574bf6dd23799c4'

LAT = 52.23244453497716
LON = 20.984389183459356

data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={api_key}")

print(data.json())