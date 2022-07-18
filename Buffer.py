class Buffer:
    def __init__(self):
        buf = []
        self.buf = buf

    def add(self, *a):
        for i in a:
            self.buf.append(i)
        while len(self.buf) >= 5:
            print(sum(self.buf))
            del self.buf[0:5]


    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
        # добавлены
        return print(self.buf)

q = Buffer()
q.add(1, 2, 3)
q.get_current_part()
q.add(4, 5, 6, 1, 1, 0, 2, 3)
q.get_current_part()
