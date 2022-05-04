from asyncio.windows_events import NULL
from flask import request, jsonify

#                       #
#   Public Endpoint     #
#                       #
def get_skitype_info(mysql):
    
    if request.method == 'GET':
        data=request.get_json()
        
        cur=mysql.connection.cursor()

        if data:
            model_filter=data['model']
            skiType_info= cur.execute("SELECT * FROM `skiType` WHERE `model`=%s", (model_filter,))
        else:
            skiType_info= cur.execute("SELECT * FROM `skiType`")

        if skiType_info >0:
            skiType_info = cur.fetchall()

        cur.close()
        return jsonify(skiType_info),201