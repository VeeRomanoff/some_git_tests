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

class Arconians(Human):
    def __init__(self, name, last_name, dignity):
        super().__init__(name, last_name)
        self.name = name
        self.last_name = last_name
        self.dignity = dignity
    
    def make_sound(self):
        return 'Woo-aao-bip-bop!'
    
    def show(self):
        return print(f'{self.make_sound()} My name is {self.make_sound()} Pogo Zoic.. i am the {self.dignity}')
    

pogo = Arconians('Pogo', 'Zoic', 'Emperor')
pogo.show()

class Babies(Human):
    def __init__(self, name, last_name, height, weight, eye_size):
        super().__init__(name, last_name)
        self.height = height
        self.weight = weight
        self.eye_size = eye_size
    
    def cry(self):
        if self.eye_size == 'Big':
            return 'damn, so much tears'
        elif self.eye_size == 'Medium':
            return 'gosh... stop crying!'
        else:
            return 'so little tearssss :D'
    

alex = Babies('Alex', 'O\'Brien', 60, 6, 'Big')
print(alex.cry())
        