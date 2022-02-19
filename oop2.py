class Person :
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
        
    def showPersonInfo(self):
        print(self.__name)  
        print(self.__age)  
        