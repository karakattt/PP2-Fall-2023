#task3 classes
class shape:
    def __init__(self):
        self.area=0

class rectangle(shape):
    def __init__(self, length, width):
        super().__init__()
        self.length=length
        self.width=width
    def area_(self):
        return self.length*self.width

rc=rectangle(5, 4)
print(rc.area_())
