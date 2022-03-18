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
    value  = int(input("Enter the number of Values you want to enter"))
    for i in range(value):
        stack1.addinstack(input("enter the number \n"))  
        
    stack1.display()
    stack1.peek()
    stack1.pop()
    print("updated")
    stack1.display()