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


def find_Mode_With_Dict(Dic):
    maxRepetition = -1
    mode=-1
    for key in Dic.keys():
        if Dic[key]>maxRepetition:
            maxRepetition=Dic[key]
            mode = key
    return mode,maxRepetition

def find_Mode_With_Tuples(list_1):
    maxRepetition = -1
    mode=-1
    for item,repetition in list_1:
        if repetition>maxRepetition:
            maxRepetition = repetition
            mode = item
    return mode,maxRepetition

myList = createList(10,1,5)
bubbleSort(myList)
Dic_1 = normalHistogramFunction(myList)
print(myList)
Dic_2= histogram_With_ListOf_Tuples(myList)

print("Dic_1: ",find_Mode_With_Dict(Dic_1))
print("Dic_2: ",find_Mode_With_Tuples(Dic_2))
    

