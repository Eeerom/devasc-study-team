from flask import Flask, render_template_string
import requests

app = Flask(__name__)

# Simplified HTML template focusing on the joke content
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
            padding: 3rem; 
            border-radius: 20px; 
            box-shadow: 0 15px 35px rgba(0,0,0,0.3); 
            text-align: center; 
            max-width: 500px; 
            width: 90%; 
        }
        h2 { 
            color: #555; 
            letter-spacing: 2px; 
            font-size: 1rem; 
            margin-bottom: 2rem;
            text-transform: uppercase;
        }
        .setup { 
            font-size: 1.4rem; 
            color: #333; 
            margin-bottom: 1.5rem; 
            font-weight: 600;
        }
        .punchline { 
            font-size: 1.6rem; 
            color: #764ba2; 
            margin-bottom: 2.5rem; 
            font-weight: 800;
        }
        button { 
            background: #764ba2; 
            color: white; 
            border: none; 
            padding: 15px 35px; 
            border-radius: 10px; 
            cursor: pointer; 
            font-size: 1.1rem; 
            font-weight: bold;
            transition: all 0.3s ease; 
        }
        button:hover { 
            background: #667eea; 
            transform: translateY(-3px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        footer {
            margin-top: 2rem;
            font-size: 0.8rem;
            color: #bbb;
        }
    </style>
</head>
<body>
    <div class="card">
        <h2>Joke of the Day</h2>
        <p class="setup">{{ setup }}</p>
        <p class="punchline">{{ punchline }}</p>
        
        <button onclick="window.location.reload();">Next Joke</button>
        
        <footer>Created by Eeerom | DEVASC Project</footer>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    try:
        # Fetching from the Public REST API
        response = requests.get("https://official-joke-api.appspot.com/random_joke", timeout=5)
        data = response.json()
        setup = data['setup']
        punchline = data['punchline']
    except Exception:
        setup = "Connection Error"
        punchline = "Could not reach the joke server."
    
    return render_template_string(HTML_TEMPLATE, setup=setup, punchline=punchline)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)