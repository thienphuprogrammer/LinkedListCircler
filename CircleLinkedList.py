class CircleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def insertFirst(self, e):
        self.head = Node(e, self.head)
        self.size += 1

    def insertLast(self, e):
        if self.isEmpty():
            self.head = Node(e, None)