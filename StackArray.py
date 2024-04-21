# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 4: Stack-Array
#
# NAME:         Sumi Nia Means 
# ASSIGNMENT:   Project 5: Implementing ADTs

class StackArray(object):
    def __init__(self, size=5):
        self.array = [0 for i in range(size)]
        self.top = -1

    def peek(self):
        if self.is_empty():
            return None
        return self.array[self.top]

    def pop(self):
        if self.is_empty():
            return None
        data = self.array[self.top]
        self.top -= 1
        return data

    def push(self, data=None):
        if self.is_full():
            return False
        self.top += 1
        self.array[self.top] = data
        return True

    def print(self):
        for i in range(self.top, -1, -1):
            print(self.array[i], "=>", end=" ")
        print("NULL")

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == len(self.array) - 1

    def clear(self):
       self.top = -1

    def size(self):
        return self.top + 1


def main():
    s = StackArray()
    s.print()
    print("Is empty?", s.is_empty())
    for i in range(1, 10):
        s.push(i)
    s.print()
    print("Peek:", s.peek())
    print("Pop: ", s.pop())
    s.print()
    print("Is empty?", s.is_empty())

# Don't run main on import
if __name__ == "__main__":
    main()

