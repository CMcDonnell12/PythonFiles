# sortTimingsV2.py
# @CMcDonnell 27/09/2023
import time

# Create a function for each sorting algorithm type
#bubble sort
def bubble(myList):
    for outerIndex in range(len(myList) - 1):
        #print(myList)
        for index in range(len(myList) - 1):
            if myList[index] > myList[index+1]:
                tempValue = myList[index]
                myList[index] = myList[index+1]
                myList[index+1] = tempValue
    #print(myList)

#insertion sort
def insertion(myList):
    for index in range(1, len(myList)):
        #print(myList)
        itemInsert = myList[index]
        position = index
        while position > 0 and myList[position-1] > itemInsert:
            myList[position] = myList[position-1]
            position -=1
        myList[position] = itemInsert
    #print(myList)

#selection sort
def selection(myList):
    for index in range(len(myList)-1):
        #print(myList)
        nextMinValue = min(myList[index+1:])
        if nextMinValue < myList[index]:
            nextMinIndex = myList.index(nextMinValue)
            myList[nextMinIndex] = myList[index]
            myList[index] = nextMinValue
    #print(myList)

#quicksort

# Create a random list of size ...?
import random
myList = []

#loops 100 times
for num in range(10000):
    num1 = random.randint(1,100)#generating and storing random integer
    myList.append(num1)#appending value of num1 onto list

print(myList) #list of 100 random numbers (unsorted)
myOGList = myList.copy()
myOGList2 = myList.copy()


# Timed Bubble Sort
start = time.time() #uses import time return time in seconds
bubble(myList) #list is being sorted by bubble function
end = time.time() #returns time in seconds
print(myList)
print("Bubble sort: ",end-start,"seconds") #end-start returns value of time between line 51 and 53

print(myOGList)

# Timings for other sorting algorithms to be done below

#Timed Insertion Sort
start = time.time() #uses import time return time in seconds
insertion(myOGList) #list is being sorted by bubble function
end = time.time() #returns time in seconds
print(myOGList)
print("Insertion sort: ",end-start,"seconds") #end-start returns value of time between line 51 and 53

#Timed Selection Sort
start = time.time() #uses import time return time in seconds
selection(myOGList2) #list is being sorted by bubble function
end = time.time() #returns time in seconds
print(myOGList2)
print("Selection sort: ",end-start,"seconds") #end-start returns value of time between line 51 and 53

#Timed Quick Sort






