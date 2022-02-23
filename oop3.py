#Data Abstraction in Python
#interface Doesnt Exist in Python !
from abc import ABC,abstractmethod

class Person(ABC):
    def __init__(self, name, age,Nationality):
        self._name = name
        self._age = age
        self.__nationality=Nationality #Can not be Accessed By Children if the field is  PRIVATE!
        
    @abstractmethod  # This function (Method) must be used in Children,could be with differet codes
    def showInfo(self):
        pass
         
        
class Student(Person):
    def __init__(self,name,age,Nationality,studentId):
        super().__init__(name, age,Nationality)
        self.studentId=studentId
        
    def showInfo(self):
       # print(f" Student Name :{self._name}\t St.Age  : {self._age}\t Nationality :{self.__nationality} ID: {self.studentId}")  
       #Children can not access to the PRIVATE   fields!
       print(f" Student Name :{self._name}\t St.Age  : {self._age}\t  ID: {self.studentId}")  
        
class Teacher(Person):
    def __init__(self, name, age,Nationality,teacherCode):
        super().__init__(name,age,Nationality)
        self.teacherCode=teacherCode   

    def showInfo(self):
          
        print(f"Teacher Name : {self._name}\t Tea.Age: {self._age}\t  Student Code :{self.teacherCode}")  
        

student1=Student("Rose",18,"American",100)
teacher1=Teacher("Philip",19,"NONE",250)

student1.showInfo()
teacher1.showInfo()






































