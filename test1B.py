#Author Kevin Turner CS21B
#Test stuff for class®

#shipAvaiByWareHouse = []
#shipWarehouseOption = []
wareHouseShipCostFactor = {'whNorth':1.8,'whSouth':2.1,'whEast':2.5,'whWest':1}

book = {'1491946008':
            {'title':'Fluent Python', 'price':39.99,
            'whNorth':4, 'whSouth':2, 'whEast':2, 'whWest':12, 'weight':2.8,
            'length':7, 'width':1.5, 'height':9.2},
        '1449357016':
            {'title':'Python Pocket Reference',
             'price':10.25, 'whNorth':3, 'whSouth':3, 'whEast':0, 'whWest':5,
             'weight':0.35, 'length':4.2, 'width':0.5, 'height':7},
        '1785289721':
            {'title':'Mastering Python', 'price':39.99, #zero stock
            'whNorth':2, 'whSouth':3, 'whEast':2, 'whWest':2, 'weight':2.2,
            'length':7.5,  'width':1.1,  'height':9.2},
        '615291805':
            {'title':'Design and Construction of Tube Guitar amplifiers',
             'price':23.18, 'whNorth':4, 'whSouth':2, 'whEast':3, 'whWest':7,
             'weight':0.7, 'length':6.9, 'width':0.6, 'height':10},
        '976982242':
            {'title':'Vacuum Tube Circuit Design: Guitar Amplifiers Power Amps',
             'price':49.95, 'whNorth':6, 'whSouth':3, 'whEast':0, 'whWest':5,
             'weight':1.7, 'length':7.4, 'width':1.1, 'height':9.1},
        '6197258048':
           {'title':'The Ultimate Solar Power Design:Less Theory More Practice',
             'price':15.97, 'whNorth':0, 'whSouth':0, 'whEast':0, 'whWest':0,
             'weight':0.9, 'length':6,  'width':0.5,  'height':9.0},
        '321967607':
            {'title':'Programming on Objective-C (6th Edition)', 'price':37.24,
            'whNorth':3, 'whSouth':1, 'whEast':4, 'whWest':2, 'weight':1.8,
            'length':7,  'width':1.4,  'height':9.0}
        }

invoice1 = {'1491946008': 4, '1449357016': 3, '1785289721': 1,
            '615291805': 2, '976982242': 1}

invoice2 = {'1785289721': 2, '1449357016': 1, '1491946008': 1,
            '321967607': 3,'976982242': 1}

invoice3 = {'1785289721': 1, '615291805': 1, '1491946008': 1,
            '6197258048': 3, '321967607': 2} #zero available for 6197258048

invoice4 = {'1491946008': 2, '615291805': 2, '1785289721': 1,
            '321967607': 1, '976982242': 1}

invoice5 = {'1785289721': 3, '615291805': 1, '1491946008': 5,
            '976982242': 6, '321967607': 4} #not enothgh inventory from any one warehouse

def totalWeight(asin, itemWeight = []):
    itemWeight.append(book[asin]['weight'])
    shipWeight = sum(itemWeight)
    print('%5.2f%s' % (shipWeight, ' lb'))
    return '%5.2f' % shipWeight

def findSize(asin, L = [], W = [], H = []):
    #L = []; W = []; H = []
    L.append(book[asin]['length'])
    W.append(book[asin]['width'])
    H.append(book[asin]['height'])
    shipSize = max(L) * max(W) * sum(H)
    print('shipSize ', '%5.2f' % shipSize)
    return '%5.2f' % shipSize

#creates two list of warehouses, 1 with full order and 1 with partial order,
# uses instock list that is generated from getShipAvail()
def shipAvaiByWareHouse(invoice,shipAvaiByWareHouse = [], shipWarehouseOption = []):
    for k, v in instockWarehouse.items():
        #print('instockWarehouse loop ', k, len(list(filter(None, v))))
        #print('value ', len(list(filter(None, v))))
        stockKey = k
        if (len(list(filter(None, v)))) == 5: #adds to shipAvaiByWareHouse if full order avail from warehouse
            shipAvaiByWareHouse.append(stockKey)
            #print('warehouse: ', shipAvaiByWareHouse)
        if (len(list(filter(None, v))) < 5 and len(list(filter(None, v)))) > 0: #adds to shipWarehouseOption if partial order at warehouse
            shipWarehouseOption.append(stockKey)
            #print('Option ', shipWarehouseOption)

