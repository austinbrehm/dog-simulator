class Dog:
    def __init__(self, name, breed, food, water):
        self.name = name
        self.breed = breed
        self.food = food
        self.water = water

    def eat(self):
        if self.food < 5:
            self.food += 1
            print('{} food is {} out of 5.'.format(self.name, self.food))
        if self.food == 5:
            print('{} food is {} out of 5. {} is not hungry...'.format(self.name, self.food, self.name))

    def drink(self):
        if self.water < 5:
            self.water += 1
            print('{} water is {} out of 5.'.format(self.name, self.water))
        if self.water == 5:
            print('{} water is {} out of 5. {} is not thirsty...'.format(self.name, self.food, self.name))

    def poop(self):
        pass

    def pee(self):
        pass

    def cuddle(self):
        pass

    def growl(self):
        pass

    def bark(self):
        pass

    def train(self):
        pass

    def walk(self):
        pass


print('Dog Simulator Registration')
name = input('Enter name: ')
breed = input('Enter breed: ')
woo = Dog(name, breed, 0, 0)

