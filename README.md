# Themed SMS Sender – Flask Web App

This web app uses Flask to combine data from three different APIs into a custom notification message, which is then sent via Twilio SMS. I also created a simple front-end interface to trigger messages with a single click. This project was designed to demonstrate how various services can work together to automate updates and alerts. It showcases integration skills and practical automation using REST APIs.

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
