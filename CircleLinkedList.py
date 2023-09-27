class CircleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def isEmpty(self):
        return self.size == 0

    def insertfirst(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node

    def insertlast(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def insertafter(self, afterdata, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp is not None:
                if temp.data == afterdata:
                    break
                temp = temp.next
            if temp is None:
                print("Phần tử không tồn tại trong danh sách")
                return
            new_node.next = temp.next
            temp.next = new_node

    def display(self):
        nodes = []
        temp = self.head
        while True:
            nodes.append(temp.data)
            temp = temp.next
            if temp == self.head:
                break
        print(" -> ".join(map(str, nodes)))