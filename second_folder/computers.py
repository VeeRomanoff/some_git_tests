class Computer():
    def __init__(self, characteristics):
        self.__characteristics = characteristics
        # self.brand = brand
        # self.model = model
        # self.chip = chip
        # self.color = color
    
    def __iter__(self):
        for item in self.__characteristics:
            yield item
    

class Macs(Computer):
    def __init__(self, characteristics):
        super().__init__(characteristics)
        
    
class Windows(Computer):
    def __init__(self, characteristics):
        super().__init__(characteristics)
   

macbook = Macs(['Apple MacBook', 'Air', 'M1', 'space-gray'])
windows = Windows(['Xiomi', 'Mi Gaming', 'Intel Core 13', 'Black'])

if 'Intel Core 13' in windows:
    print('Naah Intel just fucked M1 ahah')
    
if 'Apple MacBook' in macbook:
    print('but still macs are the best so it beats windows lmaoo')
    
# for apple in macbook or windows:
#     if apple in macbook or windows:
#         print('it is apple anywas... go get rich already! :D')