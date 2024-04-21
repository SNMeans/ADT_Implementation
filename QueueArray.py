# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 5: Queue-Array
#
# NAME:         Sumi Nia Means 04/21/24
# ASSIGNMENT:   Technical HW: Implementing ADTs

class QueueArray(object):
    def __init__(self, size=5):
        self.array = [0 for i in range(size)]
        self.front = -1
        self.tail = -1

    def get_front(self):
        if self.is_empty():
            return None
        return self.array[self.front]

    def get_tail(self):
        if self.is_empty():
            return None
        return self.array[self.tail]

    def deq(self):
        if self.is_empty():
            return None
        data = self.array[self.front]
        if self.front == self.tail:
            self.front = self.tail = -1
        else:
            self.front = (self.front + 1) % len(self.array)
        return data

    def enq(self, data=None):
       if self.is_full():
            return False  
        if self.is_empty():
            self.front = self.tail = 0
        else:
            self.tail = (self.tail + 1) % len(self.array)
        self.array[self.tail] = data
        return True


    def print(self):
        for i in range(self.front, self.front + self.size(), 1):
            print(self.array[i % len(self.array)], "=>", end=" ")
        print("NULL")

    def is_empty(self):
        return self.front == -1

    def clear(self):
       self.front = self.tail = -1

    def is_full(self):
        l = self.size()
        return l >= len(self.array)

    def size(self):
        if self.front == -1:
            return 0
        l = self.tail - self.front + 1
        if self.tail < self.front:
            l = len(self.array) - self.front + self.tail + 1
        return l


def main():
    qa = QueueArray()
    qa.print()
    print("Is empty?", qa.is_empty())
    for i in range(1, 4):
        qa.enq(i)
        #print("Size:", qa.size())
        #qa.print()
    qa.print()
    print("Deq: ", qa.deq())
    print("Deq: ", qa.deq())
    qa.print()
    for i in range(5, 11):
        qa.enq(i)
        #print("Size:", qa.size())
        #qa.print()
    print("Front:", qa.get_front())
    print("Tail: ", qa.get_tail())
    print("Deq:  ", qa.deq())
    qa.print()
    print("Is empty?", qa.is_empty())
    print("Size:", qa.size())


# Don't run main on import
if __name__ == "__main__":
    main()

