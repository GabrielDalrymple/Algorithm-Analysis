#The unsorted list is searched linearly to see if the val is in the list
def find1(list, val):
	i = 0
	while i < len(list):
		if list[i] == val:
			return True
		i += 1
	return False

#A deep copy is made of the list; the copied list is then sorted using the sort 
#builtin function and then a binary search is performed on the list to find if 
#the val is in the list
def find2(list, val):
	l = list[:]
	l.sort()
	return binarySearch(l, val)

#The in built-in is used to determine if the val is in the unsorted list
def find3(list, val):
	for i in list:
		if i == val:
			return True
	return False

#This function requires the list to be sorted before it is called. A binary search is
#performed on the pre-sorted list to find val
def find4(list, val):
	return binarySearch(list, val)

#helper function
def binarySearch(list, val):
	#error checking
	if len(list) < 1:
		return False
	if len(list) == 1:
		if list[0] == val:
			return True
		else:
			return False
	low = 0
	high = len(list) - 1
	while low <= high:
		#find midpoint
		mid = (low + high) // 2
		#check if value is greater than mid
		if list[mid] < val:
			low = mid + 1
		#check if value is less mid
		elif list[mid] > val:
			high = mid - 1
		#value is mid
		else:
			return True
	return False