def sequentialSearch(alist, search_var):
    for i in range(len(alist)-1):
        if search_var in alist:
            return True
    return False

#print(sequentialSearch([4, 2, 7], 2))

# Number of Operations
# --------------------
# Best Case: 1
# Worst Case: O(n)
# Average Case: n/2

def binarySearch(blist, search_var): #blist must be ordered
    mid = len(blist)//2
    while True:
        first_half = blist[:mid]
        second_half = blist[mid:]
        if len(blist) == 1:
            if search_var == blist[0]:
                return True
            else:
                return False
        if search_var < second_half[0]:
            blist = first_half
        if search_var > second_half[0]:
            blist = second_half
        if search_var == second_half[0]:
            return True
    return False

print(binarySearch([1, 2, 3, 4, 5], 5))

# Big-O of Binary Search
# Average = log(n)-1
#O(1)