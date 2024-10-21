class Point:
    origin=0,0
    def __init__(self,xx,yy):
        self.x=xx
        self.y=yy
    def reset(self):
        self.x, self.y=Point.origin
    def whoareyou(self):
        return self.x,self.y
    def move(self,delta):
        self.x += delta
        self.y += delta
    def __add__(self,other):
        return Point(self.x+other.x, self.y+other.y)
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
    def __eq__(self,other):
        if type(other)!=Point:
            return False
        return self.x==other.x and self.y==other.y
    def __str__(self):
        return 'Point('+str(self.x)+', '+str(self.y)+')'
    