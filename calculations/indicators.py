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
        self.indicators["Math expectation"] = math_exp
        self.indicators["Dispersion"] = disp
        self.indicators["Standard Deviation"] = stand_dev
        self.indicators["Delta"] = delta

    def set_analytical(self, math_exp, disp, stand_dev, var_coef, gamma):
        self.indicators["Math expectation"] = math_exp
        self.indicators["Dispersion"] = disp
        self.indicators["Standard Deviation"] = stand_dev
        self.indicators["Variation coefficient"] = var_coef
        self.indicators["X gamma"] = gamma
