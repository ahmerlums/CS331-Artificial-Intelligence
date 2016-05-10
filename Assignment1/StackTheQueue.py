
"You will have to import the Queue class to use it in your implementation"
from util import Queue

toStack = [1,2,3,4,5]

class StackTheQueue:
    "A container with a last-in-first-out (LIFO) queuing policy."
    def __init__(self):
        self.Queue1 = Queue()
        self.Queue2 = Queue()
        "Add Adequate queues!"
        "*** WRTIE CODE HERE ***"
        

    def push(self,item):
        self.Queue1.push(item)
        "Push 'item' onto the stack"
        "*** WRTIE CODE HERE ***"
        

    def pop(self):
        while(not self.Queue1.isEmpty()):
            temp = self.Queue1.pop()
            if self.Queue1.isEmpty():
                break
            self.Queue2.push(temp)

        while(not self.Queue2.isEmpty()):
            self.Queue1.push(self.Queue2.pop())

        return temp


            
        "Pop the most recently pushed item from the stack"
        "*** WRTIE CODE HERE ***"
        

    def isEmpty(self):
        return Queue1.isEmpty()
        "Returns true if the queue is empty"
        "*** WRTIE CODE HERE ***"
                

if __name__ == '__main__':

    myStack = StackTheQueue()

    #Push all values onto the stack
    for i in toStack:
        myStack.push(i)

    #Pop all the entered values...
    #This should print values in toStack in descending order: 54321!
    for i in range(0,len(toStack)):
        print myStack.pop()
