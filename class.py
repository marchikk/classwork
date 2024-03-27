
class Dog:
    name = 'unknown'
    def __init__(self, breed , speed):
        self.is_walked = False
        self.speed = speed
        self.breed = breed
        self.tricks = []

    def walk(self):
        print(f'dog {self.name} walks')
        self.is_walked = True

    def learn_tricks(trick):
        self.tricks += [trick] 

    def do_tricks(self):
        for trick in self.tricks:
            print(f'dog{self.name} of breed {self.breed} performs trick{trick}')
        if self.tricks ==[]:
            print(f'')
    

class DogSpike(Dog):
    name = 'Spike'

    def run(self):
        print(f'dog{self.name} is running {self.speed} km/h and is hungry')

class DogMike(Dog):
    name = 'Mike'

    def run(self):
        print(f'dog{self.name} is running {self.speed} km/h and is thirsty')

my_dog = DogSpike('bulldog' , 12)
friends_dog = DogMike('pitbull', 20)
my_dog.learn_trick('sit down')
print(f'my dog name is {my_dog.name}')
print(f'my dog speed is {my_dog.speed} km/h')
print(f'my friend\'s dog name is {friends_dog.name}')
print(f'my friend\'s dog speed is {friends_dog.speed}')
my_dog.run()
friends_dog.run()

