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

def linear_Search(list_1,lookUpValue):
    found =(-1,-1)
    for i in range(len(list_1)):
        if list_1[i] ==lookUpValue:
            found = (i,lookUpValue)
            break
    return found

def avarage_Of_List(list_1):
    n = len(list_1)
    total = 0
    for i in range (n):
        total = total+list_1[i]
    return total/n

def my_Binary_Search(list_1,lookUpValue):
    found=(-1,-1)
    low = 0
    height = len(list_1)-1
    while low!=height:
        mid = (low+height)/2
        if list_1[mid]==lookUpValue:
            found = (lookUpValue,mid)
        elif mid<lookUpValue:
            low = mid-1
        else:
            height=mid+1
    return found


def find_Middle_Item(list_1):
    n = len(list_1)
    if n%2==1:
        mid = (n-1)//2
        return list_1[mid]
    else:
        middle_1 = n//2-1
        middle_2=n//2
        avarage = (list_1[middle_1]+list_1[middle_2])/2
        return avarage
    
    

myList=createList(10,-5,5)
bubbleSort(myList)
print(myList)
a=linear_Search(myList,0)
print(a)
b = find_Middle_Item(myList)
print(b)
c = my_Binary_Search(myList,0)
print(c)
        
    
    
    


        



