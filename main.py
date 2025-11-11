from flask import Flask, request, jsonify
from flask_cors import CORS

from handler.requisite import RequisiteHandler
from handler.stats_sections_by_day import SectionsByDayHandler
from handler.stats_multi_room_classes import MultiRoomClassesHandler

app = Flask(__name__)
CORS(app)

# test route. delete before deployment.
@app.route('/')
def default():
    message = { "Default route" : "test." }
    
    return jsonify(message)

method_list = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']

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

@app.route('/teamCRJ/stats/sections-by-day', methods=method_list)
def getSectionsByDay():
    if request.method == 'GET':
        # get arguments passed to endpoint
        year = request.args.get('year')
        semester = request.args.get('semester')

        print(year)
        print(semester)
        print(year, semester)

        return SectionsByDayHandler().getSectionsByDayUsingParameter(year, semester)
    else:
        return jsonify(Error = "Method Not Allowed"), 405


#   if year and not semester:
#       return jsonify("year DETECTED, no semester")
#       return SectionsByDayHandler().getSectionsByDayUsingYear(year)
#   elif not year and semester:
#       return jsonify("semester DETECTED, no year")
#       return SectionsByDayHandler().getSectionsByDayUsingSemester(semester)
#   elif year and semester:
#       return jsonify("BOTH year and semester DETECTED")
#       return SectionsByDayHandler().getSectionsByDayUsingYearSemester(year, semester)
#   else:
#       return SectionsByDayHandler().getSectionsByDay()


@app.route('/teamCRJ/stats/multi-room-classes', methods=method_list)
def getMultiRoomClasses():
    if request.method == 'GET':
        # get arguments passed to endpoint
        year = request.args.get('year')
        semester = request.args.get('semester')
        limit = request.args.get('limit')
        orderby = request.args.get('orderby')

        print("DEBUG: year:", year)
        print("DEBUG: semester:", semester)
        print("DEBUG: limit:", limit)
        print("DEBUG: orderby:", orderby)

        return MultiRoomClassesHandler().getMultiRoomClassesUsingParameter(year, semester, limit, orderby)
    else:
        return jsonify(Error = "Method Not Allowed"), 405

    # check if at least one of the query parameters is not null
#   if year or semester:
#       return MultiRoomClassesHandler().getMultiRoomClassesUsingParameter(year, semester, limit, orderby)
#   else:
#       return MultiRoomClassesHandler().getAllMultiRoomClasses()


if __name__ == '__main__':
    app.run(debug=True)
