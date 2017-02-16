#Author Kevin Turner CS21B
#Assignment 4, Amazon order
"""
Amazon order invoice of multiple books, determine least expensive warehouse to
ship from.
"""
instock = {}
outOfStock = {}
shipAvaiByWareHouse = []
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
            'whNorth':2, 'whSouth':1, 'whEast':2, 'whWest':2, 'weight':2.2,
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
            'whNorth':3, 'whSouth':1, 'whEast':2, 'whWest':2, 'weight':1.8,
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

def getShipAvail(invoice):
    for asin in invoice.keys():
        invoiceKey = str(asin) #convert key to string for if statement
        if invoiceKey in book.keys():
            if invoice[asin] <= book[invoiceKey]['whNorth']: #if wh has enough to fulfill book order
                instock.setdefault('whNorth', [])
                instock['whNorth'].append(invoiceKey)
                #print(book[invoiceKey]['title'], ': In Stock,',#print book title and warehouse', '.join(instock))
            else:
                outOfStock.setdefault(invoiceKey, [])
                outOfStock[invoiceKey].append('whNorth')
                #print(book[invoiceKey]['title'], ': Out of Stock,', ', '.join(outOfStock[invoiceKey]))
            if invoice[asin] <= book[invoiceKey]['whSouth']:
                instock.setdefault('whSouth', [])
                instock['whSouth'].append(invoiceKey)
                #print(book[invoiceKey]['title'], ': In Stock,',', '.join(instock))
            else:
                outOfStock.setdefault(invoiceKey, [])
                outOfStock[invoiceKey].append('whSouth')
                #print(book[invoiceKey]['title'], ': Out of Stock,', ', '.join(outOfStock[invoiceKey]))
            if invoice[asin] <= book[invoiceKey]['whEast']:
                instock.setdefault('whEast', [])
                instock['whEast'].append(invoiceKey)
                #print(book[invoiceKey]['title'], ': In Stock,',', '.join(instock))
            else:
                outOfStock.setdefault(invoiceKey, [])
                outOfStock[invoiceKey].append('whEast')
                #print(book[invoiceKey]['title'], ': Out of Stock,', ', '.join(outOfStock[invoiceKey]))
            if invoice.get(asin) <= book[invoiceKey]['whWest']:
                instock.setdefault('whWest', [])
                instock['whWest'].append(invoiceKey)
                #print(book[invoiceKey]['title'], ': In Stock,', ', '.join(instock))
            else:
                outOfStock.setdefault(invoiceKey, [])
                outOfStock[invoiceKey].append('whWest')
                #print(book[invoiceKey]['title'], ': Out of Stock,', ', '.join(outOfStock[invoiceKey]))
        else:
            print('book not found')

getShipAvail(invoice1)

def inStock():
    for k, v in instock.items():
        print('instock loop ', k, len(list(filter(None, v))))
        #print('value ', len(list(filter(None, v))))
        stockKey = k
        if (len(list(filter(None, v)))) == 5:
            shipAvaiByWareHouse.append(stockKey)
    if shipAvaiByWareHouse == []:
        print('Backordered, out of stock')
    else:
        print('ship options: ', ' '.join(shipAvaiByWareHouse))

inStock()


def totalWeight(invoice):
    shipWeight = 0.0
    for asin in invoice.keys():
        invoiceKey = str(asin) #convert key to string for if statement
        if invoiceKey in book.keys():
            shipWeight = shipWeight + book[invoiceKey]['weight']
            #print(book[invoiceKey]['weight'], ' weight: %5.2f%s' % (shipWeight, ' lb'))
    return '%5.2f' % shipWeight

print(totalWeight(invoice1))


def findSize(invoice):
    L = []; W = []; H = []
    for asin in invoice.keys():
        invoiceKey = str(asin) #convert key to string for if statement
        if invoiceKey in book.keys():
            L.append(book[invoiceKey]['length'])
            W.append(book[invoiceKey]['width'])
            H.append(book[invoiceKey]['width'])
    shipSize = max(L) * max(W) * sum(H)
    return '%5.2f' % shipSize

print(findSize(invoice1))


def ShipFactor(total_weight, shipSize, wareHouse=wareHouseShipCostFactor['whWest']):
    print(float(total_weight))
    shipRate = (0.7 * float(total_weight) + 0.3 * float(shipSize)**1.5) * wareHouse
    return shipRate

print(ShipFactor(totalWeight(invoice1), findSize(invoice1), wareHouseShipCostFactor['whNorth']))


test1 = {'whNorth':224.04, 'whSouth':130.3, 'whEast':269.4, 'whWest':242.1}
lowestShipCosttest = min(test1, key = lambda x: test1[x])
print('lowestShipCosttest', lowestShipCosttest)

#shipRate = (0.7 * total_weight + 0.3 * shipSize**1.5) * wareHouseShipCostFactor # needs to be calculated per wh
#use lambda for lowest ship cost

#test run
if __name__ == "__main__":

    """
    Test Case 1: The West coast warehouse must have at least one title not in stock, or not enough
    inventory
    Test Case 2: None of the warehouse has all the books in stock and you have to print a message to
    notify the customer and offer the option to wait for the backordered
    items or choose other
    options(assuming they work, or you can use the tryexcept
    to bypass the nonexisting
    code; don't have
    to do it, just an idea if you want to take an extra step)
    """