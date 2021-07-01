from time import sleep


class TrafficLight:
    __color = '3x colors'
    def running(self):
        while True:
            print('\r' * 50, 'RED.yellow.green', end='')
            sleep(7)
            print('\r' * 50, 'red.YELLOW.green', end='')
            sleep(2)
            print('\r' * 50, 'red.yellow.GREEN', end='')
            sleep(1)
            print('\r' * 50, 'red.yellow.*****', end='')
            sleep(1)
            print('\r' * 50, 'red.yellow.GREEN', end='')
            sleep(1)
            print('\r' * 50, 'red.yellow.*****', end='')
            sleep(1)

TrafficLight_obj = TrafficLight()
TrafficLight_obj.running()
