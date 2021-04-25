import re
from tkinter import messagebox as mb


class Validator:
    """
    Class for validation data from gui
    """

    def __init__(self):
        self.regex = r"^[-|+]?\d+$|^[-|+]?\d+[\.|\,]\d+$"
        self.result = ""

    def validate(self, values: dict):
        """
        Method check for correctness values from gui and invoke error message if needed
        :param values: data from gui
        :return: boolean result of validation
        """
        self.result = ""
        for key, value in values.items():
            if not re.match(self.regex, value):
                self.result += f"Incorrect indicator {key}: {value}\n"
        if self.result:
            mb.showerror("Error", self.result)
            return False
        return True