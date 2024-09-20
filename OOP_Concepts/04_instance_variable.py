# Instance Variable 
class Myclass:
    x = 10
    def __init__(self,z) -> None:
        self.z = z # This is call instance variable only available in the created object
    

obj = Myclass(20)
