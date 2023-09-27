from enum import Enum
from CircleLinkedList import CircleLinkedList


class MenuChoice(Enum):
    EXIT = 0
    INSERT_FIRST = 1
    INSERT_LAST = 2
    INSERT_AFTER = 3
    DELETE_FIRST = 4
    DELETE_LAST = 5
    DELETE_AFTER = 6
    UPDATE = 7
    SHOW_INFORMATION = 8
    SEARCH = 9


class Menu:
    def __init__(self):
        self.list = CircleLinkedList()

    @staticmethod
    def showMenu():
        try:
            print("-" * 20 + " MENU " + "-" * 20)
            for choice in MenuChoice:
                print(f"| Choice {choice.value} to {' '.join(choice.name.split('_')).lower()}." + " " * (
                        30 - len(choice.name)) + "|")
            print("-" * 46)
            choice = Menu.getChoiceFromUser()
            Menu.handleUserChoice(choice)
        except ValueError:
            print("Invalid choice. Please enter a valid choice.")

    @staticmethod
    def getChoiceFromUser():
        while True:
            try:
                choice = int(input('Enter your choice (0 to exit): '))
                return choice
            except ValueError:
                print("Invalid choice. Please enter a valid choice.")

    def handleUserChoice(self, choice):
        if choice == MenuChoice.EXIT:
            print("Exitted program!!!!")
            status = False
        elif choice == MenuChoice.INSERT_FIRST:
            print("Insertting....")
            self.handleInsertFirst()
            pass
        elif choice == MenuChoice.INSERT_LAST:
            print("Insertting....")
            self.handleInsertLast()
            pass
        elif choice == MenuChoice.INSERT_AFTER:
            print("Insertting....")
            self.handleInsertAfter()
            pass
        elif choice == MenuChoice.DELETE_FIRST:
            print("Insertting....")
            self.handleDeleteFirst()
            pass
        elif choice == MenuChoice.DELETE_LAST:
            print("Deleting...")
            self.handleDeleteLast()
            pass
        elif choice == MenuChoice.DELETE_AFTER:
            print("Deleting...")
            self.handleDeleteAfter()
            pass
        elif choice == MenuChoice.SHOW_INFORMATION:
            print("Show...")
            self.handleShow()
            pass

    def handleInsertFirst(self):
        print("Input value: ", end='')
        value = int(input())
        self.list.insertFirst(value)
        pass

    def handleInsertLast(self):
        print("Input value: ", end='')
        value = int(input())
        self.list.insertLast(value)
        pass

    def handleInsertAfter(self):
        print("Input value: ", end='')
        value = int(input())
        print("Input index: ", end='')
        index = int(input())
        self.list.insertAtIndex(index, value)
        pass

    def handleDeleteFirst(self):
        self.list.deleteFirst()
        pass

    def handleDeleteLast(self):
        self.list.deleteLast()
        pass

    def handleDeleteAfter(self):
        print("Input index: ", end='')
        index = int(input())
        self.list.deleteAtIndex(index)
        pass

    def handleShow(self):
        self.list.display()
        pass
