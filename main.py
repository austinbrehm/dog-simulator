import json


def main():
    class Dog:
        number_of_dogs = 0

        def __init__(self, name, breed, gender, food, water):
            self.name = name
            self.breed = breed
            self.gender = gender
            self.food = food
            self.water = water
            Dog.add_dog()

        @classmethod
        def number_of_dogs_(cls):
            return cls.number_of_dogs

        @classmethod
        def add_dog(cls):
            cls.number_of_dogs += 1

        def get_name(self):
            return self.name

        def set_name(self, name):
            self.name = name

        def get_breed(self):
            return self.breed

        def set_breed(self, breed):
            self.breed = breed

        def get_gender(self):
            return self.gender

        def set_gender(self, gender):
            self.gender = gender

        def get_food(self):
            return self.food

        def set_food(self, food):
            self.food = food

        def get_water(self):
            return self.water

        def set_water(self, water):
            self.water = water

        def eat(self):
            if self.food < 5:
                self.food += 1
                print(f'{self.name} is still hungry. Hunger Level: {self.food}/5.')
            if self.food == 5:
                print(f'{self.name} is not hungry. Hunger Level: {self.food}/5.')
                print(f'You need to take {self.name} outside to poo.')

        def drink_water(self):
            if self.water < 5:
                self.water += 1
                print(f'{self.name} is still thirsty. Thirst Level: {self.water}/5.')
            if self.water == 5:
                print(f'{self.name} is not thirsty. Thirst Level: {self.water}/5.')
                print(f'You need to take {self.name} outside to pee.')

        def poo(self):
            if self.food == 0:
                print(f'{self.name} does not need to poo right now.')
            if self.food > 0:
                self.food = 0
                print(f'{self.name} went poo. Make sure you pick up and dispose of the waste.')

        def pee(self):
            if self.water == 0:
                print(f'{self.name} does not need to pee right now.')
            if self.water > 0:
                self.water = 0
                print(f'{self.name} went pee.')

        def walk(self):
            if self.food == 0 or self.water == 0:
                print(f'You need to feed and refill water for {self.name} before going on a walk.')
            else:
                behavior = input(f'Is {self.name} being a good {self.gender}? Type y/n:')
                if behavior == 'y':
                    print(f'Give {self.name} a treat!')
                elif behavior == 'n':
                    print(f'Observe what is triggering {self.name} and think of ways to avoid this in the future.')
                self.food = self.food - 1
                self.water = self.water - 1

        def veterinarian(self):
            print('\nWelcome to the Veterinary Center!\n'
                  '1. Wellness Examination\n'
                  '2. Emergency')
            choice = int(input('Select an option: '))
            if choice == 1:
                print('Checking for symptoms...')
            if choice == 2:
                print('\nEmergency List\n'
                      '1. Acute Vomiting'
                      '\n2. Poisoning'
                      '\n3. Trauma')
                another_choice = int(input('Select an option: '))
                if another_choice == 1:
                    print(f'{self.name} is going to be okay. Give {self.name} anti-nausea medication. Goodbye!')
                if another_choice == 2:
                    print(f'We need to monitor {self.name} overnight. Please feel free to stay through the night.')
                if another_choice == 3:
                    print(f'{self.name} has a broken leg. We applied a cast. {self.name} will be okay. Goodbye!')

        def notifications(self):
            print('\nNotifications:')
            if self.food == 0:
                print(f'You need to feed {self.name}.')
            if self.water == 0:
                print(f'You need to refill water for {self.name}.')
            if self.food == 5:
                print(f'You need to take {self.name} outside to poo.')
            if self.water == 5:
                print(f'You need to take {self.name} outside to pee.')

    class DogEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, Dog):
                return {'name': o.name, 'breed': o.breed, 'gender': o.gender, 'food': o.food, 'water': o.water}
            raise TypeError(f'Object {o} is not of type Dog.')

    def register():
        print('\nDog Registration')
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
              "3. Eat\n"
              "4. Drink Water\n"
              "5. Train\n"
              "6. Pee\n"
              "7. Poo\n"
              "8. Veterinarian\n"
              "9. Adopt\n"
              "10. Exit"
              )

    print('\nWelcome to Dog Simulator!')
    luna = Dog('Luna', 'Cocker Spaniel', 'girl', 0, 0)
    print(f'Number of Dogs: {Dog.number_of_dogs_()}')

    while True:
        luna.notifications()
        menu()
        option = int(input('Select an option: '))
        if option == 1:
            register()
        if option == 2:
            luna.walk()
        if option == 3:
            luna.eat()
        if option == 4:
            luna.drink_water()
        if option == 5:
            pass
        if option == 6:
            luna.pee()
        if option == 7:
            luna.poo()
        if option == 8:
            luna.veterinarian()
        if option == 9:
            pass
        if option == 10:
            print('Thank you for using Dog Simulator. Good bye!')
            break


if __name__ == '__main__':
    main()
