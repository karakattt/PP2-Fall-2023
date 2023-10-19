# task2 classes
class shape:
    def __init__(self):
        self.area=0


class square(shape):
    def __init__(self, length):
        super().__init__()
        self.length=length
    def area_(self):
        return self.length**2

sq=square(5)
print(sq.area_())
