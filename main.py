from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# test route. delete before deployment.
@app.route('/')
def default():
    message = { "Default route" : "test." }
    
    return jsonify(message)


if __name__ == '__main__':
    app.run(debug=True)
