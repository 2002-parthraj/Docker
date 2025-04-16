# app.py
import requests
res = requests.get("https://official-joke-api.appspot.com/random_joke")
joke = res.json()
print(f"{joke['setup']} - {joke['punchline']}")

