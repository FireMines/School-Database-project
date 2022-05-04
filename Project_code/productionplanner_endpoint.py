from asyncio.windows_events import NULL
from flask import request, jsonify
import consts


#                                   #
#   Production planner endpoints    #
#                                   #
def production_planner():

    #           #
    #   GET     #
    #           #
    if request.method == 'GET':
        data=request.get_json()
        
        cur=consts.mysql.connection.cursor()

        if data:
            plan_id =data['planID']
            plan_info= cur.execute("SELECT * FROM `productionplanreference` INNER JOIN `productionplan` ON `productionplanreference`.`planID`=`productionplan`.`planID` WHERE `productionplan`.`planID`=%s", (plan_id,))
        else:
            plan_info= cur.execute("SELECT * FROM `productionplan`")

        if plan_info >0:
            plan_info = cur.fetchall()

        cur.close()
        return jsonify(plan_info),201

    #           #
    #   POST    #
    #           #
    elif request.method == 'POST':
        data = request.get_json()
        plan_id = data['planID']
        employee_id = data['employeeID']
        start_date=data['startDate']
        end_date=data['endDate']
        referneces=data['planReferences']

        cur=consts.mysql.connection.cursor()

        plan_info= cur.execute("SELECT * FROM `productionplan` WHERE `planID`=%s", (plan_id,))

        if plan_info <=0:
            
            change_state = cur.execute("INSERT INTO `productionplan` (`employeeNumber`, `planID`, `startDate`, `endDate`) VALUES (%s,%s,%s,%s)", (employee_id, plan_id, start_date, end_date,))
            consts.mysql.connection.commit()

            for ref in referneces:
                ref_id=ref['referenceID']
                product_id=ref['productID']
                quantity=ref['quantity']

                change_state== cur.execute("INSERT INTO `productionplanreference` (`planID`, `productID`, `ReferenceID`, `Quantity`) VALUES (%s,%s,%s,%s)", (plan_id, product_id, ref_id, quantity,))
                consts.mysql.connection.commit()

            plan_info= cur.execute("SELECT * FROM `productionplanreference` INNER JOIN `productionplan` ON `productionplanreference`.`planID`=`productionplan`.`planID` WHERE `productionplan`.`planID`=%s", (plan_id,))

            if plan_info >0:
                plan_info = cur.fetchall()

            cur.close()
            return jsonify(plan_info),201
        else :
            cur.close()
            return "This plan already exist in the database",400

    else:
        print("Method not implemented! Choose between GET or POST instead")

