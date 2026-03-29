import requests

def get_joke():
    """Fetches a random joke from the Official Joke API."""
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        # Set a timeout so the app doesn't freeze if the API is down
        response = requests.get(url, timeout=5)
        
        # This checks for HTTP errors (like 404 or 500)
        response.raise_for_status()
        
        data = response.json()
        return f"{data['setup']}\n... {data['punchline']}"
    
    except requests.exceptions.RequestException as e:
        return f"Error: Could not retrieve joke. {e}"

if __name__ == "__main__":
    print("--- Welcome to the Student Joke App ---")
    joke = get_joke()
    print(joke)