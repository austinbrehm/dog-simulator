import json


def main():
    class Dog:
        def __init__(self, name, breed, food, water):
            self.name = name
            self.breed = breed
            self.food = food
            self.water = water

        def feed(self):
            if self.food < 5:
                self.food += 1
                print('{} food is {} out of 5.'.format(self.name, self.food))
            if self.food == 5:
                print('{} food is {} out of 5. {} is not hungry...'.format(self.name, self.food, self.name))

        def refill_water(self):
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

    class DogEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, Dog):
                return {'name': o.name, 'breed': o.breed, 'food': o.food, 'water': o.water}

            raise TypeError(f'Object {o} is not of type Dog.')

    def register():
        print('Dog Registration')
        name = input('Enter name: ')
        breed = input('Enter breed: ')
        new_dog = Dog(name, breed, 0, 0)
        json_new_dog = json.dumps(new_dog, cls=DogEncoder, indent=4)

        with open('json\data', 'w') as f:
            f.write(json_new_dog)

        print(f'{new_dog.name} is now registered!')

    def menu():
        print("Welcome to Dog Simulator!\n"
              "1: Register\n"
              "2. Walk\n"
              "3. Feed\n"
              "4. Refill Water\n"
              "5. Train\n"
              "6. Exit Simulator"
              )

    while True:
        menu()
        option = int(input('Select an option: '))
        if option == 1:
            register()
        if option == 2:
            pass
        if option == 3:
            # access object from storage
            pass
        if option == 4:
            pass
        if option == 5:
            pass
        if option == 6:
            print('Thank you for using Dog Simulator. Good bye!')
            break


if __name__ == '__main__':
    main()
