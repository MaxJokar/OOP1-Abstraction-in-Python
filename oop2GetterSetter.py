class Person :
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
        
    def showPersonInfo(self):
        print(self.__name)  
        print(self.__age)  
        
    @property #helps that this function becomes a Getter    
    def name(self):
        return self.__name 
    @name.setter
    def name(self,name):
        self.__name=name   
        
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        self.__age=age    
#===========OLD METHOD TO GET & SET  :===============================        
    #getter or setter  functions     
    # def getName(self):
    #     return self.__name    
    
    # def setName(self,name):
    #     self.__name=name 
    
    
    
person1=Person("Rose",72)
person1.showPersonInfo()

# print(person1.getName()),==>print(person1.name)  
# person1.setName("Philip")
# person1.showPersonInfo()  
#==============================================    
# property is between fields and methods and functions
# print(person1.name)   ==>works without this part too !
person1.name="Philip" #<==>person1.setName("Philip")
person1.showPersonInfo()   
    
person1.age=120
print(person1.age)   