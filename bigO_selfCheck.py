def n_list_linear(alist):
    low_term = alist[0]
    for i in range(len(alist)-1):
        if alist[i] < low_term:
            low_term = alist[i]
    return low_term

def n_squared(blist):
    counter = 0
    flip = True
    k = len(blist)-1
    while flip:
        flip = False
        for i in range(k):
            counter += 1
            if blist[i] > blist[i+1]:
                blist[i], blist[i+1]= blist[i+1], blist[i]
                flip = True

        k -= 1
    return blist[0]
