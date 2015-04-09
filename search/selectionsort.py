def selection_sort(alist):
    for fill_slot in range(len(alist) - 1,0,-1):
        position_of_max = 0
        for location in range(1, fill_slot + 1):
            if alist[location] > alist[position_of_max]:
                position_of_max = location

        temp = alist[fill_slot]
        alist[fill_slot] = alist[position_of_max]
        alist[position_of_max] = temp

alist = [54,23,65,87,43,32,5,7,3423,44,6,23,35,6,68,76,53,3]
selection_sort(alist)
print alist