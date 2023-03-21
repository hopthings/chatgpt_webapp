import os

import openai
from flask import Flask, jsonify, render_template, request, session

app = Flask(__name__)
app.secret_key = os.urandom(24)
openai.api_key = os.environ["OPENAI_API_KEY"]

with open("system_card.txt", "r") as file:
    system = file.read()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    user_message = data["message"]
    history = data["history"]

    messages = [{"role": msg["role"], "content": msg["content"]} for msg in history]
    messages.append({"role": "system", "content": system})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        # max_tokens=50,
        n=1,
        temperature=1,
    )

    ai_message = response.choices[0].message["content"].strip()

    return jsonify(ai_message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
