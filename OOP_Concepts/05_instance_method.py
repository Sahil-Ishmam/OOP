# Instance MEthond is also class method 

class Myclass:
    x = 10
    def __init__(self,x_val,y_val) -> None:
        self.x = x_val
        self.y = y_val
    def add_two(self):
        print(self.x+self.y)

obj = Myclass(100,20)
obj.add_two()  # this is call instance method
        