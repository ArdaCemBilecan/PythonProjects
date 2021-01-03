from pprint import pprint as pp
from itertools import chain,combinations

def genPowerSet(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))

class Item(object):
    def __init__(self,n,v,w):
        self.name = n
        self.value = v
        self.weight = w
    
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    
    def __str__(self):
        result = '< '+self.name + ' , ' + str(self.value)\
                    +' , ' + str(self.weight) + '>'
        return result
    
    
def value(item):
    return item.getValue()

def weightInverse(item):
    return 1 / item.getWeight()

def density(item):
    return item.getValue()/item.getWeight()


def greedy (items,maxWeight,keyFunction):
    itemscopy = sorted(items,key=keyFunction,reverse = True)
    result=[]
    totalValue,totalWeight = 0,0
    for i in range(len(itemscopy)):
        if (totalWeight + itemscopy[i].getWeight()) <=maxWeight:
            result.append(itemscopy[i])
            totalWeight+=itemscopy[i].getWeight()
            totalValue+= itemscopy[i].getValue()
    return (result , totalValue)


def buildItems(names,values,weights):
#    names = ['clock','painting','radio','vase','book','computer']
#    values = [175,90,20,50,10,200]
#    weights=[10,9,4,2,1,20]
    Items=[]
    for i in range (len(values)):
        Items.append(Item(names[i],values[i],weights[i]))
    return Items



def testGreedy(items,maxWeight,keyFunction):
    taken,val = greedy(items,maxWeight,keyFunction)
    print(val)
    for item in taken:
        print("testGreedy Item: ",item)


def testGreedys(maxWeight,names,values,weights):
    items = buildItems(names,values,weights)
    
    testGreedy(items,maxWeight,value)
    
    testGreedy(items,maxWeight,weightInverse)
    
    testGreedy(items,maxWeight,density)
    
def chooseBest(pset,maxWeight,getVal,getWeight):
    bestVal =0.0
    bestSet = None
    for items in pset:
         itemsVal =0.0
         itemsWeight = 0.0
         for item in items:
            itemsVal +=getVal(item)
            itemsWeight+=getWeight(item)
         if itemsWeight<=maxWeight and itemsVal > bestVal:
            bestVal = itemsVal
            bestSet = items
    return (bestSet,bestVal)



def testBest(maxWeight,names,values,weights):
    items = buildItems(names,values,weights)
    pset = set(genPowerSet(items))
    taken,val = chooseBest(pset,maxWeight,Item.getValue,Item.getWeight)
    print("Total Value of items: ",val)
    for item in taken:
        print("testBest Item: ",item)


# Main yeri
# Videodaki veriler
maxWeight=20
names = ['clock','painting','radio','vase','book','computer']
values = [175,90,20,50,10,200]
weights=[10,9,4,2,1,20]    
testBest(maxWeight,names,values,weights)
testGreedys(maxWeight,names,values,weights)
            
#Deneme 1 Verileri:
maxWeight1=20
names1 = ['Laptop','Kol Saati','TV','Telefon']
values1=[200,100,150,125]
weights1=[7,4,12,8]
testBest(maxWeight,names1,values1,weights1)
testGreedys(maxWeight1,names1,values1,weights1)

# Deneme 2 Verileri

testBest(25,['elma','armut','ceviz','patlıcan','karpuz'],[20,30,25,40,35],[2,5,4,3,10])
testGreedys(25,['elma','armut','ceviz','patlıcan','karpuz'],[20,30,25,40,35],[2,5,4,3,10]) 


