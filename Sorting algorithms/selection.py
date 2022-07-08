#Sorting Algorithms

#1.Selection sort

def Selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1,len(array)):
            if array[min_index] >array[j]:
                min_index = j
        array[i],array[min_index] = array[min_index],array[i]
        print(array)

array = []
n = int(input("Enter range:"))
for i in range(0, n):
    item = int(input())
    array.append(item)
Selection_sort(array)