

class Vector:
    def __init__(self, x, y, target=0):
        self.x = x
        self.y = y
        self.target = target
    def print_vec(self):
        print(f'{self.x} - {self.y} \n')


def get_y(vector):
    sum = vector.x + vector.y
    if sum >= 0:
        return 1
    else:
        return -1


weights = Vector(0, 0)
bias = 0
# define data points
data_points = [Vector(-1, 1, 1), Vector(0, -1, -1), Vector(10, 1, 1)]

found_optima = False

while found_optima is False:
    found_optima = True
    for point in data_points:
        classification = ((weights.x*point.x) + (weights.y*point.y) + bias)
        if classification < 0:
            classification = -1
        if classification > 0:
            classification = 1
        if classification is not point.target or classification is 0:
            weights.x += point.x*point.target
            weights.y += point.y*point.target
            bias += point.target
            found_optima = False
        weights.print_vec()
print(f'\n Bias: {bias}')

