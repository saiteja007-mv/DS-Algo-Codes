#Linear search using some loops
def linear_search(data,key):
    i = 0
    while i<len(data):
        if data[i] == key:
            return i
        i = i+1
    return False
data = []
data = input().split()
print(data)
key = input("Enter key:")

print("Element:",linear_search(data,key))

