from time import sleep
mySequence = [12, 2, 1, 8, 3, 5, 4, 1, 8, 9, 12, 90, 1]

def bubble_ascending(myArray):
    next = 0
    sleep(0.3)
    for i in range(0, len(myArray)-1):
        if myArray[i] > myArray[i+1]:
            myArray[i+1], myArray[i] = myArray[i], myArray[i+1]
            next = 1
    print(myArray)
    if next == 1:
        bubble_ascending(myArray)
    else:
        return 0

def bubble_descending(myArray):
    next = 0
    sleep(0.3)
    for i in range(0, len(myArray)-1):
        if myArray[i] < myArray[i+1]:
            myArray[i+1], myArray[i] = myArray[i], myArray[i+1]
            next = 1
    print(myArray)
    if next == 1:
        bubble_descending(myArray)
    else:
        return 0
    

bubble_ascending(mySequence)
print("=================================")
bubble_descending(mySequence)
