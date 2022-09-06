class Node:
    # Initialises a new node
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    # Initialises a new linked list
    def __init__(self):
        self.head = None
        
    # Inserts new element into linked list
    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    # Prints the linked list
    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

    # Reverses the linked list
    def reverseList(self, lst):
        previous = None
        current = lst.head
        following = current.next

        while current:
            current.next = previous
            previous = current
            current = following
            if following:
                following = following.next
        lst.head = previous
        


