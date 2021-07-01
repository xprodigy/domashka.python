print('Lesson 6_5:')


class Stationery:
    title = 'Name of all stationerys'

    def draw(self):
        print('Start drawing... Oops! Take a some stationery first!')


class Pen(Stationery):
    def draw(self):
        print('------ Line maked by pen')


class Pencil(Stationery):
    def draw(self):
        print('------ Line maked by pencil')


class Handle(Stationery):
    def draw(self):
        print('------ Line maked by handle')


test = Stationery()
test.draw()

blue_pen = Pen()
blue_pen.draw()

gray_pencil = Pencil()
gray_pencil.draw()

green_handle = Handle()
green_handle.draw()
