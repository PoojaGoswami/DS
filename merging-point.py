class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class sLinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next


def getCount(listA):
    count = 0
    while listA is not None:
        if listA.next == None:
            count = 1
        else:
            listA = listA.next
            count +=1
        return count

# using list count/2
def getMiddle(listA):
    current = listA
    node_count = getCount(current)
    mid = node_count/2

    if node_count ==1:
        return listA
    elif node_count >1 :
        counter =0
        while current is not None and mid != counter:
            middle = current.next
            counter = counter+1
        return middle

def getMiddle1(listA):
    current = listA
    fast = listA
    slow = listA
    if listA is not None:
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow.data

def findMergePoint(listA,listB):
    #get current head value of both list from parameters
    curA = listA
    curB = listB

    #Do till the two nodes are the same
    while curA != curB:
        # If you reached the end of one list start at the beginning of the other one
        if curA.next == None:
            curA = listB
        else:
            curA = curA.next
        if curB.next == None:
            curB = listA
        else:
            curB = curB.next
    return curA.data


list1 = sLinkedList()
list1.head = Node("sk")
print('list1.head',list1.head.data)
e2 = Node("Pooja")
e3 = Node("Pj")
e4 = Node("Other")

list1.head.next = e2
e2.next = e3
e3.next = e4


list2 = sLinkedList()
list2.head = Node("sssss")
e5 = Node("Pjj")
list2.head.next = e5
e5.next = e2
e2.next = e3
e3.next = e4

list3 = sLinkedList()
list3.head = Node("sssssssssss")

list1.printlist()
print("------------------------")
list2.printlist()
print("------------------------")
print('merge point-',findMergePoint(list1.head,list2.head))


# print('\n','count', getCount(list3.head))
#
# print('\n','middle--m1', getMiddle1(list2.head))
#
# print('\n','middle', getMiddle1(list2.head))
#
#
#
# list4 = sLinkedList()
# list4.head = Node(1)
# n2=Node(2)
# n3=Node(3)
# n4=Node(4)
# n5=Node(5)
# list4.head.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
