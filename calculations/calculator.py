import math
from calculations.indicators import Indicators
from calculations.selection import Selection


class Calculator:
    """
    Class contains methods for calculate indicators
    """
    select: Selection
    indicator = Indicators()

    def __init__(self):
        self.__a = 0
        self.__b = 0
        self.__c = 0
        self.__c_avg = 0
        self.__kc = 0
        self.__gamma = 0

    def data_entry(self, a, b, c=None, c_avg=None, kc=None, gamma=None, n=10000):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__c_avg = c_avg
        self.__kc = kc
        self.__gamma = gamma
        self.select = Selection(self.__a, self.__b, self.__c, self.__c_avg, self.__kc, n)
        self.indicator.clear()

    def to_fixed(self, number, digits=4):
        """
        Method bring number to fixed length
        :param number: any number
        :param digits: quantity of numbers after dot
        :return: number with fixed length
        """
        return float(f"{number:.{digits}f}")

    def calculate_analytical(self):
        """
        Method calculates and save analytical indicators for model
        :return:
        """
        if self.__c:
            # Math expectation | Математическое ожидание
            expected_value = self.to_fixed((self.__a + self.__b + self.__c) / 3)
            # Dispersion | Дисперсия
            dispersion = self.to_fixed((self.__a ** 2 + self.__b ** 2 + self.__c ** 2 - self.__a * self.__b
                                        - self.__a * self.__c - self.__b * self.__c) / 18)
            # Standard deviation | Стандартное отклонение
            deviation = self.to_fixed(
                math.sqrt(2 * (self.__a ** 2 + self.__b ** 2 + self.__c ** 2 - self.__a
                               * self.__b - self.__a * self.__c - self.__b * self.__c)) / 6)
            # Variation coefficient | Коэффициент вариации
            var_coef = self.to_fixed(deviation / expected_value)
            # X gamma | X гамма
            temp = ((self.__c - self.__a) / (self.__b - self.__a))
            if temp <= self.__gamma < 1:
                x_gamma = self.to_fixed(self.__a + math.sqrt(
                    (1 - self.__gamma) * (self.__b - self.__a) * (self.__c - self.__a)))
            elif 0 < self.__gamma < temp:
                x_gamma = self.to_fixed(self.__b - math.sqrt(
                    self.__gamma * (self.__b - self.__a) * (self.__b - self.__c)))
            self.indicator.set_analytical(expected_value, dispersion, deviation, var_coef, x_gamma)

    def calculate_statistical(self):
        """
        Method calculates and save statistical indicators for model
        :return:
        """
        n = 10000
        # r1 - Математическое ожидание
        r1, r2 = self.select.generate_selection()
        r1 = self.to_fixed(r1)
        # Дисперсия
        dispersion = self.to_fixed((r2 - n * r1 * r1) / (n - 1))
        # Стандартное отклонение
        s = self.to_fixed(math.sqrt(dispersion))
        # Дельта
        delta = self.to_fixed((1.96 * s) / math.sqrt(n))
        # Доверительный интервал
        conf_int = f"{self.to_fixed(r1 - delta)} - {self.to_fixed(r1 + delta)}"
        self.indicator.set_statistical(r1, dispersion, s, conf_int)

    def get_indicators(self):
        """
        Method returns indicators
        :return: indicators
        """
        return self.indicator.indicators
