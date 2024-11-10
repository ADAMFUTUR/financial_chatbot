# app.py
from flask import Flask, request, jsonify
from chatbot import simple_chatbot

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    response = simple_chatbot(data['query'], data['company'], data['year'])
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
