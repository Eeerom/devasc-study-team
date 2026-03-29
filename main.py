from flask import Flask
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def display_joke():
    current_date = datetime.now().strftime('%B %d, %Y')
    url = "https://official-joke-api.appspot.com/random_joke"
    
    try:
        r = requests.get(url)
        data = r.json()
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Joke of the Day</title>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    height: 100vh;
                    margin: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    color: #333;
                }}
                .card {{
                    background: white;
                    padding: 40px;
                    border-radius: 20px;
                    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
                    max-width: 500px;
                    width: 90%;
                    text-align: center;
                }}
                h1 {{ color: #4a5568; font-size: 1.2rem; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 1px; }}
                .setup {{ font-size: 1.5rem; font-weight: 600; margin-bottom: 20px; line-height: 1.4; }}
                .punchline {{ font-size: 1.8rem; color: #5a67d8; font-weight: 800; margin-bottom: 30px; }}
                button {{
                    background-color: #5a67d8;
                    color: white;
                    border: none;
                    padding: 12px 25px;
                    border-radius: 10px;
                    font-size: 1rem;
                    cursor: pointer;
                    transition: transform 0.2s, background 0.2s;
                }}
                button:hover {{ background-color: #4c51bf; transform: scale(1.05); }}
                footer {{ margin-top: 20px; font-size: 0.8rem; color: #a0aec0; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>{current_date}</h1>
                <div class="setup">{data['setup']}</div>
                <div class="punchline">{data['punchline']}</div>
                <button onclick="window.location.reload();">Next Joke</button>
                <footer>Created by Eeerom | DEVASC Project</footer>
            </div>
        </body>
        </html>
        """
    except:
        return "<h1>The joke server is offline. Check your internet!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)