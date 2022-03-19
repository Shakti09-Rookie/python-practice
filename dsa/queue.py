class queue:
    def __init__(self, capacity):
        self.queue = [None]* capacity
        self.front = self.size = 0
        self.rear = capacity-1
        self.capacity = capacity
    #enqueue
    # help taken from GFG
    def eq(self, value):
        if self.isFull():
            print("Queue is Full.")
            return
        else:
            self.rear = (self.rear + 1)%(self.capacity)
            self.queue[self.rear] = value
            self.size += 1
            print(f"size is {self.size}")
            # self.queue.append(value)
    #dequeue
    def dq(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        else:
            self.front = (self.front + 1) % self.capacity
            self.size -=1

    # def fo(self):
    #     self.queue.pop(0)

    def q_front(self):
        if self.isEmpty():
            print("Empty Queue")

        print(self.queue[0])
        #print(f"value at queue front -> {self.queue[self.front]}")

    def q_rear(self):
        if self.isEmpty():
            print("Empty Queue")

        # print(f"value at queue rear -> {self.queue[self.rear]}")
        print(self.queue[-1])
    #isfull
    def isFull(self):
        return self.size == self.capacity
    #isEmpty
    def isEmpty(self):
        return self.size == 0

    def printt(self):
        print(self.queue)

if __name__ == "__main__":
    sizee = int(input("Enter the size of queue"))
    queue1 = queue(sizee)
    for i in range(sizee):
        queue1.eq(input())

    print(f"is the queue full : ->{queue1.isFull()}")
    queue1.q_front()
    queue1.q_rear()
    queue1.printt()