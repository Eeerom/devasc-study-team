from flask import Flask, render_template_string
import requests
from datetime import datetime

app = Flask(__name__)

# The HTML template remains as a constant string
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Joke of the Day</title>
    <style>
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            height: 100vh; 
            display: flex; 
            justify-content: center; 
            align-items: center; 
            margin: 0; 
        }
        .card { 
            background: white; 
            padding: 2.5rem; 
            border-radius: 20px; 
            box-shadow: 0 15px 35px rgba(0,0,0,0.3); 
            text-align: center; 
            max-width: 450px; 
            width: 90%; 
        }
        h1 { color: #333; margin-bottom: 1.5rem; }
        p { color: #555; line-height: 1.6; font-size: 1.1rem; }
        .setup { font-weight: bold; color: #764ba2; }
        .punchline { margin-top: 1rem; color: #444; }
        hr { border: 0; border-top: 1px solid #eee; margin: 1.5rem 0; }
        small { color: #888; display: block; margin-bottom: 1rem; }
        button { 
            background: #764ba2; 
            color: white; 
            border: none; 
            padding: 12px 25px; 
            border-radius: 30px; 
            cursor: pointer; 
            font-size: 1rem; 
            transition: transform 0.2s, background 0.2s; 
        }
        button:hover { 
            background: #667eea; 
            transform: scale(1.05); 
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Daily Joke API</h1>
        <p class="setup">{{ setup }}</p>
        <p class="punchline"><em>{{ punchline }}</em></p>
        <hr>
        <small>Server Time: {{ date }}</small>
        <button onclick="window.location.reload();">Get New Joke</button>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    # CRITICAL: This variable must stay inside the route function 
    # so it updates on every page refresh.
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        # Fetching data from the external REST API
        response = requests.get("https://official-joke-api.appspot.com/random_joke", timeout=5)
        data = response.json()
        setup = data['setup']
        punchline = data['punchline']
    except Exception as e:
        # Fallback in case the API is down
        setup = "Why did the API stay home?"
        punchline = "Because it had a bad connection."
    
    return render_template_string(
        HTML_TEMPLATE, 
        setup=setup, 
        punchline=punchline,
        date=current_time
    )

if __name__ == '__main__':
    # Set debug=False for production/Render deployment
    app.run(debug=True)