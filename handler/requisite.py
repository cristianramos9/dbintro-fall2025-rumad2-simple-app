from flask import jsonify

from dao.requisite import RequisiteDAO

debug = "DEBUG:"

class RequisiteHandler:
    def mapRequisite(self, req):
        result = {}

        result['classid'] = req[0]
        result['reqid'] = req[1]
        result['prereq'] = req[2]

        return result


    def existInClass(self, classid, reqid, dao):
        db_record = dao.getRequisiteByIDs(classid, reqid)
        print(debug, db_record, "type:", type(db_record))

        return db_record == None

    def isDuplicate(self, classid, reqid, dao):
        db_record = dao.getRequisiteByIDs(classid, reqid)

        if not db_record:
            return False

        db_record = self.mapRequisite(db_record)
        print(debug, db_record, "type:", type(db_record))

        # convert data from database to tuple
        from_database = (str(db_record['classid']), str(db_record['reqid']))
        print(debug, from_database, "type:", type(from_database))

        # convert keys from data to insert to tuple
        to_insert = (classid, reqid)
        print(debug, to_insert, "type:", type(to_insert))
        
        print(debug, from_database == to_insert)

        # compare both tuples and return if is duplicate
        return from_database == to_insert



    # called by method POST for endpoint '/requisite'
    def insertRequisite(self, req_json):
        dao = RequisiteDAO()

        # map request json
        classid = req_json['classid']
        reqid = req_json['reqid']
        prereq = req_json['prereq']

        if classid and reqid and prereq:
            if classid == reqid or self.isDuplicate(classid, reqid, dao):
                return jsonify(Error = "Conflict"), 409
#           if self.existInClass(classid, reqid, dao):
#               return jsonify(Error = "Invalid ids, not found"), 404


            pk = dao.insertRequisite(classid, reqid, prereq)
            temp = (classid, reqid, prereq)
            result = self.mapRequisite(temp)
            print(pk)

            return jsonify(result), 201
        else:
            return jsonify(Error = "Bad Request"), 400


    # called by method GET for endpoint '/requisite/{classid}/{reqid}'
    def getRequisiteByIDs(self, classid, reqid):
        if classid == reqid:
            return jsonify(Error = "Conflict"), 409

        dao = RequisiteDAO()
        requisite = dao.getRequisiteByIDs(classid, reqid)
        
        if not requisite:
            return jsonify(Error = "Not Found"), 404
        else:
            return jsonify(self.mapRequisite(requisite)), 200


    # called by method DELETE for endpoint '/requisite/{classid}/{reqid}'
    def deleteRequisiteByIDs(self, classid, reqid):
        if classid == reqid:
            return jsonify(Error = "Conflict"), 409

        dao = RequisiteDAO()
        temp = dao.deleteRequisiteByIDs(classid, reqid)

        if temp:
            return jsonify(DeleteStatus = "OK"), 204
        else:
            return jsonify(DeleteStatus = "Not Found"), 404


