class House:
    color: str
    window_count: int

    def __init__(self, color: str, window_count: int) -> None:
        self.color=color
        self.window_count=window_count

    def get_color(self) -> str:
        return f'Elewacja budynku jest koloru:{self.color}'

    def add_windows(self, amount: int) -> None:
        self.window_count+=amount


house_1=House("blue",10)
house_2=House("red", 15)

print(f'Dom nr 1 ma {house_1.window_count} okien')
print(f'Dom nr 2 ma {house_2.window_count} okien')

house_1.add_windows(3)
print(f'Dom nr 1 ma {house_1.window_count} okien')
print(f'Dom nr 2 ma {house_2.window_count} okien')

print(house_1.get_color())
print(house_2.get_color())

house_2.color='afroamerican'
print(house_1.get_color())
print(house_2.get_color())
