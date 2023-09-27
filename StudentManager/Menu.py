from enum import Enum
from StuduentService import StudentService
from Student import Student

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


class Menu():
    def __init__(self):
        self.studentService = StudentService()
        pass

    def showMenu(self):
        print("-------- MENU --------")
        for choice in MenuChoice:
            print(f"Choice {choice.value} to {' '.join(choice.name.split('_')).lower()}.")
        print("----------------------")

    def getChoiceFromUser(self):
        while True:
            try:
                choice = int(input("Enter your choice (0 to exit): "))
                menu_choice = MenuChoice(choice)
                return menu_choice
            except ValueError:
                print("Invalid choice. Please enter a valid choice.")

    def handleUserChoice(self, choice):
        status = True

        if choice == MenuChoice.EXIT:
            print("Exitted program!!!!")
            status = False
        elif choice == MenuChoice.INSERT_FIRST:
            print("Insertting....")
            self.handleInsertFrist()
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
            self.handleDeleteFrist()
            pass
        elif choice == MenuChoice.DELETE_LAST:
            print("Insertting....")
            self.handleDeleteLast()
            pass
        elif choice == MenuChoice.DELETE_AFTER:
            print("Insertting....")
            self.handleDeleteAfter()
            pass
        elif choice == MenuChoice.UPDATE:
            print("Insertting....")
            self.handleUpdate()
            pass
        elif choice == MenuChoice.SHOW_INFORMATION:
            print("Showing....")
            self.handleShowInformation()
            pass
        elif choice == MenuChoice.SEARCH:
            print("Insertting....")
            self.handleSearch()
            pass

        return status
    def createNewStudent(self):
        print("Enter student information: ")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        mssv = int(input("Enter mssv: "))
        return Student(name, age, mssv)

    # Handle code here
    def handleInsertFrist(self):
        stduent = self.createNewStudent()
        self.studentService.insertFrist(stduent)
        pass

    def handleInsertLast(self):
        stduent = self.createNewStudent()
        self.studentService.insertLast(stduent)
        pass

    def handleInsertAfter(self):
        print("ID of student that want to insert after: ", end="")
        id = int(input())
        
        stduent = self.createNewStudent()
        self.studentService.insertAfter(stduent, id)
        pass
    
    def handleDeleteFrist(self):
        if self.studentService.deleteFirst():
            print("Deleted")
        else:
            print("Not found")
    
    def handleDeleteLast(self):
        if self.studentService.deleteLast():
            print("Deleted")
        else:
            print("Not found")
            
    def handleDeleteAfter(self):
        id = int(input("Enter id: "))
        if self.studentService.deleteAfter(id):
            print("Deleted")
        else:
            print("Not found")
    
    def handleUpdate(self):
        id = int(input("Enter id: "))
        if self.studentService.update(id):
            print("Updated")
        else:
            print("Not found")
    
    def handleShowInformation(self):
        self.studentService.showInformation()
        
    
    def handleSearch(self):
        name = input("Enter name: ")
        self.studentService.searchByName(name)