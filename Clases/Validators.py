from PyQt6.QtGui import QValidator
import re

class OnlyLettersValidator(QValidator):
    def validate(self, input_str, pos):
        pattern = re.compile("[A-Za-z ]+")
        if pattern.fullmatch(input_str):  
            return (QValidator.State.Acceptable, input_str, pos)
        else:
            return (QValidator.State.Invalid, input_str, pos)
