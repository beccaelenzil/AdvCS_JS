import matplotlib.pyplot as plt

plt.ion() #interactive


def display(some_list):
    plt.clf()
    plt.bar(range(len(some_list)),some_list)
    plt.draw()

def bubbleSort(list):
    k = len(list)-1
    flip = True
    #y = [i for i in range(len(list)+1)]
    #x = [i for i in range(len(y))]
    while flip == True:
        flip = False
        for i in range(k):
            plt.show()
            if list[i] > list[i+1]:
                list[i+1], list[i]= list[i], list[i+1]
                flip = True
                display(list)
                print(list)


        plt.show()
        k -= 1
    return list

bubbleSort([10, 4, 3, 1])


def SelectionSort(list):
    for d in range(len(list)):
        min_value = d

        for i in range(d+1, len(list)):
            print(list)
            if list[i] < list[min_value]: #if the number in the list is less than the current min
                min_value = i #that list number is new min value
        list[min_value], list[d] = list[d], list[min_value]

    return list

#print(SelectionSort([3, 2, 1, 10, 4]))









