# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: Stack-LL
#
# NAME:         Sumi Nia Means 04/21/24
# ASSIGNMENT:   Project 5: Implementing ADTs

from Node import Node

class StackLL(object):
    def __init__(self, list=None):
        self.top = None
        if list is not None:
            for item in list:
                self.add(item)

    def peek(self):
        return self.top.data if self.top else None 

    def pop(self):
        if self.is_empty():
            return None
        data = self.top.data
        self.top = self.top.next
        return data 

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        

    def print(self):
        n = self.top
        while n is not None:
            print(n.get_data(), "=>", end=" ")
            n = n.get_next()
        print("NULL")

    def is_empty(self):
        return self.top is None

    def clear(self):
        self.top = None
    

def main():
    s = StackLL()
    s.print()
    print("Is empty?", s.is_empty())
    for i in range(1, 7):
        s.push(i)
    print("Peek:", s.peek())
    print("Pop: ", s.pop())
    s.print()
    print("Is empty?", s.is_empty())
    while not s.is_empty():
        print(s.pop())

# Don't run main on import
if __name__ == "__main__":
    main()

