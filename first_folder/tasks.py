class Human():
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
    
    def say_something(self):
        return "hello"
    
    def show(self):
        return print(f'{self.name} says {self.say_something()} to you!')

jackson = Human('Jackson', 'O\'brien')
jackson.show()

        