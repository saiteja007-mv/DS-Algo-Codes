#Binary search 
def binary_search(lists , target):
    first = 0
    last  = len(lists)-1
    
    while first <= last:
        mid = (first + last)//2
        
        if lists[mid] == target:
            return mid
        elif lists[mid]<target:
            first = mid+1
        else:
            last = mid -1
    return None

def verify(index):
    if index is not None:
        print("Target found at index:",index)
    else:
        print("Target not found")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers,10)
verify(result)
    
result = binary_search(numbers,4)
verify(result)

result = binary_search(numbers,11)
verify(result)