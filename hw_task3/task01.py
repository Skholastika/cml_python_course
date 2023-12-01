class Rectangle:
    def __init__(self, w=1, h=1):
        self._width = w
        self._height = h
        print(f'Rectangle created. Width is {self._width} and height is {self._height}.')

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2*(self._width + self._height)


# rec = Rectangle(5, 3)
# print(rec.area(), rec.perimeter())
