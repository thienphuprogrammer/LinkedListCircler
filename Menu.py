from enum import Enum
from DynamicArray import DynamicArray

class MenuChoice(Enum):
    EXIT = 0
    INSERT = 1
    APPEND = 2
    SHOW = 3
    SEARCH = 4
    DELETE = 5
    SORT = 6
    UPDATE = 7
    
class Menu():
  def __init__(self, arr):
    self.arr = arr
    pass
  
  
  def showMenu(self):
    print("-------- MENU --------")
    for choice in MenuChoice:
        print(f"Choice {choice.value} to {choice.name.lower()}.")
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
    elif choice == MenuChoice.INSERT:
      print("Insertting....")
      self.handleInsert()
      pass
    elif choice == MenuChoice.APPEND:
      print("Appending...")
      self.handleAppend()
      pass
    elif choice == MenuChoice.SHOW:
      print("Show...")
      self.handleShow()
      pass
    elif choice == MenuChoice.SEARCH:
      print("Search...")
      self.handleSearch()
      pass
    elif choice == MenuChoice.DELETE:
      print("Deleting...")
      self.handleDelete()
      pass
    elif choice == MenuChoice.SORT:
      print("Sorting...")
      self.handleSort()
      pass
    elif choice == MenuChoice.UPDATE:
      print("Update...")
      self.handleUpdate()
      pass
    
    return status

  #Handle code here
  def handleInsert(self):
    pass
  
  
  def handleAppend(self):
    self.arr.append()
    pass
  
  
  def handleShow(self):
    pass
  
  
  def handleSearch(self):
    pass
  
  
  def handleDelete(self):
    pass
  
  
  def handleSort(self):
    pass
  
  
  def handleUpdate(self):
    pass
  
  
if __name__ == '__main__':
  menu = Menu()
  while True:
    menu.showMenu()
    choice = menu.getChoiceFromUser()
    if not menu.handleUserChoice(choice): 
      break
`