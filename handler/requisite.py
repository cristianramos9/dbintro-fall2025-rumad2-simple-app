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


    # called by method POST for endpoint '/requisite'
    def insertRequisite(self, req_json):
        dao = RequisiteDAO()

        # map request json
        classid = req_json['classid']
        reqid = req_json['reqid']
        prereq = req_json['prereq']

        if classid and reqid and prereq:
            if classid == reqid:
                return jsonify(Error = "Conflict"), 409

            pk = dao.insertRequisite(classid, reqid, prereq)
            temp = (classid, reqid, prereq)
            result = self.mapRequisite(temp)
            print(pk)

            return jsonify(result)
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
            return jsonify(self.mapRequisite(requisite))


    # called by method DELETE for endpoint '/requisite/{classid}/{reqid}'
    def deleteRequisiteByIDs(self, classid, reqid):
        dao = RequisiteDAO()
        temp = dao.deleteRequisiteByIDs(classid, reqid)

        if temp:
            return jsonify(DeleteStatus = "OK"), 200
        else:
            return jsonify(DeleteStatus = "Not Found"), 404
