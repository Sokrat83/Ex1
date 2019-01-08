
class Point:

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def point_x(self, x):
        self.__x = x

    @y.setter
    def point_x(self, y):
        self.__y = y

    def move_to(self, x, y):
        self.__x = x
        self.__y = y

    def move_by(self, x, y):
        self.__x += x
        self.__y += y

    def __repr__(self):
         return "I`m a point {0}x{1}".format(self.__x, self.__y)


point = Point(10, 20)
print(point)

point.move_to(100, 200)
print(point.x, ":", point.y)

point.move_by(10, 20)
print(point)

