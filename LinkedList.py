# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: Linked List
#
# NAME:         Sumi Nia Means 04/21/24
# ASSIGNMENT:   Project 5: Implementing ADTs

from Node import Node

class LinkedList(object):
    def __init__(self, list=None):
        self.head = None
        if list is not None:
            for item in list:
                self.add(item)

    def get_head(self):
        return self.head.data if self.head else None

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def delete(self, data):
        current = self.head
        previous= None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next  
                return data
            previous = current
            current = current.next
        return None 

    def print(self):
        n = self.head
        while n is not None:
            print(n.get_data(), "=>", end=" ")
            n = n.get_next()
        print("NULL")

    def is_empty(self):
        return self.head is None

    def clear(self):
        self.head = None

def main():
    l = list(range(1, 5))
    l.reverse()
    ll = LinkedList(l)
    ll.print()
    print("Search 4: ", ll.search(4))
    print("Search 5: ", ll.search(5))
    print("Delete 5: ", ll.delete(5))
    print("Delete 4: ", ll.delete(4))
    ll.print()
    print("Delete 1: ", ll.delete(1))
    ll.print()

# Don't run main on import
if __name__ == "__main__":
    main()

