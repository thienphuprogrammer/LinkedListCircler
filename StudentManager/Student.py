class  Student:
    def __init__(self, name, age, mssv):
        self.name = name
        self.age = age
        self.mssv = mssv
        self.id = 0
        pass

    def getId(self):
        return self.id
    def setId(self, id):
        self.id = id

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

    def getMssv(self):
        return self.mssv

    def setMssv(self, mssv):
        self.mssv = mssv
        
        
    def showInformation(self):
        print(f"ID: {self.id}", end=" ")
        print(f"Name: {self.name}", end=" ")
        print(f"Age: {self.age}", end=" ")
        print(f"MSSV: {self.mssv}")
        print("")

        return