'''
Scenario :
Your task is to slightly extend the Queue class's capabilities. 
We want it to have a parameterless method that returns True if the queue is empty and False otherwise.

Complete the code we've provided in the editor. Run it to check whether it outputs a similar result to ours.

Expected output :
1
dog
False
Queue empty
'''

class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.queue = []
    def put(self,elem):
        self.queue.insert(0,elem)
    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError


class SuperQueue(Queue):
    def isempty(self):
        if len(self.queue) >  0:
            return False
        return True


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")