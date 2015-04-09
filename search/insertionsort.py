def insertion_sort(alist):
	for index in range(1, len(alist)):
		current_value = alist[index]
		position = index

		while position > 0 and alist[position - 1] > current_value:
			alist[position] = alist[position - 1]
			position = position - 1

		alist[position] = current_value

alist = [1,23,45,56553,4,3,456,6,65,34,43,68,78,75,455,68,65,34,3]
insertion_sort(alist)
print alist