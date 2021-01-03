import random

def createList(n=10,minValue=-5,maxValue=5):
    numbers=[]
    for i in range(n):
        numbers.append(random.randint(minValue,maxValue))
    return numbers

def bubbleSort(list_1):
    for i in range(len(list_1)-1):
        for j in range(len(list_1)-1):
            if list_1[j]>list_1[j+1]:
                temp = list_1[j]
                list_1[j]=list_1[j+1]
                list_1[j+1]=temp
                
                
def normalHistogramFunction(list_1):
    Dic = dict()   # or Dic = {}  same things
    for item in list_1:
        if item in Dic:
            Dic[item] = Dic[item]+1
        else:
            Dic[item] = 1
    return Dic


def histogram_With_ListOf_Tuples(list_1):
    dicList = []
    for i in range(len(list_1)):
        s = False
        for j in range(len(dicList)):
            if list_1[i]==dicList[j][0]:
                dicList[j][1]=dicList[j][1]+1
                s=True
        if s == False:
            dicList.append([list_1[i],1])
    return dicList

            
A
myList=createList(10,1,5)
bubbleSort(myList)
print(myList)
a = normalHistogramFunction(myList)
print("Normal Histogram Function's Input: \n",a)
b = histogram_With_ListOf_Tuples(myList)
print("With List Of Tuples' Input: \n",b)




    