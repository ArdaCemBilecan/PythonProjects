import random

# Ağaçlı yapıda eğer eleman sayımız az ise işimize yara lakin sayı arttıkça rec fonk
    # çalışması da artar bu da sürekli hesapladığımız değeri bir daha hesaplatır.
    # Yani Boşa zaman ve işlem kaybı oluşur. Bunu önemek için bir memorable oluşturacağız.

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

def maxValue(toConsider,avail,memo={}):
    if (len(toConsider),avail)in memo:
        result = memo[(len(toConsider),avail)]
        #memoda varsa direk memodakini return et yoksa aşağıdaki işlemleri yap return et
    elif toConsider == [] or avail == 0:
        result = (0,())
        return result
    elif toConsider[0].getWeight()>avail:
        result= maxValue(toConsider[1:],avail,memo)
     
    else:
        nextItem = toConsider[0]
        withVal,withToTake = maxValue(toConsider[1:],avail-nextItem.getWeight(),memo)
        withVal += nextItem.getValue()
        withoutVal,withoutToTake = maxValue(toConsider[1:],avail,memo)
        
        if withVal > withoutVal:
            result = (withVal,withToTake+(nextItem,))
        else:
            result = (withoutVal,withoutToTake)
            
    memo[(len(toConsider),avail)] = result       
    return result


    
def buildManyItems(numItems,maxVal,maxWeight):
     items=[]
     for i in range(numItems):
         items.append(Item(str(i),
                      random.randint(1,maxVal),
                      random.randint(1,maxWeight)))
    
     return items


def bigTest(numItems):
    items = buildManyItems(numItems,10,10)
    val,taken = maxValue(items,40)
    print("Item Taken")
    for item in taken:
        print(item)
    print("Total value of item taken = ",val)
    
   

bigTest(20)  

    
    
    
    
    
    



  