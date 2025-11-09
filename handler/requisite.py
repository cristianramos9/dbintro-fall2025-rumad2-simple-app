from flask import jsonify

from dao.requisite import RequisiteDAO

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
            pk = dao.insertRequisite(classid, reqid, prereq)
            temp = (classid, reqid, prereq)
            result = self.mapRequisite(temp)
            print(pk)

            return jsonify(result)
        else:
            return jsonify(Error = "Bad Request"), 400
