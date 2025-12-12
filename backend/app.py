from flask import Flask, jsonify, request
import random

app = Flask(__name__)
quotes = [
        "Believe in yourself.",
        "Every day is a new beginning.",
        "Success is not final, failure is not fatal."
]


@app.get("/quote")

def get_quote():
    return jsonify({"quote": random.choice(quotes)})



@app.post("/add_quote")

def add_quote():
    data = request.get_json()
    new_quote = data.get("quote")
    quotes.append(new_quote)
    return jsonify({"message": "Quote added", "total_quotes": len(quotes)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)