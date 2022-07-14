class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, v):
        if self.capacity >= v:
            return True
        else:
            return False

    def add(self, v):
        self.capacity = self.capacity - v


a = MoneyBox(15)
a.add(5)
a.add(9)
a.add(3)
