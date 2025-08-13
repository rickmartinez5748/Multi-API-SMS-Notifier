import urllib.request
import json
import random

#The following function sends a message from a random fictinal character from the
#Harry Potter world and tells you who is actually the actor in the movies.

def get_hp():
   
   url="https://hp-api.onrender.com/api/characters"
   request=urllib.request.urlopen(url)
   result=json.loads(request.read())
   
   n_char=len(result)
   num=random.randint(0, n_char-1)
   random_character=result[num]    
   
   return f"Also, There are {n_char} characters in the Harry Potter world and one of them ({random_character["name"]}) sends you a greeting too. Howwever, this character is fictional because it was written by J.K Rowling and played in the movies by {random_character["actor"]}."


