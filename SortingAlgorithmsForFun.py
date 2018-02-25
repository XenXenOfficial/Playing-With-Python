import random #Only here to make the list a random value
BubbleList = [] #I made new lists cause its simplier than using the same list
'''
Bubble sort is super easy and its an extremely simple sorting algorithm.
All it does is repeatedly swap the adjacent numbers if they're in the 
wrong order.
'''
InsertionList = []
'''
Insertion Sort slowly makes the final sorted list one at a time, not quickest
for large data sets, but it works great for small things, and it's easy to 
implement.
'''
SelectionList = []
'''
Not great for large lists, and it can perform worse than insertion, but its
mostly known for its simplicity and it can have better performance advantages
over more complicated sorting algorithms like shell sort where memory is 
limited.
'''
ShakerList = []
'''
Basically the same thing as Bubble sort, but it goes both ways instead of just 
one way. It goes up the list and grabs the largest then places it, then
goes down it and grabs the smallest and places it.
'''
GnomeList = []
TrueLoop = True
'''
Also called Stupid sort, similar to insertion sort, but it swaps like bubble sort.
'''

while True: #Loops until the user put in a number
    try:
        Val = int(input("Put in a range: ")) #Gets a number from the user to make the range of the list (100 is 100 random numbers, 10 is 10 random, etc etc.)
    except ValueError: #Checks if the user didn't put in a integer
        print("Try again")
        continue #continues the loop
    else:
        break #Leaves the loop
        
for i in range(Val):
    RandomVal = random.randint(0, Val)
    BubbleList.append(RandomVal)
    InsertionList.append(RandomVal)
    ShakerList.append(RandomVal)
    SelectionList.append(RandomVal)
    GnomeList.append(RandomVal)
print("Heres the list", BubbleList)

def BubbleSwap(x,y):
    temp = x #Sets x as a temp value
    x = y #Swaps x with y 
    y = temp #Makes y equal temp (Which was saved as the X val)
    return x,y 

def SwapFunction(x, y):
    x, y = y, x #Swaps the integers
    return x, y

def SelectionSwap(minNum,y):
    minNum, y = y, minNum #Swaps the minimum value with the y value  
    return minNum, y

def GnomeSwap(x, y):
    Position = 0
    while Position < y:
        if Position == 0:
            Position += 1
        if x[Position] >= x[Position - 1]:
            Position += 1
        else:
            x[Position], x[Position - 1] = SwapFunction(x[Position], x[Position - 1])
            Position -= 1
    return(x)
    
for NumIns in range(len(InsertionList)-1,0, -1): #Goes down the list
    for i in range(NumIns):
        if InsertionList[i] > InsertionList[i + 1]: #Checks if its greater than the next 
            InsertionList[i], InsertionList[i + 1] = SwapFunction(InsertionList[i], InsertionList[i + 1]) #Swaps it

for NumBub in range(len(BubbleList)-1,0, -1): #Goes down the list
    for i in range(NumBub):
        if BubbleList[i] > BubbleList[i + 1]: #Checks if its greater than itself + 1
            BubbleList[i], BubbleList[i + 1] = BubbleSwap(BubbleList[i], BubbleList[i + 1]) #Swaps it

for NumSel in range(len(SelectionList)-1,0, -1): #Goes down the list
    minNum = NumSel #Saves the first value of the list
    for i in range(NumSel):
        if SelectionList[minNum] < SelectionList[i]: #Checks if that value is less than the next number 
            SelectionList[minNum], SelectionList[i] = SelectionSwap(SelectionList[minNum], SelectionList[i]) #Swaps it 

for NumCS in range(len(ShakerList)-1,0, -1): #Goes down the list
    for i in range(NumCS, 0, -1): #Goes down the list again for the i value
        if ShakerList[i] > ShakerList[i - 1]: #Checks if the value is less than the next
            ShakerList[i], ShakerList[i - 1] = SwapFunction(ShakerList[i], ShakerList[i - 1]) #Swaps it
    for i in range(NumCS): #Goes up the list
        if ShakerList[i] > ShakerList[i + 1]: #Checks if the value is greater than the next 
            ShakerList[i], ShakerList[i + 1] = SwapFunction(ShakerList[i], ShakerList[i + 1]) #Swaps it

while TrueLoop == True:
    YVal = len(GnomeList)
    GnomeList = GnomeSwap(GnomeList, YVal)
    TrueLoop = False

print("\nHeres it sorted Via Bubble", BubbleList, " Heres it sorted with insertion", InsertionList)
print("\nSorted through Selection", SelectionList, " Through the CockTail Shaker sort", ShakerList)
print("\nSorted through Gnome", GnomeList)
print("\nDone!")
