from flask import Flask, request, jsonify
from flask_cors import CORS

from handler.requisite import RequisiteHandler

app = Flask(__name__)
CORS(app)

# test route. delete before deployment.
@app.route('/')
def default():
    message = { "Default route" : "test." }
    
    return jsonify(message)

method_list = ['GET', 'POST', 'PUT', 'DELETE']

# route for inserting new requisite
@app.route('/teamCRJ/requisite', methods=method_list)
def insertRequisite():
    if request.method == 'POST':
        return RequisiteHandler().insertRequisite(request.json)
    else:
        return jsonify(Error = "Method Not Allowed"), 405


if __name__ == '__main__':
    app.run(debug=True)
