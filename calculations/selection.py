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
        self.x_array = list()

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

    def create_arrays(self, j, gamma):
        """
        Method creates a additional arrays for main selection
        :param j: quantity of intervals
        :param gamma: gamma indicator
        :return: all calculated arrays
        """
        # Шаг
        lamb = (self.b - self.a) / j

        result = dict()

        self.x_array.append(self.a)
        # Содержит j подмассивов со значениями от X[j] до X[j+1]
        uzli = [[] for _ in range(j)]

        for i in range(j):
            self.x_array.append(self.x_array[i] + lamb)

        for value in self.selection:
            index = math.floor((value - self.a) / lamb)
            uzli[index].append(value)

        # Сортировка подмасивов (можно убрать)
        for i in range(len(uzli)):
            uzli[i] = sorted(uzli[i])

        # Массив содержащий частоты
        counts = []
        # Подсчет частот
        for i, vals in enumerate(uzli):
            counts.append(len(vals))

        m = []
        k = []
        for i in range(j):
            m.append(sum([counts[j] for j in range(i + 1)]))
            m[i] /= self.n
            k.append(1 - m[i])
        result.update({"uzli": uzli, "counts": counts, "m": m, "k": k})
        result.update(self.define_xr_indicators(self.x_array, k, gamma, j))

        return result

    def define_xr_indicators(self, x_arr, k_arr, gamma, j):
        """
        Method calculates Xr and Xr gamma
        :param x_arr: array in the range of a and b
        :param k_arr: statistical array
        :param gamma: gamma indicator
        :param j: quantity of intervals
        :return:
        """
        xr = x_arr[0] + ((x_arr[j] - x_arr[0]) / j) * (0.5 + sum(k_arr[1:-1]))
        index = 0
        for key, value in enumerate(k_arr[1:-1]):
            if gamma >= value:
                index = key + 1
                break
        xr_gamma = x_arr[index - 1] + ((gamma - k_arr[index - 1]) / (k_arr[index] - k_arr[index - 1])) * \
                   (j / (x_arr[j] - x_arr[0]))
        return {"xr": xr, "xr_gamma": xr_gamma}
