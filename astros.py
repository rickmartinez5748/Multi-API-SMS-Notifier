import urllib.request
import json
import random

#The following function sends a greeting from a random person in space
def get_astro():
   
   url="http://api.open-notify.org/astros.json"
   request=urllib.request.urlopen(url)
   result=json.loads(request.read())
   
   n_astro=int(result["number"])
   num=random.randint(0, n_astro-1)
   random_astronaut=result["people"][num]["name"]

   return f"There are {result["number"]} people in space and one of them ({random_astronaut}) sends you a greeting from the space."


