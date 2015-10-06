# Quick Sort

# Using for pivot.
import random

mylist = (4, 6, 5, 9, 2, 3, 1, 8)

pivot_index = random.choice(range(len(mylist)))
pivot = mylist[pivot_index]
#pivot = random.choice(mylist)
# assuming unique list
# pivot_index = mylist.index(pivot)


left_range = range(0, pivot_index)
right_range = range(pivot_index+1, len(mylist))

left_side = mylist[0:pivot_index]
right_side = mylist[pivot_index+1:len(mylist)]

