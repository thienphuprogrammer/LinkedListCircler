class Node:
    def __init__(self, element, next=None):
        self.element = element
        self.next = next


class CircleLinkedList:
    def __init__(self):
        self.last_node = None
        self.size = 0

    def isEmpty(self):
        return self.last_node is None

    def size(self):
        return self.size

    def get(self, index):
        if self.isEmpty():
            return None
        current = self.last_node.next
        for i in range(index):
            current = current.next
        return current.element

    def indexOf(self, item):
        current = self.last_node.next
        index = 0
        while current is not None:
            if current.element == item:
                return index
            index += 1
            current = current.next
        return -1

    def remove(self, item):
        current = self.last_node.next
        previous = None
        found = False
        while current is not None and not found:
            if current.element == item:
                found = True
            else:
                previous = current
                current = current.next
        if previous is None:
            self.last_node = current
        else:
            previous.next = current.next
        self.size -= 1
        return found

    def deleteAfter(self, value):
        current = self.last_node.next
        previous = None
        found = False
        while current is not None and not found:
            if current.element == value:
                found = True
            else:
                previous = current
                current = current.next
        if previous is None:
            self.last_node = current
        else:
            previous.next = current.next
        self.size -= 1
        return

    def deleteFirst(self):
        if self.last_node is None:
            return
        if self.last_node.next is self.last_node:
            self.last_node = None
        else:
            self.last_node.next = self.last_node.next.next
        self.size -= 1
        return

    def deleteLast(self):
        if self.last_node is None:
            return
        if self.last_node.next is self.last_node:
            self.last_node = None
        else:
            current = self.last_node.next
            while current.next is not self.last_node:
                current = current.next
            current.next = self.last_node.next
            self.last_node = current
        self.size -= 1
        return

    def deleteAtIndex(self, index):
        if index < 0:
            print("Invalid index")
            return
        elif index >= self.size:
            self.deleteLast()
            return
        current = self.last_node.next
        previous = None
        for i in range(index):
            previous = current
            current = current.next
        previous.next = current.next
        self.size -= 1
        return

    def insertFirst(self, item):
        temp = Node(item)
        if self.last_node is None:
            self.last_node = temp
            self.last_node.next = self.last_node
        else:
            temp.next = self.last_node.next
            self.last_node.next = temp
        self.size += 1
        return

    def insertLast(self, item):
        temp = Node(item)
        if self.last_node is None:
            self.last_node = temp
            self.last_node.next = self.last_node
        else:
            temp.next = self.last_node.next
            self.last_node.next = temp
            self.last_node = temp
        self.size += 1
        return

    def insertAtIndex(self, index, item):
        if index < 0:
            print("Invalid index")
            return
        if index >= self.size:
            self.insertLast(item)
        temp = Node(item)
        current = self.last_node.next
        previous = None
        for i in range(index):
            previous = current
            current = current.next
        previous.next = temp
        temp.next = current
        self.size += 1
        return

    def display(self):
        if self.isEmpty():
            print("List is empty")
            return

        current = self.last_node.next
        while True:
            print(current.element, end=" ")
            current = current.next
            if current != self.last_node.next:
                print("->", end=" ")
            else:
                break
        print()
        return
