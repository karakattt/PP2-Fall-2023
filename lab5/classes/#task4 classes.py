#task4 classes
class point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def show(self):
        print(self.x, self.y)

    def move(self, a, b):
        self.x=a
        self.y=b

    def distance(self, oth):
        dx=self.x-oth.x
        dy=self.y-oth.y
        dist=(dx**2 + dy**2)**0.5
        return dist
p1=point(1,2)
p2=point(4,6)
 
p1.show()
p2.show()

print(round(p1.distance(p2),3))

