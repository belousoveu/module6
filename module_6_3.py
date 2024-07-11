class Horse:
    def __init__(self, x_distance=0, sound='Frrr'):
        self.x_distance = x_distance
        self.sound = sound
        super().__init__()

    def __str__(self):
        return f"Horse: x_distance={self.x_distance}, sound={self.sound}"

    def __repr__(self):
        return f"Horse(x_distance={self.x_distance}, sound={self.sound})"

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self, y_distance=0, sound='I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def __str__(self): return f"Eagle: y_distance={self.y_distance}, sound={self.sound}"

    def __repr__(self):
        return f"Eagle(y_distance={self.y_distance}, sound={self.sound})"

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    # def __init__(self):
    #     super().__init__()

    def __str__(self):
        return f"Pegasus: x_distance={self.x_distance}, y_distance={self.y_distance}, sound={self.sound}"

    def __repr__(self):
        return f"Pegasus(x_distance={self.x_distance}, y_distance={self.y_distance}, sound={self.sound})"

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def voice(self):
        print(self.sound)


if __name__ == '__main__':
    p1 = Pegasus()

    print(p1.get_pos())
    p1.move(10, 15)
    print(p1.get_pos())
    p1.move(-5, 20)
    print(p1.get_pos())

    p1.voice()
