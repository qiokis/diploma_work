import math
import random


class Selection:
    """
    Class contains all selection data and related staff
    """

    selection = []

    def __init__(self, a, b, c, c_avg, kc, n):
        self.a = a
        self.b = b
        self.c = c
        self.c_avg = c_avg
        self.kc = kc
        self.n = n

    def generate_selection(self):
        """
        Method generates selection
        :return:
        """
        self.selection.clear()
        # Накопление x-ов
        r1 = 0
        # Накопление x-ов в квадрате
        r2 = 0
        if not self.c:
            c1 = self.c_avg * (1 - math.sqrt(3) * self.kc)
            c2 = self.c_avg * (1 + math.sqrt(3) * self.kc)
        for i in range(self.n):
            #  x между 0 и 1 (Равномерное распределение по алгоритму моделирования (7))
            random_value = random.uniform(0, 1)
            # Если c не задан точно
            if not self.c:
                self.c = c1 + (c2 - c1) * random.uniform(0, 1)
            temp = 0
            if 0 < random_value <= (self.c - self.a) / (self.b - self.a):
                temp = self.a + math.sqrt(random_value * (self.b - self.a) * (self.c - self.a))
            elif (self.c - self.a) / (self.b - self.a) < random_value < 1:
                temp = self.b - math.sqrt((1 - random_value) * (self.b - self.a) * (self.b - self.c))
            self.selection.append(temp)
            r1 += temp
            r2 += temp ** 2
        r1 /= self.n
        return r1, r2