from flask import Flask, request, jsonify
from flask_cors import CORS

from handler.requisite import RequisiteHandler
from handler.stats import StatsHandler

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

# route for requesting requisite
@app.route('/teamCRJ/requisite/<int:classid>/<int:reqid>', methods=method_list)
def getRequisiteByIDs(classid, reqid):
    if request.method == 'GET':
        return RequisiteHandler().getRequisiteByIDs(classid, reqid)
    elif request.method == 'DELETE':
        return RequisiteHandler().deleteRequisiteByIDs(classid, reqid)
    else:
        return jsonify(Error = "Method Not Allowed"), 405

@app.route('/teamCRJ/stats/sections-by-day')
def getSectionsByDay():
    # get arguments passed to endpoint
    year = request.args.get('year')
    semester = request.args.get('semester')

    print(year)
    print(semester)
    print(year, semester)

    if year and not semester:
#       return jsonify("year DETECTED, no semester")
        return StatsHandler().getSectionsByDayUsingYear(year)
    elif not year and semester:
#       return jsonify("semester DETECTED, no year")
        return StatsHandler().getSectionsByDayUsingSemester(semester)
    elif year and semester:
#       return jsonify("BOTH year and semester DETECTED")
        return StatsHandler().getSectionsByDayUsingYearSemester(year, semester)
    else:
        return StatsHandler().getSectionsByDay()



#   tmp_results = [{}]
#   return jsonify(results = tmp_results)
#   return jsonify([year, semester])

if __name__ == '__main__':
    app.run(debug=True)
