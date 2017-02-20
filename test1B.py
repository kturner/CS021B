#Author Kevin Turner CS21B
#Test stuff for class

wareHouseShipCostFactor={'whNorth':1.8,'whSouth':2.1,'whEast':2.5,'whWest':1.0}

book = {'1491946008':
            {'title':'Fluent Python', 'price':39.99,
            'whNorth':4, 'whSouth':2, 'whEast':2, 'whWest':12, 'weight':2.8,
            'length':7, 'width':9.2, 'height':1.5},
        '1449357016':
            {'title':'Python Pocket Reference',
             'price':10.25, 'whNorth':3, 'whSouth':3, 'whEast':0, 'whWest':5,
             'weight':0.35, 'length':4.2, 'width':7.0, 'height':0.5},
        '1785289721':
            {'title':'Mastering Python', 'price':39.99, #zero stock
            'whNorth':2, 'whSouth':3, 'whEast':2, 'whWest':2, 'weight':2.2,
            'length':7.5,  'width':9.2,  'height':1.1},
        '615291805':
            {'title':'Design and Construction of Tube Guitar amplifiers',
             'price':23.18, 'whNorth':4, 'whSouth':2, 'whEast':3, 'whWest':7,
             'weight':0.7, 'length':6.9, 'width':10.0, 'height':0.6},
        '976982242':
            {'title':'Vacuum Tube Circuit Design: Guitar Amplifiers Power Amps',
             'price':49.95, 'whNorth':6, 'whSouth':3, 'whEast':0, 'whWest':5,
             'weight':1.7, 'length':7.4, 'width':9.1, 'height':1.1},
        '6197258048':
           {'title':'The Ultimate Solar Power Design:Less Theory More Practice',
             'price':15.97, 'whNorth':0, 'whSouth':0, 'whEast':0, 'whWest':0,
             'weight':0.9, 'length':6,  'width':9.0,  'height':0.5},
        '321967607':
            {'title':'Programming on Objective-C (6th Edition)', 'price':37.24,
            'whNorth':3, 'whSouth':1, 'whEast':4, 'whWest':2, 'weight':1.8,
            'length':7,  'width':9.0,  'height':1.4}
        }

invoice1 = {'1491946008': 4, '1449357016': 3, '1785289721': 1,
            '615291805': 2, '976982242': 1}

invoice2 = {'1785289721': 2, '1449357016': 1, '1491946008': 1,
            '321967607': 3,'976982242': 6}

invoice3 = {'1785289721': 1, '615291805': 1, '1491946008': 1,
            '6197258048': 3, '321967607': 2} #zero available for 6197258048

invoice4 = {'1491946008': 2, '615291805': 2, '1785289721': 1,
            '321967607': 1, '976982242': 1}

invoice5 = {'1785289721': 3, '615291805': 1, '1491946008': 5,
            '976982242': 6, '321967607': 4} #not enough inventory from any one warehouse

def totalWeight(asin, itemWeight = []):
    itemWeight.append(book[asin]['weight'])
    shipWeight = sum(itemWeight)
    return float('%5.2f' % shipWeight)


def getShipAvail(invoice):
    instockWarehouse = {}; outOfStock = {}
    shipAvaiByWareHouse = []; warehouseOptions = []
    L = []; W = []; H = []
    for asin in invoice.keys():
        shipWeight = totalWeight(asin)
        L.append(book[asin]['length'])
        W.append(book[asin]['width'])
        H.append(book[asin]['height'])
        if str(asin) in book.keys():
            if invoice[asin] <= book[str(asin)]['whNorth']: #if wh has enough to fulfill book order
                instockWarehouse.setdefault('whNorth', [])
                instockWarehouse['whNorth'].append(str(asin))
                #print(book[str(asin)]['title'], ': In Stock,',', '.join(instockWarehouse))#print book title and warehouse
                #print('invoice ship: ', asin)
            else:
                outOfStock.setdefault(str(asin), [])
                outOfStock[str(asin)].append('whNorth')
                #print(book[str(asin)]['title'], ': Out of Stock,', ', '.join(outOfStock[str(asin)]))
            if invoice[asin] <= book[str(asin)]['whSouth']:
                instockWarehouse.setdefault('whSouth', [])
                instockWarehouse['whSouth'].append(str(asin))
                #print(book[str(asin)]['title'], ': In Stock,',', '.join(instockWarehouse))
            else:
                outOfStock.setdefault(str(asin), [])
                outOfStock[str(asin)].append('whSouth')
                #print(book[str(asin)]['title'], ': Out of Stock,', ', '.join(outOfStock[str(asin)]))
            if invoice[asin] <= book[str(asin)]['whEast']:
                instockWarehouse.setdefault('whEast', [])
                instockWarehouse['whEast'].append(str(asin))
                #print(book[str(asin)]['title'], ': In Stock,',', '.join(instockWarehouse))
            else:
                outOfStock.setdefault(str(asin), [])
                outOfStock[str(asin)].append('whEast')
                #print(book[str(asin)]['title'], ': Out of Stock,', ', '.join(outOfStock[str(asin)]))
            if invoice.get(asin) <= book[str(asin)]['whWest']:
                instockWarehouse.setdefault('whWest', [])
                instockWarehouse['whWest'].append(str(asin))
                #print(book[str(asin)]['title'], ': In Stock,', ', '.join(instockWarehouse))
            else:
                outOfStock.setdefault(str(asin), [])
                outOfStock[str(asin)].append('whWest')
                #print(book[str(asin)]['title'], ': Out of Stock,', ', '.join(outOfStock[str(asin)]))
        else:
            print('book not found')

    for k, v in instockWarehouse.items():
        stockKey = k
        if (len(list(filter(None, v)))) == 5:  # adds to shipAvaiByWareHouse if full order avail from warehouse
            shipAvaiByWareHouse.append(stockKey)
        if (len(list(filter(None, v))) < 5 and len(list(filter(None, v)))) > 0:  # adds to shipWarehouseOption if partial order at warehouse
            warehouseOptions.append(stockKey)
    shipSize = '%5.2f' % (max(L) * max(W) * sum(H))
    return shipAvaiByWareHouse, shipWeight, float(shipSize)

shipByWareHouse, shipWeightTot, shipSizeTot = getShipAvail(invoice4)

#calculates shipfactor for each warehouse
def ShipFactor(wareHouseShipCostFactor, shipByWareHouse, shipWeightTot,
               shipSizeTot):
    whShipRates = {}
    for wh in range(len(shipByWareHouse)):
        shipRate = ((0.7 * float(shipWeightTot) +
                    ( 0.3 * (shipSizeTot) ** 1.5))) * \
                   wareHouseShipCostFactor[shipByWareHouse[wh]]
        whShipRates[shipByWareHouse[wh]] = float('%8.2f' % shipRate)
        lowestShipCosttest = min(whShipRates, key=lambda x: whShipRates[x])
    return whShipRates, lowestShipCosttest

def printInvoiceDetails(invoice):
    invoiceDetails = {}
    for key, value in book.items():
        if key in invoice:
            invoiceDetails[key] = value
    return invoiceDetails
details = printInvoiceDetails(invoice4)
print('Details: ', details)

#save shipfactor as local var


ShipCostF, lowestCostWarehouse = ShipFactor(wareHouseShipCostFactor,
                                    shipByWareHouse, shipWeightTot, shipSizeTot)

print('Warehouse with lowest shipping cost: ', lowestCostWarehouse )
print('All warehouse options for shipping single source order: ', ShipCostF)
