#recursive Binary search
def recursive_Binary_search(lists,target):
    if len(lists) == 0:
        return False
    else:
        mid = (len(lists))//2
        if lists[mid] == target:
            return True
        else:
            if lists[mid] < target:
                return recursive_Binary_search(lists[mid+1:],target)
            else:
                return recursive_Binary_search(lists[:mid],target)
            
def verify(result):
        print("Element found:",result)
        
        
lists = [1,4,6,7,9,10,11,44,66]

result = recursive_Binary_search(lists,7)
verify(result)