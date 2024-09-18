class Rhombus:
    side_a: int
    angle_a: int
    angel_b: int

    def __init__(self, side_a: int, angle_a: int):
        self.side_a = side_a
        self.angle_a = angle_a
        self.angel_b = self.check_value_angel_b(angle_a)

    def print_side_a(self):
        print(self.side_a)

    def print_angle_a(self):
        print(self.angle_a)

    def print_angle_b(self):
        print(self.angel_b)

    def check_zero_value(self, value):
        if value <= 0:
            raise ValueError("Значення сторони side_a повинно бути більше 0")

    def check_value_angel_b(self, value):
        return int((360 - 2 * value) / 2)

    def __setattr__(self, key, value):
        if key == "side_a":
            self.check_zero_value(value)
        super().__setattr__(key, value)
