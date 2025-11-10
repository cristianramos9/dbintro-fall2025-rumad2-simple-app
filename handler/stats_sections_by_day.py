from flask import jsonify

from dao.stats_sections_by_day import SectionsByDayDAO

debug = "DEBUG:"

class SectionsByDayHandler:
    semester_list = ("Fall", "Spring", "V1", "V2")
    def getSectionsByDay(self):
        dao = SectionsByDayDAO()

        days = ['L','M','W','J','V','S','D']
        result_list = []
        
        result = dao.getSectionCount()
        print(result)

        for day in days:
            wday = { "day" : day, "sections" : result[day] }
            result_list.append(wday)
            print(debug, day)
        return jsonify(result_list)

    
    def getSectionsByDayUsingYear(self, year):
        # validate year
        print("year a number?", year.isnumeric())
        print("year 4 digit?", len(year))
        print("year 4 digit?", len(year) == 4)
        if len(year) != 4 or not year.isnumeric():
            return jsonify(Error = "Bad Request"), 400

        dao = SectionsByDayDAO()

        days = ['L','M','W','J','V','S','D']
        result_list = []
        
        result = dao.getSectionCountUsingYear(year)
        print(debug, result, "type:", type(result))

        for day in days:
            wday = { "day" : day, "sections" : result[day] }
            result_list.append(wday)

        return jsonify(result_list)


    def getSectionsByDayUsingSemester(self, semester):
        if semester not in self.semester_list:
            return jsonify(Error = "Bad Request"), 400

        dao = SectionsByDayDAO()

        days = ['L','M','W','J','V','S','D']
        result_list = []
        
        result = dao.getSectionCountUsingSemester(semester)
        print(debug, result, "type:", type(result))

        for day in days:
            wday = { "day" : day, "sections" : result[day] }
            result_list.append(wday)

        return jsonify(result_list)
    

    def getSectionsByDayUsingYearSemester(self, year, semester):
        if len(year) != 4 or not year.isnumeric():
            return jsonify(Error = "Bad Request"), 400
        if semester not in self.semester_list:
            return jsonify(Error = "Bad Request"), 400


        dao = SectionsByDayDAO()

        days = ['L','M','W','J','V','S','D']
        result_list = []
        
        result = dao.getSectionCountUsingYearSemester(year, semester)
        print(debug, result, "type:", type(result))

        for day in days:
            wday = { "day" : day, "sections" : result[day] }
            result_list.append(wday)

        return jsonify(result_list)

