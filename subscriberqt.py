from PyQt5.QtCore import QThread
class QtSubscriber(QThread):
    def __init__(self, name):
        self.name = name
    def show_log(self, message):
        raise Exception('show_log method must be implemented by super class')
    def save_result(self, result):
        raise Exception('save_result method must be implemented by super class')
  