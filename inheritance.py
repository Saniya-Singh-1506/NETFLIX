class car:
    @staticmethod   #A static method is a function inside a class that doesn’t
                    #use "self" and can be called without creating an object.
    def start():
        print("carrrr starteddddd")
        
    @staticmethod   
    def stop():
        print("car stoppeeddd")
        
class toyota(car):   #inherit from parent class car
    def __init__(self,name):
        self.name=name
        
s1=toyota("fortuner")
print(s1.start())
