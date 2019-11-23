import re
from enum import Enum

class Util:
    def __init__(self):
        pass
    
    @staticmethod
    def remove_special_chars(str):
        return re.sub('[^0-9]', '', str)    


class VideoStatus(Enum):
     IDLE = 1
     WARMING = 2
     IN_PROGRESS = 3