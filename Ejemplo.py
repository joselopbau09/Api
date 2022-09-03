
import requests, json
 
# Key
api_key = "6978498fcfa6f2e476645ab243ed9194"
 
# Url
url = "http://api.openweathermap.org/data/2.5/weather?"
 
# lat lon
lat = input("Enter latitude: ")

lon = input("Enter longitude: ")
 
# Concatetion url
complete_url = f'{url}lat={lat}&lon={lon}&appid={api_key}'
 

response = requests.get(complete_url)
 
x = response.json()

print(x)
