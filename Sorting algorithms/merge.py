def Merge_sort(arr):
    if len(arr)>1:
        
        mid = len(arr)//2
        
        l = arr[:mid]
        r = arr[mid:]
        
        Merge_sort(l)
        print("Left-->",arr)
        Merge_sort(r)
        print("Right-->",arr)
        
        i=j=k=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1
            
        while i<len(l):
            arr[k] = l[i]
            i +=1
            k +=1

        while j<len(l):
            arr[k] = r[j]
            j +=1
            k =+1
    print("Sorted array-->",arr)
            
arr = []
n = int(input("Enter range:"))
for i in range(0, n):
    item = int(input())
    arr.append(item)
Merge_sort(arr)