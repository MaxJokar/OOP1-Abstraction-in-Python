class Person:
    #example of  an instance method:(data of the class are name or age )
    def __init__(self,name,age): 
        self.name=name
        self.age=age
        
    def showPersonInfo(self):  
        print(self.name)    
        print(self.age)
        
    #independant Method(Static method) :dosent Depend to the Class 
    #It doesnt belong to person1
    @staticmethod 
    def sum(x,y):
        return x+y 
    
    #It works with the class  datas
    #cls shows it belogs to what class(we access to the static or static values of the class)
    @classmethod 
    def fun1(cls,x,y):
        return cls.sum(x,y)+2000        
        
  
person1=Person("Jack",48)
person1.showPersonInfo()        
#Static method are called by the Class and not instance of Class
# print(Person.sum(20,50))
print(Person.fun1(3,25))
