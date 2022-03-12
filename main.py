import json


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

    def poo(self):
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


def register():
    print('Dog Simulator Registration')
    name = input('Enter name: ')
    breed = input('Enter breed: ')
    # x = Dog(name, breed, 0, 0)


class DogEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Dog):
            return {'name': o.name, 'breed': o.breed, 'food': o.food, 'water': o.water}

        raise TypeError(f'Object {o} is not of type Dog.')


woo = Dog('Woo', 'cocker', 0, 0)
json_woo = json.dumps(woo, cls=DogEncoder, indent=4)
print(json_woo)

with open('json\data', 'w') as file:
    file.write(json_woo)
