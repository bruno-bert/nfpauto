class Subscriber:
    def __init__(self, name):
        self.name = name
    def show_log(self, message, manual_action = 0 ):
        raise Exception('show_log method must be implemented by super class')
    def save_result(self, result):
        raise Exception('save_result method must be implemented by super class')
   
class Publisher:
    def __init__(self):
        self.subscribers = set()
    def register(self, who):
        self.subscribers.add(who)
    def unregister(self, who):
        self.subscribers.discard(who)
    def show_log(self, message, manual_action = 0):
        for subscriber in self.subscribers:
            subscriber.show_log(message, manual_action)
    def save_result(self, result):
        for subscriber in self.subscribers:
            subscriber.save_result(result)     
    def init_value(self, value):
        for subscriber in self.subscribers:
            subscriber.init_value(value)  
            