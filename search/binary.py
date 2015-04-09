def binary_search(alist, item):
	first = 0
	last = len(alist) - 1
	found = False

	while first <= last and not found:
		midpoint = (first + last) // 2
		if alist[midpoint] == item:
			found = True
		else:
			if item < alist[midpoint]:
				last = midpoint - 1
			else:
				first = midpoint + 1

	return found

def binary_recursive_search(alist, item):
	if len(alist) == 0:
		return False
	else:
		midpoint = len(alist) // 2
		if alist[midpoint] == item:
			return True
		else:
			if item < alist[midpoint]:
				return binary_recursive_search(alist[:midpoint], item)
			else:
				return binary_recursive_search(alist[midpoint+1:], item)

testlist = [0,1,2,3,8,12,34,35,65,102]
# print binary_search(testlist, 35)
print binary_recursive_search(testlist, 35)