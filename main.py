from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def display_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        r = requests.get(url)
        data = r.json()
        # This returns HTML that a browser can read
        return f"""
        <html>
            <body style="font-family: Arial; text-align: center; margin-top: 50px;">
                <h1>Developer Joke of the Day</h1>
                <hr>
                <p style="font-size: 24px;">{data['setup']}</p>
                <p style="font-size: 30px; color: blue;"><strong>{data['punchline']}</strong></p>
                <br>
                <button onclick="window.location.reload();">Get Another Joke</button>
            </body>
        </html>
        """
    except:
        return "<h1>Oops! The joke server is sleepy. Try again later.</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)