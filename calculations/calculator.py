import math
import indicators
import selection


class Calculator:
    """
    Class contains methods for calculate indicators
    """

    indicator = indicators.Indicators()

    def __init__(self, a, b, c, c_avg, kc, gamma):
        self.a = a
        self.b = b
        self.c = c
        self.c_avg = c_avg
        self.kc = kc
        self.gamma = gamma
        self.select = selection.Selection(self.a, self.b, self.c, self.c_avg, self.kc, 10000)

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
        # Math expectation | Математическое ожидание
        expected_value = self.to_fixed((self.a + self.b + self.c) / 3)
        # Dispersion | Дисперсия
        dispersion = self.to_fixed((self.a ** 2 + self.b ** 2 + self.c ** 2 - self.a * self.b
                                    - self.a * self.c - self.b * self.c) / 18)
        # Standard deviation | Стандартное отклонение
        deviation = self.to_fixed(math.sqrt(2 * (self.a ** 2 + self.b ** 2 + self.c ** 2
                                                 - self.a * self.b - self.a * self.c - self.b * self.c)) / 6)
        # Variation coefficient | Коэффициент вариации
        var_coef = self.to_fixed(deviation / expected_value)
        # X gamma | X гамма
        x_gamma = self.to_fixed(self.a + math.sqrt((1 - self.gamma) * (self.b - self.a) * (self.c - self.a)))
        self.indicator.set_analytical(expected_value, dispersion, deviation, var_coef, x_gamma)

    def calculate_statistical(self):
        """
        Method calculates and save statistical indicators for model
        :return:
        """
        n = 10000
        # r1 - Математическое ожидание
        r1, r2 = self.select.generate_selection()
        # Дисперсия
        dispersion = self.to_fixed((r2 - n * r1 * r1) / (n - 1))
        # Стандартное отклонение
        s = self.to_fixed(math.sqrt(dispersion))
        # Дельта
        delta = self.to_fixed((1.96 * s) / math.sqrt(n))
        self.indicator.set_statistical(r1, dispersion, s, delta)

if __name__ == '__main__':
    c = Calculator(1, 12, 5, 0, 0, 0)
    c.calculate_statistical()