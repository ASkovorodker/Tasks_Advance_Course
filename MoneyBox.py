class MoneyBox:
    def __init__(self, capacity=0, saving=0): # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
        self.saving = saving
        #self.free = 0
        #self.status = True

    def can_add(self, v): # True, если можно добавить v монет, False иначе
        # проверяем в can_add можно ли положить монету в копилку (если мы положим монету в копилку, не привысит ли она capacity?)
        if self.capacity > (self.saving + v):
            #self.status = True
            return True
        else:
            #self.status = False
            return False

    def add(self, v): # положить v монет в копилку. Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True.
        if self.can_add(v) is True: # проверяем в add, что вернула can_add. если все хорошо, добавляем монеты в копилку и возвращаем True или False
        #if self.status is True:
            self.saving += v
            self.capacity = self.capacity - self.saving
            return self.capacity
        #else:
            #self.free = self.capacity - self.saving
            #return self.free

a = MoneyBox(15)
a.add(5)
a.add(9)
a.add(3)


#Не забывайте, что результат нужно вывести исключительно через return.
# Никаких print'ов. Вывести нужно can_add: True/False и
# Внимание! add: доступное число монет, которое можно внести (Напр.: Capacity = 10. Внесли 5. Осталось 5. Это наш ответ).
