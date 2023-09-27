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
    
  def printList(self):
    current = self.head
    while current != None:
      print(current.element, end = " ")
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
        
  def deleteFirst(self):
    if self.head == None:
      return
    self.head = self.head.next
      
  def deleteLast(self):
    if self.head == None:
      return
    current = self.head
    previous = None
    while current.next != None:
      previous = current
      current = current.next
    previous.next = None
      
  def deleteAtIndex(self, index):
    current = self.head
    previous = None
    for i in range(index):
      previous = current
      current = current.next
    previous.next = current.next
    
    
  def update(self, newItem, item):
    if self.head == None:
      return

    current = self.head
    while current != None:
      if current.element == item:
        current.element = newItem
        return
      current = current.next
    return
  
  def search(self, item):
    current = self.head
    while current != None:
      if current.element == item:
        return True
      current = current.next
    return False
  
  def delete(self, item):
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