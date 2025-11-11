from flask import request, jsonify, Blueprint

from dao.stats_sections_by_day import SectionsByDayDAO

debug = "DEBUG:"
bp = Blueprint("stat_sections_by_day", __name__)
method_list = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']

# ROUTE

@bp.route('/stats/sections-by-day', methods=method_list)
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

# HANDLER

class SectionsByDayHandler:
#   def getSectionsByDay(self):
#       dao = SectionsByDayDAO()
#       days = ['L','M','W','J','V','S','D']
#       result_list = []
#       result = dao.getSectionCount()
#       print(result)
#       for day in days:
#           wday = { "day" : day, "sections" : result[day] }
#           result_list.append(wday)
#           print(debug, day)
#       return jsonify(result_list)

    
#   def getSectionsByDayUsingYear(self, year):
#       # validate year
#       print("year a number?", year.isnumeric())
#       print("year 4 digit?", len(year))
#       print("year 4 digit?", len(year) == 4)
#       if len(year) != 4 or not year.isnumeric():
#           return jsonify(Error = "Bad Request"), 400
#       dao = SectionsByDayDAO()
#       days = ['L','M','W','J','V','S','D']
#       result_list = []
#       result = dao.getSectionCountUsingYear(year)
#       print(debug, result, "type:", type(result))
#       for day in days:
#           wday = { "day" : day, "sections" : result[day] }
#           result_list.append(wday)
#       return jsonify(result_list)


#   def getSectionsByDayUsingSemester(self, semester):
#       if semester not in self.semester_list:
#           return jsonify(Error = "Bad Request"), 400
#       dao = SectionsByDayDAO()
#       days = ['L','M','W','J','V','S','D']
#       result_list = []
#       result = dao.getSectionCountUsingSemester(semester)
#       print(debug, result, "type:", type(result))
#       for day in days:
#           wday = { "day" : day, "sections" : result[day] }
#           result_list.append(wday)
#       return jsonify(result_list)
    

#   def getSectionsByDayUsingYearSemester(self, year, semester):
#       if len(year) != 4 or not year.isnumeric():
#           return jsonify(Error = "Bad Request"), 400
#       if semester not in self.semester_list:
#           return jsonify(Error = "Bad Request"), 400
#       dao = SectionsByDayDAO()
#       days = ['L','M','W','J','V','S','D']
#       result_list = []
#       result = dao.getSectionCountUsingYearSemester(year, semester)
#       print(debug, result, "type:", type(result))
#       for day in days:
#           wday = { "day" : day, "sections" : result[day] }
#           result_list.append(wday)
#       return jsonify(result_list)


    # gets count with or without query parameters
    def getSectionsByDayUsingParameter(self, year=None, semester=None):
        if year != None:
            # validate year
            if len(year) != 4 or not year.isnumeric():
                return jsonify(Error = "Bad Request"), 400
        if semester != None:
            # validate semester
            if not semester.isalnum() or semester.lower() not in ['fall', 'spring', 'v1', 'v2']:
                return jsonify(Error = "Bad Request"), 400
            semester = semester[0].upper() + semester[1:]
            
#           semester_list = ()
#           if semester not in ["fall", "spring", "v1", "v2"]:
#               return jsonify(Error = "Bad Request"), 400


        dao = SectionsByDayDAO()

        days = ['L','M','W','J','V','S','D']
#       days = ['L']
        result_list = []
        
        result = dao.getSectionCountUsingParameter(year, semester)
        print(debug, result, "type:", type(result))

        for day in days:
            wday = { "day" : day, "sections" : result[day] }
            result_list.append(wday)

        return jsonify(result_list), 200

