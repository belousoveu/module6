import math


class Figure:
    sides_count = 0

    @staticmethod
    def __is_valid_color(r, b, g):
        if not (isinstance(r, int) and isinstance(b, int) and isinstance(g, int)):
            return False
        if r < 0 or r > 255 or b < 0 or b > 255 or g < 0 or g > 255:
            return False
        return True

    @classmethod
    def __is_valid_sides(cls, *new_sides):
        if len(new_sides) != cls.sides_count:
            return False
        for s in new_sides:
            if not isinstance(s, int):
                return False
            if s < 0:
                return False
        return True

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return (f'{self.__class__.__name__}(sides :{self.__sides}, colors: {self.__color}, '
                f'{"filled" if self.filled else "not filled"})')

    def __init__(self, color, *sides):
        # Проверяем что переданные параметры sides являются целыми положительными числами
        # Иначе выбрасываем исключение
        for s in sides:
            if not isinstance(s, int):
                raise ValueError('Параметры должны быть целыми числами')
            if s < 0:
                raise ValueError('Параметры должны быть положительными числами')
        # Проверяем что переданные параметры color являются допустимыми значениями при инициализации объекта
        # Иначе выбрасываем исключение
        if not isinstance(color, tuple):
            raise ValueError('Параметр color должен быть кортежем')
        if len(color) != 3:
            raise ValueError('Параметр color должен быть кортежем из 3 элементов')
        for c in color:
            if not isinstance(c, int) or c > 255 or c < 0:
                raise ValueError('Значения цветов должны быть целыми числами в диапазоне от диапазона [0, 255]')
        if len(sides) != self.sides_count:
            sides = [1] * self.sides_count
        self.__sides = list(sides)
        self.__color = list(color)

    def get_color(self):
        return self.__color

    def set_color(self, r, b, g):
        if self.__is_valid_color(r, b, g):
            self.__color = [r, b, g]

    def get_sides(self):
        return self.__sides

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)

    def __setattr__(self, key, value):
        if key == '_Figure__color':
            self.filled = value != [255, 255, 255]  # Считаем закрашенным объект любого цвета, кроме белого
        super().__setattr__(key, value)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def square(self):
        return math.pow(self.__radius, 2) * math.pi

    def get_radius(self):
        return self.__radius

    def __len__(self):
        return self.get_sides()[0]

    def __setattr__(self, key, value):
        if key == '_Figure__sides':
            self.__radius = value[0] / (2 * math.pi)
        super().__setattr__(key, value)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        self.__height = [0, 0, 0]  # Список высот треугольника, проведенных к соответствующей стороне.
        super().__init__(color, *sides)

    def __setattr__(self, key, value):
        if key == '_Figure__sides':
            # Проверяем возможность существования такого треугольника и в случае провала вызываем исключение
            if value[0] >= value[1] + value[2] or value[1] >= value[0] + value[2] or value[2] >= value[0] + value[1]:
                raise ValueError(f'Треугольника со сторонами {value[0], value[1], value[2]} не может существовать')
            else:
                p = sum(value) / 2
                self.__height[0] = math.sqrt(p * (p - value[0]) * (p - value[1]) * (p - value[2])) * 2 / value[0]
                self.__height[1] = math.sqrt(p * (p - value[0]) * (p - value[1]) * (p - value[2])) * 2 / value[1]
                self.__height[2] = math.sqrt(p * (p - value[0]) * (p - value[1]) * (p - value[2])) * 2 / value[2]
        super().__setattr__(key, value)

    def __len__(self):
        return sum(self.get_sides())

    def get_height(self):
        return self.__height

    def square(self):
        return (self.get_height()[0] * self.get_sides()[0]) / 2


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = [sides[0]] * self.__class__.sides_count
        super().__init__(color, *sides)

    def __len__(self):
        return sum(self.get_sides())

    def square(self):
        return self.get_sides()[0] ** 2 * 6

    def get_volume(self):
        return self.get_sides()[0] ** 3

    def set_sides(self, *sides):
        if len(sides) == 1:
            sides = [sides[0]] * self.__class__.sides_count
        super().set_sides(*sides)


if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)
    triangle1 = Triangle((100, 100, 75), 10, 30, 30)
    cube1 = Cube((222, 35, 130), 6)

    print(triangle1)
    print(triangle1.get_sides())
    print(triangle1.get_height())
    triangle1.set_sides(30, 30, 10)
    print(triangle1)
    print(triangle1.get_height())
    print(len(triangle1))
    print(triangle1.square())
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    print(cube1.get_color())
    cube1.set_color(300, 70, 15)
    print(cube1.get_color())

    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    cube1.set_sides(10)
    print(cube1)

    print(len(circle1))
    print(circle1.square())
    print(circle1.get_radius())
    print(circle1.filled)
    print(circle1)
    circle1.set_color(255, 255, 255)
    print(circle1)
    print(cube1.get_volume())

    c = Circle((255, 255, 155), 10, 2)
    t = Triangle((255, 255, 255), 10, 10, 10)
    cube = Cube((255, 255, 255), 15)
    print(c, t, cube)
    print(c.sides_count)
    print(t.sides_count)
    print(cube.sides_count)
    print(f'Длина окружности {len(c)}')
    print(f'Радиус окружности r={c.get_radius()}')
    c.set_sides(5)
    print(len(c))
    print(c.get_radius())
    c.set_sides(10)
    print(len(c))
    print(c.get_radius())
    c.set_sides(6)
    print(len(c))
    print(c.get_radius())
