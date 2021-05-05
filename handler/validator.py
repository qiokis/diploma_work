import re


class Validator:
    """
    Class for validation data from gui
    """

    def __init__(self):
        self.__regex = r"^[-|+]?\d+$|^[-|+]?\d+[\.|\,]\d+$"
        self.__result = ""

    def validate(self, values: dict):
        """
        Method check for correctness values from gui and invoke error message if needed
        :param values: data from gui
        :return: boolean result of validation
        """
        self.__result = ""
        for key, value in values.items():
            if not re.match(self.__regex, value):
                self.__result += f"Incorrect indicator {key}: {value}\n"
        if self.__result:
            return False
        return True

    def comma_replace(self, values: dict):
        """
        Method replace comma to dot
        :param values:
        :return:
        """
        for key, value in values.items():
            if value.count(","):
                values[key] = value.replace(",", ".")
        return values