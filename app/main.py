from flask import Flask, jsonify

app = Flask(__name__)

games = [
    {"id": 1, "name": "God of War Ragnarök", "price": 299.90, "promo": False},
    {"id": 2, "name": "Spider-Man 2", "price": 349.90, "promo": True}
]

@app.route("/games")
def games_list():
    return jsonify(games)

@app.route("/notify")
def notify():
    return jsonify([g for g in games if g["promo"]])

if __name__ == "__main__":
    app.run()
