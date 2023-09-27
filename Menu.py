from enum import Enum
from CircleLinkedList import CircleLinkedList
from Student import Student


class MenuChoice(Enum):
    EXIT = 0
    INSERT_FIRST_STUDENT = 1
    INSERT_LAST_STUDENT = 2
    INSERT_AT_INDEX_STUDENT = 3
    INSERT_AFTER_STUDENT = 4
    DELETE_FIRST_STUDENT = 5
    DELETE_LAST_STUDENT = 6
    DELETE_AFTER_STUDENT = 7
    DELETE_AT_INDEX_STUDENT = 8
    SEARCH_STUDENT_BY_ID = 9
    SEARCH_STUDENT_BY_NAME = 10


class Menu:
    def __init__(self):
        self.list = CircleLinkedList()

    def showMenu(self):
        """ Shows the menu to the user. """
        running = True
        while running:
            try:
                print("-" * 30 + "My Students List: " + "-" * 30)
                self.list.display()
                print("-" * 78)

                print("-" * 20 + " MENU " + "-" * 20)
                for choice in MenuChoice:
                    print(f"| Choice {choice.value} to {' '.join(choice.name.split('_')).lower()}." + " " * (
                            30 - len(choice.name)) + "|")
                print("-" * 46)
                choice = self.getChoiceFromUser()
                switcher = {
                    MenuChoice.INSERT_FIRST_STUDENT.value: self.handleInsertFirst,
                    MenuChoice.INSERT_LAST_STUDENT.value: self.handleInsertLast,
                    MenuChoice.INSERT_AT_INDEX_STUDENT.value: self.handleAtIndex,
                    MenuChoice.INSERT_AFTER_STUDENT.value: self.handleInsertAfter,
                    MenuChoice.DELETE_FIRST_STUDENT.value: self.handleDeleteFirst,
                    MenuChoice.DELETE_LAST_STUDENT.value: self.handleDeleteLast,
                    MenuChoice.DELETE_AFTER_STUDENT.value: self.handleDeleteAfter,
                    MenuChoice.DELETE_AT_INDEX_STUDENT.value: self.handleDeleteAtIndex,
                    MenuChoice.SEARCH_STUDENT_BY_ID.value: self.handleSearchById,
                    MenuChoice.SEARCH_STUDENT_BY_NAME.value: self.handleSearchByName
                }
                if choice == MenuChoice.EXIT.value:
                    running = False
                elif choice < (MenuChoice.__sizeof__(MenuChoice)):
                    switcher.get(choice)()

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
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        major = input("Enter student major: ")
        gpa = float(input("Enter student GPA: "))
        id_student = len(self.list)
        self.list.insertFirst(Student( id_student, name, age, major, gpa))

    def handleInsertLast(self):
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        major = input("Enter student major: ")
        gpa = float(input("Enter student GPA: "))
        id_student = len(self.list)
        self.list.insertLast(Student(id_student, name, age, major, gpa))

    def handleAtIndex(self):
        index = int(input("Enter index: "))
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        major = input("Enter student major: ")
        gpa = float(input("Enter student GPA: "))
        id_student = len(self.list)
        self.list.insertAtIndex(index, Student(id_student, name, age, major, gpa))

    def handleInsertAfter(self):
        value = input("Enter id student: ")
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        major = input("Enter student major: ")
        gpa = float(input("Enter student GPA: "))
        id_student = len(self.list)
        self.list.insertAfter(value, Student(id_student, name, age, major, gpa))

    def handleDeleteFirst(self):
        self.list.deleteFirst()

    def handleDeleteLast(self):
        self.list.deleteLast()

    def handleDeleteAfter(self):
        id_student = input("Enter id student: ")
        self.list.deleteAfter(id_student)

    def handleDeleteAtIndex(self):
        index = int(input("Enter index: "))
        self.list.deleteAtIndex(index)

    def handleSearchById(self):
        id_student = int(input("Enter id student: "))
        self.list.searchById(id_student)

    def handleSearchByName(self):
        name_student = input("Enter name student: ")
        self.list.searchByName(name_student)