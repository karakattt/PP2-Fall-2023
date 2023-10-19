#task1 classes
class string:
    def __init__(self):
        self.str=""
    def getsrting(self):
        self.str=input()
    
    def printstring(self):
        print(self.str.upper())
s=string()
s.getsrting()
s.printstring()
