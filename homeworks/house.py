class House:
    door_square = 1.5
    window_square = 2.5

    def __init__(self, doors=1, windows=2, houses=1):
        self.doors = doors
        self.windows = windows
        self.houses = houses

    def get_total_doors_and_windows_square(self):
        return (self.windows * self.window_square + self.doors * self.door_square) * self.houses

    def __str__(self):
        door_str = 'door' if self.doors == 1 else 'doors'
        window_str = 'window' if self.windows == 1 else 'windows'
        is_or_are = 'is' if self.houses == 1 else 'are'
        house_str = 'house' if self.houses == 1 else 'houses'
        return (f'There {is_or_are} {self.houses} {house_str} with {self.doors} {door_str} '
                f'and {self.windows} {window_str}. '
                f'Total square of doors and windows is: {self.get_total_doors_and_windows_square()}')


house1 = House()
house2 = House(1, 10)
house3 = House(1, 10, 2)
print(house1)
print(house2)
print(house3)
