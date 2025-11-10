from flask import jsonify

from dao.stats_sections_by_day import SectionsByDayDAO

debug = "DEBUG:"

class SectionsByDayHandler:
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
        dao = SectionsByDayDAO()

        days = ['L','M','W','J','V','S','D']
        result_list = []
        
        result = dao.getSectionCountUsingYearSemester(year, semester)
        print(debug, result, "type:", type(result))

        for day in days:
            wday = { "day" : day, "sections" : result[day] }
            result_list.append(wday)

        return jsonify(result_list)

