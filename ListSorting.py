import matplotlib.pyplot as plt
from random import shuffle

def create_random_list(length):
    some_list = [i for i in range(length)]
    shuffle(some_list)
    return some_list

plt.ion() #interactive


def display(some_list):
    plt.clf()
    plt.bar(range(len(some_list)),some_list)
    plt.draw()

def bubbleSort(list):
    counter = 0
    flip = True
    k = len(list)-1
    while flip:
        flip = False
        for i in range(k):
            counter += 1
            if list[i] > list[i+1]:
                list[i], list[i+1]= list[i+1], list[i]
                flip = True
                #display(list)

        k -= 1
    return counter

#print(bubbleSort([10, 4, 3, 1]))

'''
num_iter = []
for i in range(100):
    print(i)
    n = bubbleSort(create_random_list(100))
    num_iter.append(n)

ave_iter = sum(num_iter)/len(num_iter)
print(ave_iter)
'''

def SelectionSort(list):
    counter = 0
    for d in range(len(list)):
        min_value = d

        for i in range(d+1, len(list)):
            #print(list)
            counter += 1
            if list[i] < list[min_value]: #if the number in the list is less than the current min
                min_value = i #that list number is new min value
        list[min_value], list[d] = list[d], list[min_value]

    return counter

#print(SelectionSort([3, 2, 1, 10, 4]))
#print(counter)
'''
num_iter1 = []
for i in range(100):
    print(i)
    q = SelectionSort(create_random_list(100))
    num_iter1.append(q)

ave_iter1 = sum(num_iter1)/len(num_iter1)
print(ave_iter1)
'''

def insertionSort(list):

    for i in range(1, len(list)): #for each unsorted item in list
        while i > 0 and list[i-1] > list[i]: #so it only bubbles down until it reaches the correct spot
            print(list)
            list[i], list[i-1] = list[i-1], list[i] #"bubble" down
            i -= 1
        display(list)
    return list


print(insertionSort([4, 3, 2, 1]))






