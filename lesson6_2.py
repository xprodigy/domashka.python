print('Lesson 6_2:')


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight_calculate(self, weight=25, thickness=5):
        return round(self._length * self._width * weight * thickness / 1000, 2)


MyRoad = Road(1000, 20)
print('MyRoad потребует', MyRoad.weight_calculate(30, 9), 'тонн')
