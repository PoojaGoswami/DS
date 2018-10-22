class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class sLinkedList:
    def __init__(self):
        self.head = None

    def insert(self,NewData):
        newNode = Node(NewData)

        if self.head is None:
            newNode.next = self.head
            self.head = newNode
        elif self.head.data > newNode.data:
            newNode.next = self.head
            self.head = newNode
        else:
            current = self.head
            while current is not None and current.next.data < newNode.data:
                current = current.next
                # print(current.data)
            newNode.next = current.next
            current.next = newNode

    def printlist(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next







sll = sLinkedList()
sll.head = Node(5)

n2 = Node(6)

n3 = Node(9)
sll.head.next = n2
n2.next = n3

# NewNode = Node(7)
sll.printlist()
sll.insert(7)

print("\n", "print new linked list")
sll.printlist()
