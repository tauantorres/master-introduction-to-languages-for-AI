class Point:
    def __init__(self,xx,yy):
        self.x=xx
        self.y=yy
        
    def whoareyou (self):
        return self.x,self.y
    
    def move(self,delta):
        self.x+=delta
        self.y+=delta

class ColPoint_Bad(Point):
    def __init__(self,xx,yy,cc):
        self.x = xx
        self.y = yy
        self.color = cc
        
    def whoareyou (self):
        return (self.x, self.y) + (self.color, )
    
    
class ColPoint(Point):
    def __init__(self,xx,yy,cc):
        super().__init__(xx, yy)
        self.color = cc
        
    def whoareyou (self):
        return super().whoareyou() + (self.color, )