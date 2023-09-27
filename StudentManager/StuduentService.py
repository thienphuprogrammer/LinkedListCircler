from LinkedList import LinkedList

class StudentService:
  def __init__(self) -> None:
    self.listStudent = LinkedList()
    pass

  def insertFrist(self, item):
    flat = True
    if self.listStudent.search(item):
      flat = False
    else:
      item.setId(self.listStudent.size + 1)
      self.listStudent.insertFisrt(item)
      
    return flat

  def insertLast(self, item):
    flat = True
    if self.listStudent.search(item):
      
      flat = False
    else:
      item.setId(self.listStudent.size + 1)
      self.listStudent.insertLast(item)
    return flat

  def insertAfter(self, item, id):
    if self.listStudent.searchByID(id):
      flat = True
      if self.listStudent.search(item):
        flat = False
      else:
        item.setId(self.listStudent.size + 1)
        self.listStudent.insertAfter(item, id)
      return flat

  def deleteFirst(self):  
    return self.listStudent.deleteFirst()

  def deleteLast(self):
    return self.listStudent.deleteLast()
    

  def deleteAfter(self, id):
    return self.listStudent.deleteAfter(id)
    

  def update(self, id, item):
    self.listStudent.update(id, item)
    pass

  def showInformation(self):
    self.listStudent.show()
    pass

  def searchByName(self, name):
    self.listStudent.searchByName(name)
    pass
  
    