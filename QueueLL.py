# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 3: Queue-LL
#
# NAME:         Sumi Nia Means 04/21/24
# ASSIGNMENT:   Project 5: Implementing ADTs

from Node import Node

class QueueLL(object):
    def __init__(self, list=None):
        self.front = None
        self.tail = None
        if list is not None:
            for item in list:
                self.enq(item)

    def get_front(self):
        if self.is_empty():
            return None
        return self.front.get_data()

    def get_tail(self):
        if self.is_empty():
            return None
        return self.tail.get_data()

    def deq(self):
        if self.is_empty():
            return None
        data = self.front.get_data()
        self.front = self.front.get_next()
        if self.front is None:
            self.tail = None

        return data 

    def enq(self, data=None):
       new_node = Node(data)
        if self.is_empty():
            self.front = new_node 
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def print(self):
        n = self.front
        while n is not None:
            print(n.get_data(), "=>", end=" ")
            n = n.get_next()
        print("NULL")

    def is_empty(self):
        return self.front is None

    def clear(self):
        self.front = None
        self.tail = None 

def main():
    ql = QueueLL()
    ql.print()
    print("Is empty?", ql.is_empty())
    for i in range(1, 7):
        ql.enq(i)
    ql.print()
    print("Front:   ", ql.get_front())
    print("Deq:     ", ql.deq())
    ql.print()
    print("Is empty?", ql.is_empty())

# Don't run main on import
if __name__ == "__main__":
    main()

