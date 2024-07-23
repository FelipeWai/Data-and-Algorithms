class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prior = None

class Doubly_Linked_List:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
        new_node.prior = cur

    def print_forward(self):
        """This method prints the list in forward direction"""
        cur = self.head
        while cur.next != None:
            cur = cur.next
            print(cur.data)

    def print_backward(self):
        """This method prints the list in backward direction"""
        cur = self.head
        while cur.next is not None:
            cur = cur.next

        while cur.prior is not None:
            cur = cur.prior
            print(cur.data)

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

my_list = Doubly_Linked_List()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()
my_list.print_forward()
my_list.print_backward()