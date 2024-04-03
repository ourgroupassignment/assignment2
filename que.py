#Queue class to maintain the appointment data
class Queue:
    def __init__(self):
        self.items = []
    #enqueue(insert) data in queue
    def enqueue(self, item):
        self.items.append(item)

    #dequeue data from queue
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    #to check the queue is empty or not
    def is_empty(self):
        return len(self.items) == 0

    #display the details of patient
    def display(self):
        if self.is_empty():
            return "Queue is empty\n"
        else:
            queue_str = ""
            for item in self.items:
                queue_str += str(item) + "\n"  
            return queue_str
