import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    response = requests.get('https://randomuser.me/api/?results=10')
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
