class queue:
    def __init__(self):
        self.queue = []

    def add(self, value):
        self.queue.append(value)

    def fo(self):
        self.queue.pop(0)

    def printt(self):
        print(self.queue)

    def q_front(self):
        print(self.queue[0])

    def q_rear(self):
        print(self.queue[-1])

if __name__ == "__main__":
    queue1 = queue()
    queue1.add("one")
    queue1.add("two")
    queue1.add("three")
    queue1.add("four")
    queue1.printt()
    queue1.fo()
    queue1.printt()
    queue1.q_front()
    queue1.q_rear()