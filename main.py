import json


def main():
    class Owner:
        def __init__(self, name):
            self.name = name

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
                print(f'{self.name} is still hungry. Hunger Level: {self.food}/5.')
            if self.food == 5:
                print(f'{self.name} is not hungry. Hunger Level: {self.food}/5.')
                print(f'You need to take {self.name} outside to poo.')

        def refill_water(self):
            if self.water < 5:
                self.water += 1
                print(f'{self.name} is still thirsty. Thirst Level: {self.water}/5.')
            if self.water == 5:
                print(f'{self.name} is not thirsty. Thirst Level: {self.water}/5.')
                print(f'You need to take {self.name} outside to pee.')

        def poo(self):
            self.food = 0
            print(f'{self.name} says: "Ahhh much better!"')

        def pee(self):
            self.water = 0
            print(f'{self.name} says: "Ahhh much better!"')

        def train(self):
            pass

        def walk(self):
            if self.food == 0 or self.water == 0:
                print(f'You need to feed and refill water for {self.name} before going on a walk.')
            else:
                behavior = input(f'Is {self.name} being a good {self.gender}? Type y/n:')
                if behavior == 'y':
                    print(f'\nGive {self.name} a treat!')
                elif behavior == 'n':
                    print(f'Observe what is triggering {self.name} and think of ways to avoid this in the future.')
                self.food = self.food - 1
                self.water = self.water - 1

        def adoption(self):
            pass

        def veterinarian(self):
            print('\nWelcome to the Veterinary Center!\n'
                  '1. Wellness Examination\n'
                  '2. Emergency')
            choice = input('Select an option: ')
            if choice == 1:
                print('Checking for symptoms...')
            if choice == 2:
                print('Emergency List\n'
                      '1. Acute Vomiting'
                      '2. Poisoning'
                      '3. Trauma')
                another_choice = input('Select an option: ')
                if another_choice == 1:
                    print(f'{self.name} is going to be okay. Here is some anti-nausea medication. Goodbye!')
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
              "8. Veterinarian\n"
              "9. Adoption\n"
              "10. Exit"
              )

    print('\nWelcome to Dog Simulator!')
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
