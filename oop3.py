#Data Abstraction in Python
#interface Doesnt Exist in Python !
from abc import ABC,abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @abstractmethod  # This function (Method) must be used in Children,could be with differet codes
    def showInfo(self):
        pass
         
        
class Student(Person):
    def __init__(self,name,age,studentId,):
        super().__init__(name, age)
        self.studentId=studentId
        
    def showInfo(self):
        print(f" Student Name :{self.name}\t St.Age  : {self.age}\t ID: {self.studentId}")  
        
        
class Teacher(Person):
    def __init__(self, name, age,teacherCode):
        super().__init__(name,age)
        self.teacherCode=teacherCode   

    def showInfo(self):
          
        print(f"Teacher Name : {self.name}\t Tea.Age: {self.age}\t Student Code :{self.teacherCode}")  
        

student1=Student("Rose",18,100)
teacher1=Teacher("Philip",19,250)

student1.showInfo()
teacher1.showInfo()






































