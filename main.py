from CSD.DoubleLinkingList.CircleLinkedList import CircleLinkedList
from CSD.DoubleLinkingList.Menu import Menu

if __name__ == '__main__':
    a = CircleLinkedList()
    a.insertFirst(1)
    a.insertFirst(2)
    a.insertFirst(3)
    a.insertFirst(1)
    a.insertLast(5)
    a.insertLast(6)
    a.insertFirst(3123)
    a.insertAtIndex(1, 4)
    a.display()

    a.deleteLast()
    a.display()

    a.deleteAfter(2)
    a.display()

    a.deleteAtIndex(1)
    a.display()

    Menu.showMenu()