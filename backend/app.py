# Created by: Aswin KS
# Integrating the back end API with postgres Database

# Import the necessary libraries
from flask import Flask, jsonify, request
import random, os
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


#-------------------DATABASE CONFIGURATION----------------

# We are taking the values of each variable needed to connect to db. 
# ("POSTGRES_USER", "postgres") : This means if an environment variable names "POSTGRES_USER" is set then take that value, else use the default value "postgres"

POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")  # default values is provided at end
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
POSTGRES_DB = os.getenv("POSTGRES_DB", "quotesdb")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "quotes-postgres")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

# SQLALCHEMY_DATABASE_URI tells SQLAlchemy where the database is.
#Format for PostgreSQ : postgresql://username:password@host:port/database_name

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# SQLAlchemy can track every object change in memory to emit signals, Setting it to False disables this extra overhead, which is good for performance.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initilizinf the SQLAlchemy.
# db is now your database object. We use it to define models, add or commit data, query etc
db = SQLAlchemy(app)


# -------------------- QUOTE TABLE MODEL CREATION --------------------

# You are defining a Python class called Quote.
# db.Model means SQLAlchemy knows this class represents a database table
# Each instance of Quote corresponds to a row in the table.


class Quote(db.Model):
    #represent that we have 2 columns. one for primary key and other for the quote
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)

# -------------------- INITIALIZE THE DB --------------------

# app.app_context() activates the Flask app temporarily, so code inside the with block knows which app it belongs to.
# The with statement in Python is used for context managers, After the block ends, Flask cleans up resources.
with app.app_context():
# This tells SQLAlchemy to create all tables defined by your models (like Quote) in the database. It only creates tables that don’t already exist. existing tables are left untouched
    db.create_all()



#---------------------------------API CREATION---------------

# API to retreive the quote from DB
@app.get("/quote")

def get_quote():
    # allows you to query the quote table in the database. all() → returns all rows as a list of Quote objects.
    # Output: [<Quote id=1 text='Believe in yourself'>, <Quote id=2 text='Every day is a new beginning'>] its a list of objects
    quotes = Quote.query.all()
    if not quotes:
        return jsonify({"quote": "No quotes available"})
    
    # This list comprehension converts the list of objects to a list of strings: ["Believe in yourself", "Every day is a new beginning"]
    return jsonify({"quote": random.choice([q.text for q in quotes])})


# API to add the quote to DB
@app.post("/add_quote")

def add_quote():
    data = request.get_json()
    new_quote_text = data.get("quote")
    if not new_quote_text:
        return jsonify({"message": "Quote cannot be empty"}), 400

# Creates a new instance of the Quote model.
# text=new_quote_text assigns the user-provided quote to the text column.
    new_quote = Quote(text=new_quote_text)

    # add() tells the session: “I want to insert this object into the database.”
    db.session.add(new_quote)
    # This finalizes the transaction and writes all pending changes to the database.
    db.session.commit()
    return jsonify({"message": "Quote added", "total_quotes": Quote.query.count()}), 201



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)