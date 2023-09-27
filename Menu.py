from enum import Enum
from CircleLinkedList import CircleLinkedList


class MenuChoice(Enum):
    EXIT = 0
    INSERT_FIRST = 1
    INSERT_LAST = 2
    INSERT_AT_INDEX = 3
    DELETE_FIRST = 4
    DELETE_LAST = 5
    DELETE_AFTER = 6
    DELETE_AT_INDEX = 7
    SHOW_INFORMATION = 8


class Menu:
    def __init__(self):
        self.list = CircleLinkedList()

    def showMenu(self):
        """ Shows the menu to the user. """
        running = True
        while True:
            try:
                print("My LinkedList: ", end='')
                self.list.display()

                print("-" * 20 + " MENU " + "-" * 20)
                for choice in MenuChoice:
                    print(f"| Choice {choice.value} to {' '.join(choice.name.split('_')).lower()}." + " " * (
                            30 - len(choice.name)) + "|")
                print("-" * 46)
                choice = self.getChoiceFromUser()

                if choice == MenuChoice.EXIT.value:
                    print("Exitted program!!!!")
                    running = False
                elif choice == MenuChoice.INSERT_FIRST.value:
                    self.handleInsertFirst()
                    pass
                elif choice == MenuChoice.INSERT_LAST.value:
                    self.handleInsertLast()
                    pass
                elif choice == MenuChoice.INSERT_AT_INDEX.value:
                    self.handleAtIndex()
                    pass
                elif choice == MenuChoice.DELETE_FIRST.value:
                    self.handleDeleteFirst()
                    pass
                elif choice == MenuChoice.DELETE_LAST.value:
                    self.handleDeleteLast()
                    pass
                elif choice == MenuChoice.DELETE_AFTER.value:
                    self.handleDeleteAfter()
                    pass
                elif choice == MenuChoice.DELETE_AT_INDEX.value:
                    self.handleDeleteAtIndex()
                    pass
            except ValueError:
                print("Invalid choice. Please enter a valid choice.")

    def getChoiceFromUser(self):
        """ Gets the choice from the user. """
        while True:
            try:
                choice = int(input('Enter your choice (0 to exit): '))
                return choice
            except ValueError:
                print("Invalid choice. Please enter a valid choice.")

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

    def handleAtIndex(self):
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
        print("Input value: ", end='')
        value = int(input())
        self.list.deleteAfter(value)
        pass

    def handleDeleteAtIndex(self):
        print("Input index: ", end='')
        index = int(input())
        self.list.deleteAtIndex(index)
        pass
