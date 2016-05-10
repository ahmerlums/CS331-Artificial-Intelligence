"You will have to import the Stack class to use it in your implementation"
from util import Stack

toEnqueue = [1,2,3,4,5]

class QueueTheStack:
    "A container with a first-in-first-out (FIFO) queuing policy."   
    def __init__(self):
        self.Stack1 = Stack()
        self.Stack2 = Stack()
        "add adequate number of stacks here"
        "*** WRITE CODE HERE ***"

    def push(self,item):
        self.Stack1.push(item);
        "Enqueue the 'item' into the queue"
        "*** WRITE CODE HERE ***"
        
        
    def pop(self):
        while (not self.Stack1.isEmpty()):
            self.Stack2.push(self.Stack1.pop())

        toreturn = self.Stack2.pop()
        while (not self.Stack2.isEmpty()):
            self.Stack1.push(self.Stack2.pop())

        return toreturn


        "dequeue the 'item' from the queue"
        "*** WRITE CODE HERE ***"

    def isEmpty(self):
        return self.Stack1.isEmpty()
        "returns true if the queue is empty"
        "***WRITE CODE HERE***"
        



#MAIN Method
if __name__ == '__main__':

    myQueue = QueueTheStack()
    "This will enqueue the whole list."
    for i in toEnqueue:
        myQueue.push(i)

    "This should print the queue.. in order : 12345"
    for i in range(0,len(toEnqueue)):
        print myQueue.pop()
    


