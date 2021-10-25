


class Node():

    def __init__(self,data):
        self.data = data
        self.next = None



class LinkedList():

    def __init__(self,head):
        self.head = head


    def append(self,node):

        curr_node = self.head

        while(curr_node.next != None):
            curr_node = curr_node.next


        

        
        curr_node.next = node

    def printList(self):

        curr_node = self.head

        while(curr_node != None):
            print(curr_node.data,end="->")
            curr_node = curr_node.next   
        print()

    def delete(self):

        curr_node = self.head

        while(curr_node.next.next != None):
            curr_node = curr_node.next

        temp = curr_node.next
        curr_node.next = None

        del temp

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node("hello")

ll = LinkedList(node1)

ll.append(3)
ll.append(node3)
ll.append(node4)


ll.printList()

ll.append(node5)

ll.printList()