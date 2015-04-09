def bubble_sort(alist):
    for num in range(len(alist)-1,0,-1):
        for i in range(num):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def short_bubble_sort(alist):
    exchanges = True
    num_passes = len(alist) - 1
    while num_passes > 0 and exchanges:
        exchanges = False
        for i in range(num_passes):
            if alist[i] > alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        num_passes = num_passes-1


# alist = [54,26,45,32,87,23,55,3,67,23,23]
# bubble_sort(alist)
# print alist

alist=[20,30,40,90,50,60,70,80,100,110]
short_bubble_sort(alist)
print(alist)