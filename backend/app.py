import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/data', methods=['POST'])
def receive_data():
    raw_data = request.data.decode('utf-8')
    print("Data received:", raw_data)

    print("Sending data to the model API")

    headers = {'Content-Type': 'text/plain; charset=utf-8'}
    response = requests.post("http://127.0.0.1:8000/score-product", data=raw_data.encode('utf-8'), headers=headers)

    if response.status_code == 200:
        result = response.json()
        print('reponse recieved ' , result)
        return jsonify({"status": "success", "data": result.get('response')})
    else:
        return jsonify({"status": "error", "message": response.text}), response.status_code


if __name__ == '__main__':
    app.run(port=5000, debug=True)
