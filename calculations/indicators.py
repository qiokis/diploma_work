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
                                  "Conf int": None,
                                  "Xr": None,
                                  "Xr gamma": None}
                  }

    def set_statistical(self, math_exp, disp, stand_dev, conf_int):
        """
        Method save values to dict
        :param xr_gamma: xr gamma
        :param xr: xr
        :param math_exp: math expectation
        :param disp: dispersion
        :param stand_dev: standard deviation
        :param delta: delta
        :return:
        """
        self.indicators["Statistical"]["Math expectation"] = math_exp
        self.indicators["Statistical"]["Dispersion"] = disp
        self.indicators["Statistical"]["Standard Deviation"] = stand_dev
        self.indicators["Statistical"]["Conf int"] = conf_int

    def set_xrs(self, values):
        self.indicators["Statistical"]["Xr"] = values["xr"]
        self.indicators["Statistical"]["Xr gamma"] = values["xr_gamma"]

    def set_analytical(self, math_exp, disp, stand_dev, var_coef, gamma):
        """
        Method save values to dict
        :param math_exp: math expectation
        :param disp: dispersion
        :param stand_dev:standard deviation
        :param var_coef: variation coefficient
        :param gamma: x gamma
        :return:
        """
        self.indicators["Analytical"]["Math expectation"] = math_exp
        self.indicators["Analytical"]["Dispersion"] = disp
        self.indicators["Analytical"]["Standard Deviation"] = stand_dev
        self.indicators["Analytical"]["Variation coefficient"] = var_coef
        self.indicators["Analytical"]["X gamma"] = gamma

    def __str__(self):
        """
        Method present a string format of indicators
        :return:
        """
        return self.indicators.__str__()

    def clear(self):
        """
        Method clears indicators dict
        :return:
        """
        self.indicators = {"Analytical": {"Math expectation": None,
                                          "Dispersion": None,
                                          "Standard Deviation": None,
                                          "Variation coefficient": None,
                                          "X gamma": None},
                           "Statistical": {"Math expectation": None,
                                           "Dispersion": None,
                                           "Standard Deviation": None,
                                           "Delta": None}}
