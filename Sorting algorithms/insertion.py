#Insertion sort

def Insertion_sort(array):
    for i in range(1,len(array)):
        key = array[i]
        
        j = i-1
        while j>=0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
        print("Iteration",i,"-->",array)

array = []
n = int(input("Enter range:"))
for i in range(0, n):
    item = int(input())
    array.append(item)
Insertion_sort(array)