#Linked List 

#Singly

#Creating a node and displaying elements in list
class Node:
    def __init__(self,data):
        self.data = data # Assign data
        self.next  = None # Initialize next as null
        print("Created Node",data)

class LinkedList:
     # Function to initialize head
    def __init__(self):
        self.head = None
        print("Linkedlist created")
    
    #Printing the data
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    
    # Function to insert a new node at the beginning
    def insert(self,new_data):
        
        # 1 & 2: Allocate the Node & Put in the data
        new_node = Node(new_data)
        # 3. Make next of new Node as head
        new_node.next = self.head
        # 4. Move the head to point to new Node
        self.head = new_node
        print("Node inserted",new_data)

        
    # This function is in LinkedList class. Inserts a
    # new node after the given prev_node. 
    def insertafter(self,prev,new_data):
        
        # 1. check if the given prev_node exists
        if prev is None:
            print("previous must be in ll")
            return
        
        #  2. create new node & Put in the data
        new_node = Node(new_data)
        # 3. Make next of new Node as next of prev_node
        new_node.next = prev.next
        # 5. make next of prev_node as new_node
        prev.next = new_node
        print("Node ",new_data,"inserted",)
        
    # This function is defined in Linked List class
    # Appends a new node at the end.  
    def insertend(self,new_data):
        #  1. create new node & Put in the data
        new_node = Node(new_data)
        # 2. If the Linked List is empty, then make the new node as head
        if self.head is None:
            self.head = new_node
            return
        # 3. Else traverse till the last node
        last = self.head
        while(last.next):
            last = last.next
        # 4. Change the next of last node
        last.next = new_node
        print("Node inserted at end",new_data)
    
    def deleteKey(self,key):
        #Store head node
        temp = self.head
        
        #If head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
            
        #Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
            
        # if key was not present in linked list
        if temp == None:
            return 
        # Unlink the node from linked list
        prev.next = temp.next
        temp = None
        
        print("Node ",key," deleted")
    
    # Given a reference to the head of a list
    # and a position, delete the node at a given position
    def deletePos(self,pos):
        if self.head is None:
            return
        if pos == 0:
            self.head = self.head.next
            return self.head
        index = 0
        current = self.head
        prev = self.head
        temp = self.head
        while current is not None:
            if index == pos:
                temp = current.next
                break
            prev = current
            current = current.next
            index += 1
        prev.next = temp
        print("Node deleted at ",pos)
    

  
    
#<<-----Driver Code----->>
#Creating nodes and list

llist = LinkedList()
llist.head = Node(1)

second = Node(2)
third = Node(3)
#Assigning nexts
llist.head.next = second
second.next = third
#Inserting elements starting
llist.insert(10)
#Inserting elements between
llist.insertafter(llist.head.next.next,20)
llist.insertafter(llist.head.next,24)
#Inserting elements end
llist.insertend(30)
llist.deleteKey(24)
llist.printlist()
llist.deletePos(2)
llist.printlist()