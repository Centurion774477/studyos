import httpx as requests
import json

import os

try:
    from dotenv import load_dotenv
    load_dotenv()
    WORKER = os.getenv("WORKER", "http://localhost:8000")
except ImportError:
    WORKER = os.environ.get("WORKER", "http://localhost:8000")
    pass

def login(username, password):
    payload = {
        "name": username,
        "pass": password
    }

    try:
        response = requests.post(WORKER+"/login", json=payload, timeout=10)
        
        response.raise_for_status()

        if response.status_code != 200:
            print(f"Status code {response.status_code}. Error logging in")
            return ("","")
        else:
            user = json.loads(response.text)
            return (user["name"], user["token"])

        
    except:
        print(f"Error")
        return ("","")

def register(username, password):
    payload = {
        "name": username,
        "pass": password
    }

    try:
        response = requests.post(WORKER+"/register", json=payload, timeout=10)
        
        response.raise_for_status()

        if response.status_code != 201:
            print(f"Status code {response.status_code}. Error registering")
            return ("","")
        else:
            user = json.loads(response.text)
            return login(username, password)

        
    except:
        print(f"Error")
        return ("","")

def logout(username, token) -> None:
    payload = {
        "user": username,
        "token": token
    }

    try:
        response = requests.post(WORKER+"/logout", json=payload, timeout=10)
        
        response.raise_for_status()
        
    except:
        print(f"Error")