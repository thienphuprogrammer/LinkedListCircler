class Node:
    def __init__(self, data):
        self.element = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def size(self):
        if self.isEmpty():
            return 0

        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def get(self, index):
        if self.isEmpty():
            return None

        current = self.head
        for i in range(index):
            current = current.next
        return current.element

    def indexOf(self, item):
        current = self.head
        index = 0
        while current != None:
            if current.element == item:
                return index
            index += 1
            current = current.next
        return -1

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.element == item:
                found = True
            else:
                previous = current
                current = current.next
        if previous == None:
            self.head = current.next
        else:
            previous.next = current.next

    def insertFisrt(self, item):
        temp = Node(item)
        if self.head == None:
            self.head = temp
        else:
            temp.next = self.head

        self.head = temp
        self.size += 1

    def printList(self):
        current = self.head
        while current != None:
            print(current.element, end=" ")
            current = current.next
        print()

    def reverse(self):
        current = self.head
        previous = None
        while current != None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def insertLast(self, item):
        temp = Node(item)
        if self.head == None:
            self.head = temp
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = temp
            self.size += 1

    def insertAfter(self, item, id):
        temp = Node(item)
        if self.head == None:
            self.head = temp
        else:
            current = self.head
            while current.next != None:
                if current.element.id == id:
                    temp.next = current.next
                    current.next = temp
                    self.size += 1
                    break
                current = current.next
        

    def deleteFirst(self):
        if self.head == None:
            return False
        self.head = self.head.next
        self.size -= 1
        return True


    def deleteLast(self):
        if self.head == None:
            return False
        current = self.head
        previous = None
        while current.next != None:
            previous = current
            current = current.next
        previous.next = None
        self.size -= 1
        return True

    def deleteAfter(self, id):
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.element.id == id:
                found = True
            else:
                previous = current
                current = current.next
        if previous == None:
            self.head = current.next
        else:
            previous.next = current.next
        self.size -= 1
        return found

    def update(self, item, id):
        current = self.head
        found = False
        while current != None and not found:
            if current.element.id == id:
                found = True
            else:
                current = current.next
        if found:
            current.element = item
            
    def search(self, item):
        current = self.head
        while current != None:
            if current.element == item:
                return True
            current = current.next
        return False
    
    def searchByName(self, name):
        current = self.head
        while current != None:
            if current.element.name == name:
                return True
            current = current.next
        return False

    def searchByID(self, id):
        current = self.head
        while current != None:
            if current.element.id == id:
                return True
            current = current.next
        return False
       
    def show(self):
        current = self.head
        while current != None:
            current.element.showInformation()
            current = current.next