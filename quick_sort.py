# Quick Sort

import random

def quick_sort(mylist):

    #pivot = random.choice(mylist)

    # left_range = range(0, pivot_index)
    # right_range = range(pivot_index+1, len(mylist))
    #pivot_index = mylist.index(pivot)
    if len(mylist) == 1:
        return mylist

    if len(mylist) == 0:
        return mylist

    pivot_index = random.choice(range(len(mylist)))
    pivot = mylist[pivot_index]

    left_side = mylist[0:pivot_index]
    right_side = mylist[pivot_index+1:]

    if not left_side and not right_side:
        return pivot

    right_side_2 = list()
    left_side_2 = list()

    for item in left_side+right_side:
        if item > pivot:
            right_side_2.append(item)
        if item <= pivot:
            left_side_2.append(item)

    return (quick_sort(left_side_2) + [pivot] + quick_sort(right_side_2))

mylist = [4, 6, 5, 9, 2, 3, 1, 8]
print mylist
print quick_sort(mylist)