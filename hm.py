class DogRex:
    name = 'Rex'
    def __init__(self):
        self.is_walked = False
    def walk(self):
        print('Dog walked')
        self.is_walked = True


my_dog = DogRex()
print('my dog name:', my_dog.name) # Rex
print('my dog voice:', my_dog.voice) # bow-wow
print('my dog is hungry:', my_dog.hungry) # True
my_dog.feed()
print('my dog is hungry:', my_dog.hungry) # False
my_dog.walk()
print('my dog is hungry:', my_dog.hungry) # True