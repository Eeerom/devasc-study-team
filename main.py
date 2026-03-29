from flask import Flask
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def display_joke():
    # Get the current date in "Month Day, Year" format
    current_date = datetime.now().strftime('%B %d, %Y')
    
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        r = requests.get(url)
        data = r.json()
        return f"""
        <html>
            <body style="font-family: Arial; text-align: center; margin-top: 50px;">
                <h1>Joke of the Day - {current_date}</h1>
                <hr>
                <p style="font-size: 24px;">{data['setup']}</p>
                <p style="font-size: 30px; color: blue;"><strong>{data['punchline']}</strong></p>
                <br>
                <button onclick="window.location.reload();">Get Another Joke</button>
            </body>
        </html>
        """
    except:
        return f"<h1>Date: {current_date} | The joke server is sleepy.</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)