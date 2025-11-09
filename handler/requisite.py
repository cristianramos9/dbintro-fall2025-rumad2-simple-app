 from flask import jsonify

 class RequisiteHandler:
     def mapRequisite(self, req):
         result = {}

         result['classid'] = req[0]
         result['reqid'] = req[1]
         result['prereq'] = req[2]

         return result

