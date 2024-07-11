class Vehicle:
    __COLOR_VARIANTS = ['red', 'green', 'blue', 'black', 'white']

    def _is_valid_color(self, color):
        if color.lower() in self.__COLOR_VARIANTS:
            return color.lower()
        else:
            print(f'Нельзя установить цвет {color}')
            return None

    def __new__(self, owner, model, color, engine_power):
        if not self._is_valid_color(self, color):
            return None
        return super().__new__(self)

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_owner(self):
        return self.owner

    def get_model(self):
        return print(f'Модель : {self.__model}')

    def get_horsepower(self):
        return print(f'Мощность двигателя : {self.__engine_power} л.с.')

    def get_color(self):
        return print(f'Цвет : {self.__color}')

    def set_owner(self, owner):
        self.owner = owner

    def set_color(self, new_color):
        self.__color = self._is_valid_color(new_color)


    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец : {self.owner}')

    def __str__(self):
        return f'Owner: {self.owner}, Model: {self.__model}, Engine power: {self.__engine_power}, Color: {self.__color}'


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)


if __name__ == '__main__':
    # Пытаемся создать объект с недопустимым цветом
    vehicle0 = Sedan('Fedor', 'Toyota Mark II', 'Yellow', 500)
    print(vehicle0)  # Возвращает None. Объект не был создан

    vehicle1 = Sedan('Fedor', 'Toyota Mark II', 'blue', 500)
    print(vehicle1)

    # Изначальные свойства
    vehicle1.print_info()

    # Меняем свойства (в т.ч. вызывая методы)
    vehicle1.set_color('Pink')
    vehicle1.set_color('BLACK')
    vehicle1.owner = 'Vasyok'

    # Проверяем что поменялось
    vehicle1.print_info()

