class Circle():
    def __init__(self, r):
        self.radius = r

    def getArea(self):
        return self.radius ** 2 * 3.14

    def getPerimeter(self):
        return 2 * 3.14 * self.radius

c = Circle(7)
print(c.getArea())

c = Circle(8.88)
print(c.getPerimeter())