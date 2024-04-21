# Project Title: Advanced Data Structures Implementation
## Introduction: 
This project is part of my learning journey through Joy of Coding Software Development Academy, focusing on the implementation of fundamental data structures from scratch. These include Linked Lists, Stacks, and Queues, using both array-based and linked-list implementations. This project emphasizes the development of a deep understanding of these structures, which are crucial for efficient data handling and algorithm development in software engineering.

## Technologies Used
- Python 3.8
* Pytest for unit testing
## Features
- Linked List: Efficient data insertion and deletion.
* Stack (Linked-List based and Array based): LIFO operations ideal for undo mechanisms in web applications.
+ Queue (Linked-List based and Array based): FIFO operations essential for task scheduling and managing user actions on a website.

## Code Examples 

```python
def push(self, data):
    # Adds a new Node with data to the top of the stack
    new_node = Node(data, self.top)
    self.top = new_node
````
This method demonstrates the push operation for a stack, a critical function in managing last-in, first-out operations.

## How to Install and Run the Project
Clone the repository:
```bash
git clone [https://github.com/SNMeans/ADT_Implementation]
cd [Project-Folder]
```
Install dependencies:
```bash
pip install -r requirements.txt
```
Run the project:
```bash
python3 LinkedList.py
```
## Usage Scenarios and Examples
- Undo Mechanism: Use the stack implementation to track user actions and provide an undo feature.
* Task Scheduling: Utilize queues to ensure that user-generated tasks are executed in the order they were received, improving overall system performance and reliability.

## Real-World Applications
- Web Development: Implementing undo features in text editors or graphic design tools.
* Software Engineering: Using queues to manage API requests in a web server to maintain service quality even under high load.

### License
MIT License
