import urllib.request
import json

#The following function tells you the current weather in Sudbury.
def get_weather():
   
   url="https://api.openweathermap.org/data/2.5/weather?q=Sudbury&appid=884db306856a765ed4d4ecd3f01a7e3b"
   request=urllib.request.urlopen(url)
   result=json.loads(request.read())
   
   
   temp=round((result["main"]["temp"]-273.15),1)
   feel=round((result["main"]["feels_like"]-273.15),1)
   

   return f"The weather in {result["name"]} is {temp} and feels like {feel}."




