import matplotlib.pyplot as plt

plt.ion() #interactive

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
                print(list)
                plt.clf()
                plt.bar(list[i], list[i])
                plt.pause(0.5)

        plt.show()
        k -= 1
    return list

#bubbleSort([10, 4, 3, 1])


def SelectionSort(list):
    min_value = list[0] #first minimum value-- the first value in the list
    min_index = 0
    for i in range(len(list)):
        if list[i] < min_value: #if the number in the list is less than the current min
            min_value = list[i] #that list number is new min value
            
        min_index += 1











