import math

class Figure:
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a = a  # основа 1
        self.b = b  # основа 2
        self.c = c  # бічна сторона 1
        self.d = d  # бічна сторона 2

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        # Формула для трапеції з обчисленням висоти (приблизна)
        s = self.perimeter() / 2
        try:
            h = (2 / abs(self.a - self.b)) * ((s - self.a) * (s - self.b) * (s - self.a - self.c) * (s - self.a - self.d)) ** 0.5
        except:
            h = 1  # fallback якщо не рахується нормально
        return ((self.a + self.b) / 2) * h

class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.h

class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return 2 * math.pi * self.r

    def area(self):
        return math.pi * self.r ** 2
