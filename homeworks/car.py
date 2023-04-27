amount = 0


class Car:
    def __init__(self, model, color='', volume=0.0, speed=0):
        self.model = model
        self.color = color
        self.volume = volume
        self.speed = speed
        global amount
        amount += 1

    def __str__(self):
        model = 'Model is: ' + self.model
        color = 'Color is: ' + self.color if len(self.color) > 0 else ''
        volume = 'Volume is: ' + str(self.volume) if self.volume > 0.0 else ''
        speed = 'Speed is: ' + str(self.speed) if self.speed > 0 else ''
        _list = [model, color, volume, speed]
        updated_list = [item for item in _list if item != '']
        print(updated_list)

    @classmethod
    def print_cars(cls, *cars):
        for car in cars:
            car.__str__()

    def change_color(self, color):
        self.color = color


car_1 = Car('BMW')
car_2 = Car('Audi', 'green')
car_3 = Car('Skoda', 'yellow', 2.0)
car_4 = Car('Mercedes', 'black', 3.0, 250)
Car.print_cars(car_1, car_2, car_3, car_4)
print(amount, 'car' if amount == 1 else 'cars', 'created!')

car_1.change_color('white')
print('car_1 after color changing -> ', end='')
Car.print_cars(car_1)
