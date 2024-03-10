# Node class
class Node:
    def __init__(self,value):
        self.next = None
        self.value = value
        self.pre = None
        
# D-linked list class         
class DoublyLinkedList:
    def __init__(self,value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1
                        
    # append method   
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.pre = self.tail
            self.tail = new_node
            self.length +=1    
        return True
    
    # pop method 
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.pre
            self.tail.next = None
            temp.pre = None
        self.length -=1
        return temp        
            
            
    
    
    # get head 
    def get_head(self):
        return self.head.value  
    
    
    def print_list(self):
        if self.length == 0:
            print("The list is empty.")
            return
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
      
    
doubly_linked_list = DoublyLinkedList(1)
doubly_linked_list.append(2)
doubly_linked_list.append(3)
doubly_linked_list.append(4)
doubly_linked_list.append(5)
doubly_linked_list.append(6)
doubly_linked_list.pop()
doubly_linked_list.pop()
doubly_linked_list.pop()
doubly_linked_list.pop()
doubly_linked_list.pop()
doubly_linked_list.pop()

print(doubly_linked_list.pop())
print(doubly_linked_list.pop())
print(doubly_linked_list.pop())
doubly_linked_list.print_list()