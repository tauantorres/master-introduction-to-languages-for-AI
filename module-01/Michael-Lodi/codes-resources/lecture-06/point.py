class Point:
    def __init__(self):
        self.x=0
        self.y=0
    def whoareyou (self):
        return self.x, self.y
    def move(self, delta):
        self.x+=delta
        self.y+=delta
    def __str__(self):
        return 'Point'+str(self.whoareyou())
