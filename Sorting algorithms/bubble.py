#1.Bubble sort

def Bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
        print(array)

array = []
n = int(input("Enter range:"))
for i in range(0, n):
    item = int(input())
    array.append(item)
Bubble_sort(array)