# constructor with parameter

class Myclass:
    x = 10
    def __init__(self,a,b) -> None:
        sum = self.x + a+ b
        print(sum)

obj = Myclass(30,40)


