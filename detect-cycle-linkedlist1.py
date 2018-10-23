#1. travese list and store in a list and at point list reaches end without finding any duplicate value , then return null
#2- and if value of the current pointed node matches to any of the previously stored nodes then return True

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class sLinkedList:
    def __init__(self):
        self.head = None

    def add(self, NewData):
        newNode = Node(NewData)
        newNode.next = self.head
        self.head = newNode

    def PrintList(self):
        printVal = self.head
        while printVal:
            print(printVal.data, end=' ')
            printVal = printVal.next

    def Detect_loop(self):
        s = set() # set contains unique values
        temp = self.head
        while temp:
            if temp in s:
                return True
            s.add(temp) # add to set
            temp = temp.next  # move to next pointer
        return False


l_list = sLinkedList()
l_list.add(20)
l_list.add(4)
l_list.add(15)
l_list.add(10)


# Create a loop for testing
l_list.head.next.next.next.next = l_list.head

print(l_list.Detect_loop())
