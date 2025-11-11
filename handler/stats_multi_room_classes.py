from flask import jsonify

from dao.stats_multi_room_classes import MultiRoomClassesDAO



class MultiRoomClassesHandler:
    def getAllMultiRoomClasses(self):
        dao = MultiRoomClassesDAO()

        item_list = {}
        class_list = []

        result = dao.getAllMultiRoomClasses()
        print(len(result))

        for item in result:
            item_list = { "cid" : item[0], "distinct_rooms" : item[1] }
            class_list.append(item_list)

        return jsonify(class_list)


    def getMultiRoomClassesUsingParameter(self, year=None, semester=None, limit=None, orderby=None):

        if year:
            # validate year
            pass
        if semester:
            # validate semester
            pass
        if limit:
            # validate limit
            pass
        if orderby:
            # validate orderby
            pass

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


        return jsonify(class_list)




#       result = []

