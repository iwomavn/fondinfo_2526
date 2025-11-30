from math import sqrt

class Point():
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def x(self):
        return self._x
    
    def y(self):
        return self._y
    
    def distance(self, point):
        return sqrt((self._x - point.x()) ** 2 + (self._y - point.y()) ** 2)
    
    
class LineSegment():
    def __init__(self, first, second):
        self._first = first
        self._second = second
        
    def lenght(self):
        return self._first.distance(self._second)
    
def main():
    x1 = int(input("Inserisci x primo punto: "))
    y1 = int(input("Inserisci y primo punto: "))
    primo = Point(x1, y1)
    
    x2 = int(input("Inserisci x secondo punto: "))
    y2 = int(input("Inserisci y secondo punto: "))
    secondo = Point(x2, y2)
    
    segmento = LineSegment(primo, secondo)
    print(segmento.lenght())
    
main()
    