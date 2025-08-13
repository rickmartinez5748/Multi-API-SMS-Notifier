from flask import Flask, render_template, request, redirect, url_for, flash
from twilio.rest import Client
from message import message
import datetime

app = Flask(__name__, template_folder='templates')
app.secret_key = 'Ricardo123'

@app.route('/')
def index():
    return render_template("index.html")



@app.route('/sms', methods=['GET', 'POST'])
def send_sms():
        if request.method == "POST":
            account_sid = 'ACa981ba789c0ce75731f5fff3d970f84e'
            auth_token = '39e884e11b9fc219ef838c1ed747c396'

            client = Client(account_sid, auth_token)    
            
            #CAlling the message() function to generate the message from the three APIS
            msg=message()

            client.messages.create(
            body=msg,
            from_='+12532640822',        # my twilio number
            to='+16132616833'            # my phone number
            )

            #generating Flash Message
            flash("SMS sent successfully!")
            
            #Logging message to a text fiile
            time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            entry = f"{time} - {msg}\n\n"
            
            with open("log.txt", "a", encoding="utf-8") as file:
                file.write(entry)
            
            #redirecting page to index.html after sending the message and also
            #sending flash message with jinja
            return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)



