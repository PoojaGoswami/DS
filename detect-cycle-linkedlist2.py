#- floyd's cycle finding algorithm
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
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def Detect_loop(self):
        slow = self.head
        fast = self.head
        if slow and fast and fast.next:
            slow= slow.next
            fast = fast.next.next
            if slow==fast:
                print("cycle detected")
                return True
            return False

l_list = sLinkedList()
l_list.add(20)
l_list.add(15)
l_list.add(4)
l_list.add(10)

l_list.head.next.next.next = l_list.head

print(l_list.Detect_loop())
