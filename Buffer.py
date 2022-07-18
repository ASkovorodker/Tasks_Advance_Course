class Buffer:
    def __init__(self):
        buf = []
        self.buf = buf

    def add(self, *a):
        for i in a:
            self.buf.append(i)
        while len(self.buf) >= 5:
            slc = self.buf[0:5]
            print(sum(slc))
            del self.buf[0:5]

    def get_current_part(self):
        return self.buf


q = Buffer()
q.add(1, 2, 3)
q.get_current_part() # вернуть [1, 2, 3]
q.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
q.get_current_part() # вернуть [6]
q.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
q.get_current_part() # вернуть []
q.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
q.get_current_part() # вернуть [1]
