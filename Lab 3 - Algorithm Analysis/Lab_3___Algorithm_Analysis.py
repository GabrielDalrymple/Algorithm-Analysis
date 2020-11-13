import bigo
import timeit
import random

FINDFUNCTIONS = 4
#helper list fuction
def createList(size):
	list = []
	for i in range(size):
		list.append(random.randint(1, (size*10)))
	return list

#global variables for testing
myList = createList(10)
beginOfList = myList[0]
endOfList   = myList[-1]
midOfList   = myList[len(myList) // 2]
partOfList  = myList[random.randint(1, len(myList) - 2)]
beyondList  = (len(myList) * 100) + 1
belowList   = -1

#debugging tests for each find function.  Checks for all the global variables
#at different spots in the list to ensure correctness
def testFind1():
	print("Linear search, not using in")
	print("Check for item at beginning, end, middle, and somehere in the list.  All should return true")
	print(bigo.find1(myList, beginOfList))
	print(bigo.find1(myList, endOfList))
	print(bigo.find1(myList, midOfList))
	print(bigo.find1(myList, partOfList))

	print()
	print("Check for items beyond and below the list, both should be false")
	print(bigo.find1(myList, beyondList))
	print(bigo.find1(myList, belowList))
	print()
	return

def testFind2():
	print("Deep copy, built-in sort, binary search")
	print("Check for item at beginning, end, middle, and somehere in the list.  All should return true")
	print(bigo.find2(myList, beginOfList))
	print(bigo.find2(myList, endOfList))
	print(bigo.find2(myList, midOfList))
	print(bigo.find2(myList, partOfList))

	print()
	print("Check for items beyond and below the list, both should be false")
	print(bigo.find2(myList, beyondList))
	print(bigo.find2(myList, belowList))
	print()
	return

def testFind3():
	print("Linear search, using in")
	print("Check for item at beginning, end, middle, and somehere in the list.  All should return true")
	print(bigo.find3(myList, beginOfList))
	print(bigo.find3(myList, endOfList))
	print(bigo.find3(myList, midOfList))
	print(bigo.find3(myList, partOfList))

	print()
	print("Check for items beyond and below the list, both should be false")
	print(bigo.find3(myList, beyondList))
	print(bigo.find3(myList, belowList))
	print()
	return

def testFind4():
	print("Binary search on presorted list")
	binaryList = myList[:]
	binaryList.sort()
	print("Check for item at beginning, end, middle, and somehere in the list.  All should return true")
	print(bigo.find4(binaryList, beginOfList))
	print(bigo.find4(binaryList, endOfList))
	print(bigo.find4(binaryList, midOfList))
	print(bigo.find4(binaryList, partOfList))

	print()
	print("Check for items beyond and below the list, both should be false")
	print(bigo.find4(binaryList, beyondList))
	print(bigo.find4(binaryList, belowList))
	return

#running the tests
#testFind1()
#testFind2()
#testFind3()
#testFind4()

#Timer tests on lists of various sizes
listSizes = [10, 100, 1000, 10000, 100000]
def timerTests(sizes):
	i = 0
	while i < FINDFUNCTIONS:
		j = 0
		#print out which algorithm we are using
		if i == 0:
			print("Linear Search")
		elif i == 1:
			print("Deep Copy & Binary Search")
		elif i == 2:
			print("Linear Seach with In Function")
		elif i == 3:
			print("Binary Search")
		else: #error checking statement
			print("none")
		while j < len(sizes):
			#print out list size
			print("Timing function 10 times, with a list size of ", sizes[j])
			#complicated ass timer call to change size of the list and find algorithm
			timer = timeit.Timer("findTest(" + str(sizes[j]) + ", " + str(i+1) + ")", "from __main__ import findTest")
			#run it multiple times to try and ween out exceptionally good/bad cases
			duration = timer.timeit(10)
			#print how long it took
			print(duration, " seconds")
			#add extra space for readability
			print()
			#update counters
			j += 1
		i += 1
	return


def findTest(size, choice):
	#create variables
	myList = createList(size)
	beginOfList = myList[0]
	endOfList   = myList[-1]
	midOfList   = myList[len(myList) // 2]
	partOfList  = myList[random.randint(1, len(myList) - 2)]
	beyondList  = (len(myList) * 100) + 1
	belowList   = -1

	#deep copy of list and sorting for find4
	binaryList = myList[:]
	binaryList.sort()
	
	#check all variables but use different find function based on what is passed in
	#linear search (no in)
	if choice == 1: 
		bigo.find1(myList, beginOfList)
		bigo.find1(myList, endOfList)
		bigo.find1(myList, midOfList)
		bigo.find1(myList, partOfList)
		bigo.find1(myList, beyondList)
		bigo.find1(myList, belowList)
	#deep copy then binary
	elif choice == 2: 
		bigo.find2(myList, beginOfList)
		bigo.find2(myList, endOfList)
		bigo.find2(myList, midOfList)
		bigo.find2(myList, partOfList)
		bigo.find2(myList, beyondList)
		bigo.find2(myList, belowList)
	#linear with in
	elif choice == 3: 
		bigo.find3(myList, beginOfList)
		bigo.find3(myList, endOfList)
		bigo.find3(myList, midOfList)
		bigo.find3(myList, partOfList)
		bigo.find3(myList, beyondList)
		bigo.find3(myList, belowList)
	#binary on sorted
	elif choice == 4:
		bigo.find4(binaryList, beginOfList)
		bigo.find4(binaryList, endOfList)
		bigo.find4(binaryList, midOfList)
		bigo.find4(binaryList, partOfList)
		bigo.find4(binaryList, beyondList)
		bigo.find4(binaryList, belowList)
	else:
		print("Error, wrong number entered")
	return

timerTests(listSizes)