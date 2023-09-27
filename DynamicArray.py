import ctypes
import random

class DynamicAraay:
    def __init__(self, capacity = 1):
        self.capacity = capacity
        self.size = 0
        self.elements = self.make_array(self.capacity)

    def make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def show_infor(self):
        print("current size: ", self.size)
        print("current capacity: ", self.capacity)
        for i in range(self.size):
            print(self.elements[i], end= ' ')
            
        print()

    def _resize(self, capacity):
        b = self.make_array(capacity)
        for i in range(self.size):
            b[i] = self.elements[i]

        self.elements = b
        self.capacity = capacity

    def insert(self, index, value):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)

        for j in range(self.size, index, -1):
            self.elements[j] = self.elements[j - 1]

        self.elements[index] = value
        self.size += 1


    def append(self, value):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        
        self.elements[self.size] = value
        self.size += 1
    
    
    #search a element in array and return the index of the element
    def search(self, value):
        index = None
        for i in range(self.size):
            if value == self.elements[i]:
                index = i
                break
            
        return index
    
            
    def delete_by_index(self, index):
        if index >= self.size:
            return False
        
        for i in range(index, self.size - 1, 1):
            self.elements[i] = self.elements[i + 1]
        
        self.size -= 1
        return True
            
    
    def delete_by_value(self, value):
        for i in range(self.size):
            if value == self.elements[i]:
                self.delete_by_index(i)
                
    def sort(self):
        for i in range(self.size):
            for j in range(i, self.size()):
                if (self.elements[j] > self.elements[j + 1]):
                    temp = self.elements[j]
                    self.elements[j] = self.elements[j + 1]
                    self.elements[j + 1] = temp
                    
                    
    def pop(self):
        self.elements[self.size() - 1] = 0
        self.size -= 1
        
    def count(self, value):
        cnt = 0
        for i in range(self.size):
            if self.elements[i] == value:
                cnt += 1
        return cnt
    
    def index(self, value):
        index = None
        for i in range(self.size):
            if self.elements[i] == value:
                index = i
                break
        return index
    
    def __len__(self):
        return self.size
    
    def __getitem__(self, index):
        return self.elements[index]
    
    def __setitem__(self, index, value):
        self.elements[index] = value