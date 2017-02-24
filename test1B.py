#Author Kevin Turner CS21B
#Test stuff for class

wareHouseShipCostFactor={'whWest':1.0, 'whNorth':1.8,'whSouth':2.1,'whEast':2.5}


book = {'1491946008':
            {'title':'Fluent Python', 'author': 'Luciano Ramalho','price':39.99,
            'whWest':12, 'whNorth':4, 'whSouth':2, 'whEast':2,  'weight':2.8,
            'length':7, 'width':9.2, 'height':1.5},
        '1449357016':
            {'title':'Python Pocket Reference', 'author': 'Mark Lutz',
             'price':10.25, 'whWest':5, 'whNorth':3, 'whSouth':3, 'whEast':1,
             'weight':0.35, 'length':4.2, 'width':7.0, 'height':0.5},
        '1785289721':
            {'title':'Mastering Python', 'author': 'Rick van Hattem',
             'price':39.99, #zero stock
             'whWest':2, 'whNorth':4, 'whSouth':3, 'whEast':2, 'weight':2.2,
            'length':7.5,  'width':9.2,  'height':1.1},
        '615291805':
            {'title':'Design and Construction of Tube Guitar amplifiers',
             'author': 'Robert C. Megantz and Ken Leyva',
             'price':23.18, 'whWest':7, 'whNorth':4, 'whSouth':2, 'whEast':3,
             'weight':0.7, 'length':6.9, 'width':10.0, 'height':0.6},
        '976982242':
            {'title':'Vacuum Tube Circuit Design: Guitar Amplifiers Power Amps',
             'author': 'Richard Kuehnel', 'price':49.95, 'whWest':5,
             'whNorth':6, 'whSouth':3, 'whEast':1, 'weight':1.7, 'length':7.4,
             'width':9.1, 'height':1.1},
        '6197258048':
           {'title':'The Ultimate Solar Power Design:Less Theory More Practice',
             'author': ' Lacho Pop MSE and Dimi Avram MSE', 'price':15.97,
            'whWest':1, 'whNorth':2, 'whSouth':1, 'whEast':1,
             'weight':0.9, 'length':6,  'width':9.0,  'height':0.5},
        '321967607':
            {'title':'Programming on Objective-C (6th Edition)',
             'author': 'Stephen G. Kochan', 'price':37.24,
            'whWest':4, 'whNorth':3, 'whSouth':1, 'whEast':4, 'weight':1.8,
            'length':7,  'width':9.0,  'height':1.4}
        }

invoice1 = {'1491946008': 4, '1449357016': 3, '1785289721': 1,
            '615291805': 2, '976982242': 2}
invoice2 = {'1785289721': 2, '1449357016': 1, '1491946008': 1,
            '321967607': 3,'976982242': 6}
invoice3 = {'1785289721': 1, '615291805': 1, '1491946008': 1,
            '6197258048': 3, '321967607': 2} #zero available for 6197258048
invoice4 = {'1491946008': 2, '615291805': 2, '1785289721': 1,
            '321967607': 1, '976982242': 1}
invoice5 = {'1785289721': 4, '615291805': 5, '1491946008': 5,
            '976982242': 6, '321967607': 4} #not enough inventory from any one warehouse

def totalWeight(asin, itemWeight = []):
    """
    Sums the weight of all the books in the order
    This function is called inside of shipAvaiByWareHouse
    :param asin: Amazon item ID
    :param itemWeight: Empty list that will be populated with the wieght of
    each book.
    :return: Total weight for all books in order
    """
    itemWeight.append(book[asin]['weight'])
    shipWeight = sum(itemWeight)
    return float('%5.2f' % shipWeight)

def totalCost(invoice):
    """
    Multiplies the price of each book by quanitiy each book then sums the
    product of all the books.
    :param invoice: Customer invoice consisting of an ASIN number and quantity
    :return: Calculated cost of all the books ordered.
    """
    cost = []
    for asin in invoice.keys():
        tempCost = book[asin]['price']
        tempQt = invoice[asin]
        cost.append(tempCost * tempQt)
    totalCost = sum(cost)
    return totalCost