def shipOptions(invoice, shipAvaiByWareHouse = [], shipWarehouseOption = []):
    if shipAvaiByWareHouse != []:
        return None
    elif shipAvaiByWareHouse == [] and shipWarehouseOption == [] and outOfStock != None: # nothing in stock at any warehouse
        return print('Backordered, out of stock')
    elif shipAvaiByWareHouse == [] and shipWarehouseOption != []:#partial order avail
        #print('Availble by multiple shipments only:',' '.join(shipWarehouseOption))
        return print('split order, cannot be shipped from one location')

def getShipAvail(invoice, outOfStock = {}, **instockWarehouse):
    for asin in invoice.keys():
        totalWeight(asin)
        findSize(asin)
        invoiceKey = str(asin) #convert key to string for if statement
        if invoiceKey in book.keys():
            if invoice[asin] <= book[invoiceKey]['whNorth']: #if wh has enough to fulfill book order
                instockWarehouse.setdefault('whNorth', [])
                instockWarehouse['whNorth'].append(invoiceKey)
                #print(book[invoiceKey]['title'], ': In Stock,',', '.join(instockWarehouse))#print book title and warehouse
                #print('invoice ship: ', asin)
            else:
                outOfStock.setdefault(invoiceKey, [])
                outOfStock[invoiceKey].append('whNorth')
                #print(book[invoiceKey]['title'], ': Out of Stock,', ', '.join(outOfStock[invoiceKey]))
            if invoice[asin] <= book[invoiceKey]['whSouth']:
                instockWarehouse.setdefault('whSouth', [])
                instockWarehouse['whSouth'].append(invoiceKey)
                #print(book[invoiceKey]['title'], ': In Stock,',', '.join(instockWarehouse))
            else:
                outOfStock.setdefault(invoiceKey, [])
                outOfStock[invoiceKey].append('whSouth')
                #print(book[invoiceKey]['title'], ': Out of Stock,', ', '.join(outOfStock[invoiceKey]))
            if invoice[asin] <= book[invoiceKey]['whEast']:
                instockWarehouse.setdefault('whEast', [])
                instockWarehouse['whEast'].append(invoiceKey)
                #print(book[invoiceKey]['title'], ': In Stock,',', '.join(instockWarehouse))
            else:
                outOfStock.setdefault(invoiceKey, [])
                outOfStock[invoiceKey].append('whEast')
                #print(book[invoiceKey]['title'], ': Out of Stock,', ', '.join(outOfStock[invoiceKey]))
            if invoice.get(asin) <= book[invoiceKey]['whWest']:
                instockWarehouse.setdefault('whWest', [])
                instockWarehouse['whWest'].append(invoiceKey)
                #print(book[invoiceKey]['title'], ': In Stock,', ', '.join(instockWarehouse))
            else:
                outOfStock.setdefault(invoiceKey, [])
                outOfStock[invoiceKey].append('whWest')
                #print(book[invoiceKey]['title'], ': Out of Stock,', ', '.join(outOfStock[invoiceKey]))
        else:
            print('book not found')

    return instockWarehouse, outOfStock



(instockWarehouse, outOfStock) = getShipAvail(invoice1)

print(shipAvaiByWareHouse(invoice1))


#dont need a function here and warehouse is hardwired
def ShipFactor(total_weight, shipSize, wareHouse=wareHouseShipCostFactor['whWest']):
    #print(float(total_weight))
    shipRate = (0.7 * float(total_weight) + 0.3 * float(shipSize)**1.5) * wareHouse
    return shipRate

#print('shipfactor: ', ShipFactor(totalWeight(invoice1), findSize(invoice1), wareHouseShipCostFactor['whNorth']))

#replace test1 with instockWarehouse loop for warehouse
test1 = {'whNorth':224.04, 'whSouth':130.3, 'whEast':269.4, 'whWest':242.1}
lowestShipCosttest = min(test1, key = lambda x: test1[x])
#print('lowestShipCosttest', lowestShipCosttest)


#test run
if __name__ == "__main__":
    """
    invoice1 = {'1491946008': 4, '1449357016': 3, '1785289721': 1,
            '615291805': 2, '976982242': 1}

    invoice2 = {'1785289721': 2, '1449357016': 1, '1491946008': 1,
                '321967607': 3,'976982242': 1}

    invoice3 = {'1785289721': 1, '615291805': 1, '1491946008': 1,
                '6197258048': 3, '321967607': 2} #zero available for 6197258048

    invoice4 = {'1491946008': 2, '615291805': 2, '1785289721': 1,
                '321967607': 1, '976982242': 1}

    invoice5 = {'1785289721': 3, '615291805': 1, '1491946008': 5,
                '976982242': 6, '321967607': 4} #not enothgh inventory from any one warehouse
    """
