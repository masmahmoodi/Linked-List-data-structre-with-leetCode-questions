# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# LinkedList class
class LinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    # Print list method
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Append method
    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        return True

    # Pop method
    def pop(self):
        if self.head is None:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        pre.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    # Prepend method
    def prepend(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return True

    # Pop first method
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value

    # Get method
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp

    # Set method
    def set(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    # Insert method
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        newNode = Node(value)
        temp = self.get(index - 1)
        newNode.next = temp.next
        temp.next = newNode
        self.length += 1
        return True

    # Remove method
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp.value

    # Reverse method
    def reverse(self):
        current = self.head
        previous = None
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.tail = self.head
        self.head = previous

    # Has loop method
    def has_loop(self):
        fast = self.head
        slow = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

    # Remove duplicates method
    def remove_duplicates(self):
        values = set()
        previous = None
        current = self.head
        while current:
            if current.value in values:
                previous.next = current.next
                self.length -= 1
            else:
                values.add(current.value)
                previous = current
            current = current.next

    # Length method
    def len(self):
        return self.length

# Example usage
mylinkedlist = LinkedList(1)
mylinkedlist.append(2)
mylinkedlist.append(3)
mylinkedlist.append(1)
mylinkedlist.append(4)
mylinkedlist.append(2)
mylinkedlist.append(5)

print("Original List:")
mylinkedlist.printList()
print(f"Length: {mylinkedlist.len()}")

print("\nList after removing duplicates:")
mylinkedlist.remove_duplicates()
mylinkedlist.printList()
print(f"Length: {mylinkedlist.len()}")
