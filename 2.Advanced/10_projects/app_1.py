class Point:
    # self can be any name
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # def __init__(this_object, x, y):
    #     this_object.x = x
    #     this_object.y = y

    # def falls_in_rectangel(self, lowleft, upright):
    #     if lowleft[0] < self.x < upright[0] \
    #     and lowleft[1] < self.y < upright[1]:
    #         return True
    #     else:
    #         return False 

    def falls_in_rectangel(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x \
        and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False 


    # def distance_from_point(self, x, y):
    #     return ((self.x - x)**2 + (self.y -y)**2) ** 0.5
    
    def distance_from_point(self,point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2) ** 0.5

class Rectangle:
    def __init__(slef, lowleft, uprihgt):
        self.lowleft = lowleft
        self.upright = upright

    # ractanglex = Rectangle(Point(5, 6), Point(7, 9))