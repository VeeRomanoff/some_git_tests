class Animal():
    def __init__(self, animal, color , is_haunter):
        self.animal = animal
        self.color = color
        self.is_haunter = is_haunter
        
    def roar(self):
        if self.is_haunter == True:
            return print("Roarrrrr >.<")
        else:
            return print('This animal is not a haunter :<')
    
    def make_sound(self):
        if self.is_haunter == False:
            return print('Moo-o')
        else:
            return self.roar()

pingeon = Animal('Pingeon', 'grey', False)
pingeon.roar() 
pingeon.make_sound()           

tiger = Animal('Tiger', 'orange', True)
tiger.roar()
tiger.make_sound()
            