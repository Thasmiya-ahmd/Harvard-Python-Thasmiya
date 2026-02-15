class jar:
    def __init__(self,capacity=12):
        self.capacity=capacity
        self.size=0
        if self.capacity<0:
            raise ValueError("capacity cannot be negative")
    def __str__(self):
        return self.size*"🍪"
    def deposit(self,n):
        self.size+=n
        if self.size>self.capacity:
            raise ValueError("Exceeds capacity")
    def withdraw(self,n):
        self.size-=n
        if self.size<1:
            raise ValueError("Jar is empty")
    @property
    def capacityy(self):
        return self.capacity
    @property
    def sizee(self):
        return self.size
