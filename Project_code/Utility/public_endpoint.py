from asyncio.windows_events import NULL
import http
from flask import request, jsonify
import consts

#                       #
#   Public Endpoint     #
#                       #
def get_skitype_info():
    
    if request.method == 'GET':
        data=request.get_json()
        
        cur=consts.mysql.connection.cursor()

        if data:
            modeladd = ""
            sizeadd = ""

            if "model" in data:
                model_filter=data['model']
                modeladd = " AND `skitype`.`model`='" + model_filter + "'"
                print(modeladd)

            if "size" in data:
                size_filter=data['size']
                sizeadd = " AND `ski`.`length`='" + size_filter + "'"
                print(sizeadd)

            skiType_info= cur.execute("SELECT `ski`.`productID`, `ski`.`length`, `ski`.`weight`, `skitype`.`model`,`skitype`.`description`, `skitype`.`historical`, `skitype`.`url` FROM `ski` INNER JOIN `skitype` WHERE `ski`.`typeID` = `skitype`.`typeID`" + modeladd + sizeadd)
        else:
            skiType_info= cur.execute("SELECT `ski`.`productID`, `ski`.`length`, `ski`.`weight`, `skitype`.`model`,`skitype`.`description`, `skitype`.`historical`, `skitype`.`url` FROM `ski` INNER JOIN `skitype` WHERE `ski`.`typeID` = `skitype`.`typeID`")

        if skiType_info >0:
            skiType_info = cur.fetchall()

        cur.close()
        return jsonify(skiType_info),http.HTTPStatus.OK