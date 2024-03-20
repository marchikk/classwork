
class DogSpike:
    name= 'Spike'
    def __init__(self):
        self.is_walked = False
    def walk(self):
        print('Dog walked')
        self.is_walked = True