class Point:
    def __init__(self,xx,yy):
        self.x=xx
        self.y=yy
    def chisei (self):
        return self.x,self.y

class ColPoint(Point):
    def __init__(self,xx,yy,col):
        super().__init__(xx,yy)
        self.c=col
    def origin(self):
        self.x,self.y=0,0
