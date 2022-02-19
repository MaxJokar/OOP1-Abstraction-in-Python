#Data Abstraction in Python
#interface Doesnt Exist in Python !
from abc import ABC,abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @abstractmethod
    def showInfo(self):
        pass
         
        
class Student(Person):
    def __init__(self,studentId,name,age):
        super().__init__(name, age)
        self.studentId=studentId
        
    def showInfo(self):
        print(f"{self.name}\t {self.age}\t{self.studentId}")  
        
        
class Teacher(Person):
    def __init__(self,teacherCode, name, age):
        super().__init__(name,age)
        self.teacherCode=teacherCode   

    def showInfo(self):
          
        print(f"Name : {self.name}\t Age: {self.age}\t Teacher Code :{self.teacherCode}")  
        

student1=Student(100,"Rose",18)
teacher1=Teacher(200,"Philip",19)

student1.showInfo()
teacher1.showInfo()






































