import json


def main():
    class Dog:
        def __init__(self, name, breed, gender, food, water):
            self.name = name
            self.breed = breed
            self.gender = gender
            self.food = food
            self.water = water

        def feed(self):
            if self.food < 5:
                self.food += 1
                print(f'{self.name} is hungry. {self.food} out of 5.')
            if self.food == 5:
                print(f'{self.name} is not hungry. {self.food} out of 5.')
                print(f'{self.name} needs to poo!')

        def refill_water(self):
            if self.water < 5:
                self.water += 1
                print(f'{self.name} is thirsty. {self.water} out of 5.')
            if self.water == 5:
                print(f'{self.name} is not thirsty. {self.water} out of 5.')
                print(f'{self.name} needs to pee!')

        def poo(self):
            self.food = 0
            print(f'{self.name} says: "Ahhh much better!"')

        def pee(self):
            self.water = 0
            print(f'{self.name} says: "Ahhh much better!"')

        def cuddle(self):
            pass

        def growl(self):
            pass

        def bark(self):
            pass

        def train(self):
            pass

        def give_treat(self):
            pass

        def walk(self):
            behavior = input(f'Is {self.name} being a good {self.gender}? Type y/n:')

            if behavior == 'y':
                print(f'\nGive {self.name} a treat!')
            elif behavior == 'n':
                print(f'Observe what is triggering {self.name} and think of ways to avoid this in the future...')

            if self.food > 0:
                self.food = self.food - 1
            if self.water > 0:
                self.water = self.water - 1

        def notifications(self):
            pass

    class DogEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, Dog):
                return {'name': o.name, 'breed': o.breed, 'gender': o.gender, 'food': o.food, 'water': o.water}

            raise TypeError(f'Object {o} is not of type Dog.')

    def register():
        print('Dog Registration')
        name = input('Enter name: ')
        breed = input('Enter breed: ')
        gender = input('Enter gender: ')
        new_dog = Dog(name, breed, gender, 0, 0)
        json_new_dog = json.dumps(new_dog, cls=DogEncoder, indent=4)

        with open('json\data', 'w') as f:
            f.write(json_new_dog)

        print(f'{new_dog.name} is now registered!')

    def menu():
        print("\nMain Menu\n"
              "1. Register\n"
              "2. Walk\n"
              "3. Feed\n"
              "4. Refill Water\n"
              "5. Train\n"
              "6. Pee\n"
              "7. Poo\n"
              "8. Exit Simulator"
              )

    print('Welcome to Dog Simulator!')
    luna = Dog('Luna', 'Cocker Spaniel', 'girl', 0, 0)

    while True:
        luna.notifications()
        menu()
        option = int(input('Select an option: '))
        if option == 1:
            register()
        if option == 2:
            luna.walk()
        if option == 3:
            luna.feed()
        if option == 4:
            luna.refill_water()
        if option == 5:
            pass
        if option == 6:
            pass
        if option == 7:
            pass
        if option == 8:
            print('Thank you for using Dog Simulator. Good bye!')
            break


if __name__ == '__main__':
    main()