def getShipAvail(invoice):
    """
    GetShipAvail takes the order invoice as input (which consist of an ASIN
     number to identify each book ordered and the quanity of each book ordered).
     Calculates the size of the order to ship and saves the weight of each book
     for calculation.
     Compares the book inventory from each warehouse to the order quantity and
     if the warehouse has enough inventory, then that book gets added to the
     instockWarehouse dictionary. If the warehouse has insufficient inventory,
     then the book gets added to the insufficientStock dictionary. If no
     inventory exists at a warehouse, then it is added to the  outOfStock
     dictionary. All of these dictionaries include the warehouse and the
     ASIN number.
     Next it iterates through the instockWarehouse and checks to see if all
     the books from the order have sufficient stock to fill the order. If so,
     then the warehouse is added to the shipAvaiByWareHouse list for an option
     to ship from a single source. If there is not enough inventory from any
     one warehouse, the warehouse and ASIN are added to the warehouseOptions
     dictionary.
     :param invoice: Customer invoice consisting of an ASIN number and quantity
     :return:
    """
    instockWarehouse = {}; insufficientStock = {}
    outOfStock = {}; warehouseOptions = {}; shipAvailOptions = {}
    shipAvaiByWareHouse = [];
    tempInvoice = invoice
    L = []; W = []; H = []
    for asin in invoice.keys():
        shipWeight = totalWeight(asin)
        L.append(book[asin]['length'])
        W.append(book[asin]['width'])
        H.append(book[asin]['height'])
        if str(asin) in book.keys():
            if invoice.get(asin) <= book[str(asin)]['whWest']:
                instockWarehouse.setdefault('whWest', [])
                instockWarehouse['whWest'].append(str(asin))
            elif invoice[asin] > book[str(asin)]['whWest']:
                insufficientStock.setdefault('whWest', [])
                insufficientStock['whWest'].append(str(asin))
            elif book[str(asin)]['whWest'] == 0:
                outOfStock.setdefault('whWest', [])
                outOfStock['whWest'].append(str(asin))

            if invoice[asin] <= book[str(asin)]['whNorth']: #if wh has enough to fulfill book order
                instockWarehouse.setdefault('whNorth', [])
                instockWarehouse['whNorth'].append(str(asin))
            elif invoice[asin] > book[str(asin)]['whNorth']:
                insufficientStock.setdefault('whNorth', []) #this warehouse is low on stock on book
                insufficientStock['whNorth'].append(str(asin))
            elif book[str(asin)]['whNorth'] == 0:
                outOfStock.setdefault('whNorth', []) #this warehouse is out of stock on book
                outOfStock['whNorth'].append(str(asin))

            if invoice[asin] <= book[str(asin)]['whSouth']:
                instockWarehouse.setdefault('whSouth', [])
                instockWarehouse['whSouth'].append(str(asin))
            elif invoice[asin] > book[str(asin)]['whSouth']:
                insufficientStock.setdefault('whSouth', [])
                insufficientStock['whSouth'].append(str(asin))
            elif book[str(asin)]['whSouth'] == 0:
                outOfStock.setdefault('whSouth', [])
                outOfStock['whSouth'].append(str(asin))

            if invoice[asin] <= book[str(asin)]['whEast']:
                instockWarehouse.setdefault('whEast', [])
                instockWarehouse['whEast'].append(str(asin))
            elif invoice[asin] > book[str(asin)]['whEast']:
                insufficientStock.setdefault('whEast', [])
                insufficientStock['whEast'].append(str(asin))
            elif book[str(asin)]['whEast'] == 0:
                outOfStock.setdefault('whEast', [])
                outOfStock['whEast'].append(str(asin))
        else:
            print('book not found')
    #print('insufficientStock', insufficientStock)
    #print('inStock', instockWarehouse)
    #print('outOfStock', outOfStock)
    i = 0
    for k, v in instockWarehouse.items():
        # adds warehouse to shipAvaiByWareHouse if full order avail from warehouse
        if (len(list(filter(None, v)))) == len(invoice):
            shipAvaiByWareHouse.append(str(k))
        elif shipAvaiByWareHouse == []:
            warehouseOptions[k] = v
    if warehouseOptions != {}:
        if 'whWest' in warehouseOptions:
            for value in warehouseOptions['whWest']:
                if value in tempInvoice:
                    shipAvailOptions.setdefault('whWest', [])
                    shipAvailOptions['whWest'].append(str(value))
                    del tempInvoice[value]
        if 'whNorth' in warehouseOptions:
            for value in warehouseOptions['whNorth']:
                if value in tempInvoice:
                    shipAvailOptions.setdefault('whNorth', [])
                    shipAvailOptions['whNorth'].append(str(value))
                    del tempInvoice[value]
        if 'whSouth' in warehouseOptions:
            for value in warehouseOptions['whSouth']:
                if value in tempInvoice:
                    shipAvailOptions.setdefault('whSouth', [])
                    shipAvailOptions['whSouth'].append(str(value))
                    del tempInvoice[value]
        if 'whEast' in warehouseOptions:
            for value in warehouseOptions['whEast']:
                if value in tempInvoice:
                    shipAvailOptions.setdefault('whEast', [])
                    shipAvailOptions['whEast'].append(str(value))
                    del tempInvoice[value]

        print('Best available shipping option from multiple sources: ', end='' )
        for key, value in shipAvailOptions.items():
            print(key, value)
        if tempInvoice != {}:
            for key in tempInvoice:
                print('Out of Stock: ', book[key]['title'])
        shipSize = '%5.2f' % (max(L) * max(W) * sum(H))
    if shipAvaiByWareHouse != []:
        print('shipAvaiByWareHouse', shipAvaiByWareHouse)
    shipSize = '%5.2f' % (max(L) * max(W) * sum(H))
    return shipAvaiByWareHouse, insufficientStock, shipAvailOptions, shipWeight, float(shipSize)

