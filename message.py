from weather import get_weather
from astros import get_astro
from harry_potter import get_hp

#The following function joins messages from three APIS

def message():

    
    return f"{get_weather()}{get_astro()}{get_hp()}"



