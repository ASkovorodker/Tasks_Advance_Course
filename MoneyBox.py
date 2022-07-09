class MoneyBox:
    def __init__(self, capacity=0): # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
        self.sum = 0
        self.status = True

    def can_add(self, v): # True, если можно добавить v монет, False иначе
        if self.capacity > v:
            self.status = True
            #return True
        else:
            self.status = False
            #return False

    def add(self, v): # положить v монет в копилку. Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True.
        #self.sum += v
        self.can_add(v)
        if self.status is True:
            self.sum += v

a = MoneyBox(5)
#a.can_add(7)
a.add(3)

print(a.capacity)
print(a.sum)
