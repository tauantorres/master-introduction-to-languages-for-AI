class Count:
    def __init__(self, start=0):
        if type(start) != int:
            raise TypeError(str(start)+" is not an integer")
        if start < 0:
            raise ValueError(str(start)+" is not >=0")
        self.current_count = start
    def inc(self):
        self.current_count += 1