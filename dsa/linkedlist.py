from types import NoneType


class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    #beginning
    def firstnode(self,data):
        node1 = node(data)
        node1.next = self.head
        self.head = node1
    #middle
    def atMiddle(self, data, after):
        temp= self.head
        if(self.head is None or temp.data != after):
            print("The given prvious value must be part of linked list.")
            return
        node1 = node(data)
        while(temp.data != after):
            temp = temp.next
        node1.next = temp.next    
        temp.next = node1
    #at end
    def atEnd(self, data):
        node1 = node(data)
        #if empty
        if self.head is None:
            self.head = node1
            return
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next

        temp.next = node1

    def delfrombeginning(self):
        self.head = self.head.next

    def delfromend(self):
        temp = self.head
        while(temp.next.next != None):
            temp = temp.next
        temp.next = None

    def deleteNode(self, position):
        if self.head is None:
            print("Linked list is empty")
            return
        if position == 0:
            self.head = self.head.next
            return self.head
        index = 1
        current = self.head
        prev = self.head
        temp = self.head
        while current is not None:
            if index == position:
                temp = current.next
                break
            else:
                prev = current
                current = current.next
                index += 1
        prev.next = temp
        return prev

    def searchbykey(self, key):
        temp = self.head
        while(temp.data != None):
            if temp.data == key:
                print("Item Found")
                return True
            else:
                temp = temp.next
        print("Not Found")
        return False

    def printutility(self):
        # while(self.head != None):
        #     print(self.head.data, end = " ")
        #     self.head = self.head.next
        temp = self.head
        while(temp != None):
            print(temp.data, end = " ")
            temp = temp.next

if __name__ == "__main__":
    linked1 = linkedlist()

    while True:
        print("\n Main Menu")
        print(f"""\n 1 To insert at beginning
                \n 2 To insert at end
                \n 3 To insert between two nodes
                \n 4 To print
                \n 5 To delete from beginning
                \n 6 To delete from end
                \n 7 To delete by position
                \n 8 To search by key
                \n 9 To sort the linked list
                \n 10 to exit""")
        choice = int(input("\n Enter your selection \n"))
        if choice == 1:
            linked1.firstnode(int(input("enter data \t")))
        elif choice == 2:
            linked1.atEnd(int(input("enter data \t")))
        elif choice == 3:
            linked1.atMiddle(int(input("enter data \t")), input("enter after which value you want to insert data \t"))
        elif choice == 4:
            linked1.printutility()
        elif choice == 5:
            linked1.delfrombeginning()
        elif choice == 6:
            linked1.delfromend()
        elif choice == 7:
            linked1.deleteNode(int(input("delete from which position \t")))
        elif choice == 8:
            linked1.searchbykey(int(input("Enter value to be searched \t")))
        elif choice == 10:
            break
        else:
            print("Invalid selection")