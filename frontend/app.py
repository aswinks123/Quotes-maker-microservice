# Import the required modules
import os
import requests
from pywebio import start_server
from pywebio.output import put_text, put_markdown, put_success, put_error
from pywebio.input import input, TEXT


# Specify the backent URL to connect to. This is the backend API microservice 

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:5000") 

# Function to add quotes

def add_quote():
        # ask the user to enter the quote
        quote = input("Enter a motivational quote", type=TEXT)

        # if user didnt enter any quote, print a message that it cannot be empty
        if not quote:
                put_text("Quote cannot be empty")
                return
        
        # if user type a valid quote, then sent a post request to backend API to add it to the database.
        try:
                resp = requests.post(f"{BACKEND_URL}/quotes", json={"quote":quote})
                if resp.status_code == 201:
                        put_success("Quote added successfully")
                # if the return code is not success then print the error
                else:
                        put_error("Failed to add quote")
                #if an exception occure, then print the exception 
        except Exception as e:
                    put_error(f"Error connecting the backend: {e}")
                
        



