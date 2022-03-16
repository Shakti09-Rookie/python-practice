class stack:
    def __init__(self):
        self.stack = []

    def addinstack(self, value):
        if self.stack is not None:
            return self.stack.append(value)

    def display(self):
        for item in self.stack:
            print(item)

    def peek(self):
        print(self.stack[-1])

    def pop(self):
        return self.stack.pop()

if __name__ == "__main__":
    stack1 = stack()
    stack1.addinstack("5")
    stack1.addinstack("6")
    stack1.addinstack("7")
    stack1.addinstack("8")
    stack1.display()
    stack1.peek()
    stack1.pop()
    print("updated")
    stack1.display()