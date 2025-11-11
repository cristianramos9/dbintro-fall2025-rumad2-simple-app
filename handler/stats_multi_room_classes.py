from flask import jsonify

from dao.stats_multi_room_classes import MultiRoomClassesDAO



class MultiRoomClassesHandler:
#   def getAllMultiRoomClasses(self):
#       dao = MultiRoomClassesDAO()
#       item_list = {}
#       class_list = []
#       result = dao.getAllMultiRoomClasses()
#       print(len(result))
#       for item in result:
#           item_list = { "cid" : item[0], "distinct_rooms" : item[1] }
#           class_list.append(item_list)
#       return jsonify(class_list)


    def getMultiRoomClassesUsingParameter(self, year=None, semester=None, limit=None, orderby=None):

        if year != None:
            # validate year
            if len(year) != 4 or not year.isnumeric():
                return jsonify(Error = "Bad Request"), 400
        if semester != None:
            # validate semester
            if not semester.isalnum() or semester.lower() not in ['fall', 'spring', 'v1', 'v2']:
                return jsonify(Error = "Bad Request"), 400
            semester = semester[0].upper() + semester[1:]
        if limit != None:
            # validate limit
            if not limit.isnumeric() or len(limit) > 2 or int(limit) > 10 or int(limit) < 1:
                return jsonify(Error = "Bad Request"), 400
        else:
            limit = 5
        if orderby != None:
            print("alpha:", orderby.isalpha())
            # validate orderby
            if not orderby.isalpha() or orderby.lower() not in ['asc', 'desc']:
                return jsonify(Error = "Bad Request"), 400

        dao = MultiRoomClassesDAO()

        item_list = {}
        class_list = []

        print("DEBUG: h.year:", year)  
        print("DEBUG: h.semester:", semester)  
        print("DEBUG: h.limit:", limit)  
        print("DEBUG: h.orderby:", orderby)  

        result = dao.getMultiRoomClassesUsingParameter(year, semester, limit, orderby)
        print(len(result))

        for item in result:
            item_list = { "cid" : item[0], "fullcode" : item[1] + item[2], "distinct_rooms" : item[3] }
            class_list.append(item_list)


        return jsonify(class_list), 200
