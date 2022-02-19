class Person :
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
        
    def showPersonInfo(self):
        print(self.__name)  
        print(self.__age)  
        
    def getName(self):
        return self.__name    
    
    def setName(self,name):
        self.__name=name 
    
    
    
person1=Person("Rose",72)
person1.showPersonInfo()

print(person1.getName())
person1.setName("Philip")
person1.showPersonInfo()  
    
    
    
    
    