def shipFactor(wareHouseShipCostFactor, shipByWareHouse, shipWeightTot,shipSizeTot):
    """
    calculates shipfactor for each warehouse and determines the warehouse with
    the lowest shipping cost.
    :param wareHouseShipCostFactor: A factor to weigh cost of shipping per
    warehouse location.
    :param shipByWareHouse:
    :param shipWeightTot: Shipping weight of all books in the order
    :param shipSizeTot: (The length of the longest book) * (the width of the
    widest book) * (the sum of the heights of all the books)
    :return: whShipRates is the cost number associated with the shipRate and the
    cost factor. lowestShipCost returns the warehouse with the lowest shipping
    cost.
    """
    whShipRates = {}
    for wh in range(len(shipByWareHouse)):
        shipRate = ((0.7 * float(shipWeightTot) +
                    ( 0.3 * (shipSizeTot) ** 1.5))) * \
                   wareHouseShipCostFactor[shipByWareHouse[wh]]
        whShipRates[shipByWareHouse[wh]] = float('%8.2f' % shipRate)
        lowestShipCost = min(whShipRates, key=lambda x: whShipRates[x])
    return whShipRates, lowestShipCost

def printInvoiceDetails(invoice):
    """
    Prints specified details for books in invoice
    :param invoice: Customer invoice consisting of an ASIN number and quantity
    :return: returns specific details for the books in the invoice. Name of book,
    author, price and total price.
    """
    print('Invoice Details:')
    for key, value in book.items():
        if key in invoice:
            print(book[str(key)]['title'], ' by ', book[str(key)]['author'] ,
                  ' $',book[str(key)]['price'])
    return print('total price $', '%5.2f' % totalCost(invoice), '\n')

def orderDetails(invoice):
    """
    :param invoice:Customer invoice consisting of an ASIN number and quantity
    :return: all the details of the books in the invoice.
    """
    details = {}
    for key, value in book.items():
        if key in invoice:
            details[key] = value
    return details

def amazonOrder(invoice):
    """
    Takes invoice as a parameter and passes it to all the functions that require
    invoice. Calls functions: getShipAvail, shipFactor and orderDetails.
    prints results
    :param invoice: Customer invoice consisting of an ASIN number and quantity
    :return:
    """
    shipByWareHouse, insufficientStock, shipAvailOptions, shipWeightTot, shipSizeTot \
        = getShipAvail(invoice)
    totalCost(invoice)
    if shipByWareHouse != []:
        ShipCostF, lowestCostWarehouse = shipFactor(wareHouseShipCostFactor,
                                        shipByWareHouse, shipWeightTot, shipSizeTot)
        print('Warehouse with lowest shipping cost: ', lowestCostWarehouse, '\n')
        print('All warehouse options for shipping single source order: ',
              ShipCostF, '\n')
    elif shipByWareHouse == [] and shipAvailOptions != {}:
        print('shipAvailOptions', shipAvailOptions)
    #elif outOfStock != {}:
        #print('Out of Stock', outOfStock)
        #print('insufficientStock', insufficientStock)
    #printInvoiceDetails(invoice)
    details = orderDetails(invoice)
    #print('full invoice details ', details)

amazonOrder(invoice1)