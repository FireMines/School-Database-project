from asyncio.windows_events import NULL
from flask import request, jsonify

#                       #
#   Customer endpoint   #
#                       #
def customer_info(mysql):
    
    if request.method == 'GET':
        
        cur=mysql.connection.cursor()

        customer_info= cur.execute("SELECT * FROM `customer`")

        if customer_info >0:
            customer_info = cur.fetchall()

        cur.close()
        return jsonify(customer_info),201

    elif request.method == 'PUT':
        data = request.get_json()
        customer_id=data['customerID']
        start_of_contract=data['startDate']

        cur=mysql.connection.cursor()

        checkIfTeamSkier = cur.execute("SELECT * FROM `teamskier` WHERE `customerID`=%s", (customer_id,))
        checkIfIndivStore = cur.execute("SELECT * FROM `store` WHERE `customerID`=%s", (customer_id,))
        checkIfFranchise = cur.execute("SELECT * FROM `franchise` WHERE `customerID`=%s", (customer_id,))
        checkIfValidID = cur.execute("SELECT * FROM `customer` WHERE `customerID`=%s", (customer_id,))


        print("Skier: 1 Means exists, 0 means does not: ", checkIfTeamSkier)
        print("Store: 1 Means exists, 0 means does not: ", checkIfIndivStore)
        print("Franchise: 1 Means exists, 0 means does not: ", checkIfFranchise)

        print(checkIfValidID)
        if checkIfValidID <= 0:
            return "No customer with that ID!"

        if checkIfTeamSkier and checkIfIndivStore and checkIfFranchise < 0: 
            return "Not in any of its mandatory tables"


        if checkIfTeamSkier > 0:
            name=data['name']
            dob=data['dateOfBirth']
            club=data['club']
            annual_skies=data['annual_skies']

            change_startDate = cur.execute("UPDATE `customer` SET `startDate`=%s WHERE `customerID`=%s",(start_of_contract,customer_id,))
            updateTeamSkier = cur.execute("UPDATE `teamskier` SET `name`=%s, `dateOfBirth`=%s, `club`=%s, `annual_skies`=%s WHERE `customerID`=%s",(name,dob,club,annual_skies,customer_id,))
            mysql.connection.commit()

            customer_info= cur.execute("SELECT * FROM (`customer`, `teamskier`)")

            if customer_info > 0:
                customer_info = cur.fetchall()

            cur.close()
            return jsonify(customer_info),201


        if checkIfIndivStore > 0:
            name=data['name']
            price=data['price']
            address=data['address']

            change_startDate = cur.execute("UPDATE `customer` SET `startDate`=%s WHERE `customerID`=%s",(start_of_contract,customer_id,))
            updateIndivStore = cur.execute("UPDATE `store` SET `name`=%s, `price`=%s, `address`=%s WHERE `customerID`=%s",(name,price,address,customer_id,))
            mysql.connection.commit()

            customer_info= cur.execute("SELECT * FROM (`customer`, `store`)")

            if customer_info > 0:
                customer_info = cur.fetchall()

            cur.close()
            return jsonify(customer_info),201

        if checkIfFranchise > 0:
            name=data['name']
            price=data['buying_price']
            address=data['shipping_address']

            checkIfFranchise_store = cur.execute("SELECT * FROM `franchise_store` WHERE `name`=%s", (name,))

            change_startDate = cur.execute("UPDATE `customer` SET `startDate`=%s WHERE `customerID`=%s",(start_of_contract,customer_id,))
            updateFranchise = cur.execute("UPDATE `franchise` SET `name`=%s, `buying_price`=%s, `shipping_address`=%s WHERE `customerID`=%s",(name,price,address,customer_id,))
            
            if checkIfFranchise_store > 0:
                shipping=data['shipping']
                updateFranchise_Store = cur.execute("UPDATE `franchise_store` SET `shipping`=%s WHERE `customerID`=%s",(shipping,customer_id,))

            
            mysql.connection.commit()

            customer_info= cur.execute("SELECT * FROM (`customer`, `franchise`, `franchise_store`)")

            if customer_info > 0:
                customer_info = cur.fetchall()

            cur.close()
            return jsonify(customer_info),201


    elif request.method == 'POST':
        data = request.get_json()
        customer_id=data['customerID']
        name=data['name']
        dob=data['dateOfBirth']
        club=data['club']
        annual_skies=data['annual_skies']
        startDate=data['startDate']

        cur=mysql.connection.cursor()

        customer_info = cur.execute("SELECT * FROM `customer` WHERE `customerID`=%s", (customer_id,))
        team_skier_info = cur.execute("SELECT * FROM `teamskier` WHERE `customerID`=%s", (customer_id,))



        if customer_info <= 0:
            add_customer_info = cur.execute("INSERT INTO `customer` (`customerID`, `startDate`) VALUES (%s,%s)", (customer_id,startDate))
            mysql.connection.commit()

            add_customer_info = cur.execute("SELECT * FROM `customer`")

            if add_customer_info > 0:
                add_customer_info = cur.fetchall()

            #cur.close()
            #return jsonify(add_customer_info), 201            

            if team_skier_info <= 0:
                change_teamskier_info = cur.execute("INSERT INTO `teamskier` (`customerID`, `name`, `dateOfBirth`, `club`, `annual_skies`) VALUES (%s,%s,%s,%s,%s)", (customer_id, name, dob, club, annual_skies))
                mysql.connection.commit()

                team_skier_info = cur.execute("SELECT * FROM `teamskier`")

                if team_skier_info > 0:
                    team_skier_info1 = cur.fetchall()

                cur.close()
                return jsonify(team_skier_info),201
            else : 
                cur.close()
                return "Team Skier with that customerID already exists"
        else:
            cur.close()
            return "Unable to add a customer, customerID already exists!"

    elif request.method == 'DELETE':
        data = request.get_json()
        customer_id=data['customerID']
        start_of_contract=data['startDate']

        cur=mysql.connection.cursor()

        checkIfTeamSkier = cur.execute("SELECT * FROM `teamskier` WHERE `customerID`=%s", (customer_id,))
        checkIfIndivStore = cur.execute("SELECT * FROM `store` WHERE `customerID`=%s", (customer_id,))
        checkIfFranchise = cur.execute("SELECT * FROM `franchise` WHERE `customerID`=%s", (customer_id,))
        checkIfValidID = cur.execute("SELECT * FROM `customer` WHERE `customerID`=%s", (customer_id,))

        print("Skier: 1 Means exists, 0 means does not: ", checkIfTeamSkier)
        print("Store: 1 Means exists, 0 means does not: ", checkIfIndivStore)
        print("Franchise: 1 Means exists, 0 means does not: ", checkIfFranchise)

        print(checkIfValidID)
        if checkIfValidID <= 0:
            return "No customer with that ID!"

        if checkIfTeamSkier and checkIfIndivStore and checkIfFranchise < 0: 
            return "Not in any of its mandatory tables"


        if checkIfTeamSkier > 0:
            #name=data['name']
            #dob=data['dateOfBirth']
            #club=data['club']
            #annual_skies=data['annual_skies']

            deleteTeamSkier = cur.execute("DELETE FROM `teamskier` WHERE `teamskier`.`customerID` = %s",(customer_id,))
            deleteCustomer = cur.execute("DELETE FROM `customer` WHERE `customer`.`customerID` = %s",(customer_id,))
            mysql.connection.commit()

            customer_info= cur.execute("SELECT * FROM (`customer`, `teamskier`)")

            if customer_info > 0:
                customer_info = cur.fetchall()

            cur.close()
            return jsonify(customer_info),201


        if checkIfIndivStore > 0:
            #name=data['name']
            #price=data['price']
            #address=data['address']

            deleteIndivStore = cur.execute("DELETE FROM `store` WHERE `store`.`customerID` = %s",(customer_id,))
            deleteCustomer = cur.execute("DELETE FROM `customer` WHERE `customer`.`customerID` = %s",(customer_id,))
            mysql.connection.commit()

            customer_info= cur.execute("SELECT * FROM (`customer`, `store`)")

            if customer_info > 0:
                customer_info = cur.fetchall()

            cur.close()
            return jsonify(customer_info),201

        if checkIfFranchise > 0:
            name=data['name']
            #price=data['buying_price']
            #address=data['shipping_address']

            checkIfFranchise_store = cur.execute("SELECT * FROM `franchise_store` WHERE `name`=%s", (name,))

            deleteFranchise = cur.execute("DELETE FROM `franchise` WHERE `franchise`.`customerID` = %s",(customer_id,))
            change_startDate = cur.execute("DELETE FROM `customer` WHERE `customer`.`customerID` = %s",(customer_id,))
            
            if checkIfFranchise_store > 0:
                shipping=data['shipping']
                deleteFranchise_Store = cur.execute("DELETE FROM `franchise_store` WHERE `franchise_store`.`name` = %s",(name,))

            
            mysql.connection.commit()

            customer_info= cur.execute("SELECT * FROM (`customer`, `franchise`, `franchise_store`)")

            if customer_info > 0:
                customer_info = cur.fetchall()

            cur.close()
            return jsonify(customer_info),201


    else:
        print("Method not implemented! Choose between GET, POST, PUT or DELETE instead")