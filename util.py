import re
class Util:
    def __init__(self):
        pass
    
    @staticmethod
    def remove_special_chars(str):
        return re.sub('[^0-9]', '', str)    
