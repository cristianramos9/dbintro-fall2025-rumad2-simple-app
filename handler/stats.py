from flask import jsonify

from dao.stats import StatsDAO

debug = "DEBUG:"

class StatsHandler:
    def getSectionsByDay(self):
        dao = StatsDAO()

        days = ['L','M','W','J','V','S','D']
        result_list = []
        
        result = dao.getSectionCount()

        for day in days:
            wday = { "day" : day, "sections" : result[day][0] }
            result_list.append(wday)

        return jsonify(result_list)
