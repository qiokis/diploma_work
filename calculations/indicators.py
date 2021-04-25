class Indicators:
    """
    POJO class contains indicators
    """

    indicators = {"Analytical": {"Math expectation": None,
                                 "Dispersion": None,
                                 "Standard Deviation": None,
                                 "Variation coefficient": None,
                                 "X gamma": None},
                  "Statistical": {"Math expectation": None,
                                  "Dispersion": None,
                                  "Standard Deviation": None,
                                  "Delta": None}}

    def set_statistical(self, math_exp, disp, stand_dev, delta):
        self.indicators["Statistical"]["Math expectation"] = math_exp
        self.indicators["Statistical"]["Dispersion"] = disp
        self.indicators["Statistical"]["Standard Deviation"] = stand_dev
        self.indicators["Statistical"]["Delta"] = delta

    def set_analytical(self, math_exp, disp, stand_dev, var_coef, gamma):
        self.indicators["Analytical"]["Math expectation"] = math_exp
        self.indicators["Analytical"]["Dispersion"] = disp
        self.indicators["Analytical"]["Standard Deviation"] = stand_dev
        self.indicators["Analytical"]["Variation coefficient"] = var_coef
        self.indicators["Analytical"]["X gamma"] = gamma

    def __str__(self):
        return self.indicators.__str__()

    def clear(self):
        self.indicators = {"Analytical": {"Math expectation": None,
                                          "Dispersion": None,
                                          "Standard Deviation": None,
                                          "Variation coefficient": None,
                                          "X gamma": None},
                           "Statistical": {"Math expectation": None,
                                           "Dispersion": None,
                                           "Standard Deviation": None,
                                           "Delta": None}}
