def partition(array,low,high):
    
    pivot = array[high]
    
    i = low - 1
    for j in range(low,high):
        if array[j]<=pivot:
            i = i+1
            array[i],array[j]=array[j],array[i]
    array[i+1],array[high] = array[high],array[i+1]
    print(array)
    return i+1
        
def Quick_sort(array,low,high):
    
    if low < high:
        
        pi = partition(array,low,high)
        
        Quick_sort(array,low,pi-1)
        
        Quick_sort(array,pi+1,high)
        
array = []
n = int(input("Enter range:"))
for i in range(0, n):
    item = int(input())
    array.append(item)
Quick_sort(array,0,len(array)-1)
