print('Lesson 6_4:')


class Car:

    def __init__(self, color, name, is_police=False):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(self.name, 'started moving')

    def stop(self):
        print(self.name, 'stopped moving')

    def turn(self, direction):
        self.direction = direction
        print(self.name, 'turned', self.direction)

    def show_speed(self, speed):
        self.speed = int(speed)
        print(self.name, ' speed is ', self.speed, 'km/h', sep='')


class TownCar(Car):
    def show_speed(self, speed):
        self.speed = int(speed)
        if self.speed > 60:
            print(self.name, ' is overspeed: ', self.speed, 'km/h', sep='')
        else:
            print(self.name, ' speed is ', self.speed, 'km/h', sep='')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self, speed):
        self.speed = int(speed)
        if self.speed > 40:
            print(self.name, ' is overspeed: ', self.speed, 'km/h', sep='')
        else:
            print(self.name, ' speed is ', self.speed, 'km/h', sep='')


class PoliceCar(Car):
    pass


cybertruck = TownCar('gray', 'Cybertruck')

print('New TownCar - ', cybertruck.color, ' ', cybertruck.name, '! Is it police? - ', cybertruck.is_police, sep='')
cybertruck.go()
cybertruck.show_speed(60)
cybertruck.turn('left')
cybertruck.show_speed(80)
cybertruck.stop()

tesla = SportCar('red', 'Tesla')
print('-' * 40, '\nNew SportCar - ', tesla.color, ' ', tesla.name, '! Is it police? - ', tesla.is_police, sep='')
tesla.go()
tesla.show_speed(60)
tesla.turn('left')
tesla.show_speed(120)
tesla.stop()

teslasemi = WorkCar('white', 'Tesla Semi')
print('-' * 40, '\nNew TownCar - ', teslasemi.color, ' ', teslasemi.name, '! Is it police? - '
                                                                          '', teslasemi.is_police, sep='')
teslasemi.go()
teslasemi.show_speed(30)
teslasemi.turn('right')
teslasemi.show_speed(50)
teslasemi.stop()

crownvic = PoliceCar('black/white', 'Crown Vic', True)

print('-' * 40, '\nNew PoliceCar - ', crownvic.color, ' ', crownvic.name, ' is created! Is it police? - ',
      crownvic.is_police, sep='')
crownvic.go()
crownvic.show_speed(30)
crownvic.turn('right')
crownvic.show_speed(250)
crownvic.stop()

