# Created by: Aswin KS

# Import the required modules
import os
import requests
from pywebio import start_server
from pywebio.output import put_text, put_markdown, put_success, put_error
from pywebio.input import input, TEXT, select


# Specify the backent URL to connect to. This is the backend API microservice 

BACKEND_URL = os.getenv("BACKEND_URL", "http://quotes-backend:5000") 

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
                resp = requests.post(f"{BACKEND_URL}/add_quote", json={"quote":quote})
                if resp.status_code in [200,201]:
                        put_success("Quote added successfully")
                # if the return code is not success then print the error
                else:
                        put_error("Failed to add quote")
                #if an exception occure, then print the exception 
        except Exception as e:
                    put_error(f"Error connecting the backend: {e}")
                
#--------------------ADD QUOTE COMPLETED-------------------------------

# Function to show daily quotes

def show_daily_quote():
        try:
                # sent a get request to backend API
                resp = requests.get(f"{BACKEND_URL}/quote")

                # if return code is 200 then print the quote, if not print the error
                if resp.status_code == 200:
                        quote = resp.json().get("quote") 
                        put_markdown(f"### Daily Motivation\n\n> {quote}")
                else:
                        put_error("Failed to fetch quotes")
                # if any exception, print the exception
        except Exception as e:
                put_error(f"Error connecting to backend: {e}")



#--------------------SHOW DAILY QUOTE COMPLETED-------------------------------

# Main function. Program starts from here.

def main():
        
        #Heading for out home page
        put_markdown("# 🌟 Quotes Maker — Frontend")

        # Option chooser
        put_markdown("Choose an option:")
        action = select("Select an option", ["Add Quote", "View Quote"])
        
        # Call the function according to the selection
        if action.lower() == "add quote":
            add_quote()
        elif action.lower() == "view quote":
            show_daily_quote()
        else:
            put_error("Invalid option")


# Start the server on port 8080
if __name__ == "__main__":
    start_server(main, port=8080, debug=True)

#--------------------MAIN FUNCTION COMPLETED-------------------------------