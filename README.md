# Themed SMS Sender – Flask Web App

This is a fun Flask web application that simulates sending SMS messages by randomly selecting content from one of three themed modules:

- A greeting from a real astronaut in space  
- A message from a fictional Harry Potter character  
- The current weather in Sudbury, Canada  

## How It Works

When the user clicks the **Send Message** button on the web page:

1. The app randomly selects one of the three themed message generators.
2. It sends the message content (simulated SMS) and displays a success flash message.
3. The generated message is also logged in a `log.txt` file for record-keeping.

## Technologies Used

- Python
- Flask
- Jinja2
- REST APIs:
  - [Open Notify API](http://api.open-notify.org/astros.json)
  - [HP API](https://hp-api.onrender.com/api/characters)
  - [OpenWeatherMap API](https://openweathermap.org/)
