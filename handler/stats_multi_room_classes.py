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
