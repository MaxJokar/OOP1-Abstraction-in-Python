class Person:
    #example of  an instance method:(data of the class are name or age )
    def __init__(self,name,age): 
        self.name=name
        self.age=age
        
    def showPersonInfo(self):  #showPersonInfo:instance method depends on the method
        print(self.name)    
        print(self.age)
        
person1=Person("Jack",48)
person1.showPersonInfo()        