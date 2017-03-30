import math

class Car():
    valuta = 'leva'
    fuelType = {'petrol': 2.08,'diesel': 1.75, 'gas': 1.06}

    def __init__(self, name=None, razhod=None, **kwargs):
        self.fuel_type = kwargs.get('fuel_type', 'diesel')
        self.literkm = razhod
        self.name = name

    @property
    def fuel_type(self):
        return self._fuel_type

    @fuel_type.setter
    def fuel_type(self, val):
        assert val in Car.fuelType.keys(),\
            'illegal fuel type. Possible types: {}'.format(', '.join(Car.fuelType.keys()))
        self._fuel_type = val

    @property
    def fuelPrice(self):
        return Car.fuelType[self.fuel_type]

    @property
    def whoami(self):
        """
        Name of the car object
        :return: (dict) keys: name, razhod, fuelType
        """
        return {'name': self.name, 'razhod': self.literkm, 'fuelType': self.fuel_type}

class Marshrut():
    def __init__(self, km, **kwargs):
        """
        :param km: (int) kilometers length
        :param kwargs: (int) speed, list[(object)] cars
        """
        self._cars = {}
        if kwargs.get('cars'):
            self.cars = kwargs.get('cars')
        self.averagespeed = kwargs.get('speed', 50)
        self.km = km

    @property
    def cars(self):
        return self._cars

    @cars.setter
    def cars(self, car):
        if type(car) is list:
            if isinstance(car[0], Car) and len(car):
                self._cars = {k:(k.literkm/100) * self.km * k.fuelPrice for k in car}
        elif isinstance(car, Car):
            self._cars[car] = (car.literkm/100) * self.km * car.fuelPrice
        else:
            print(car, ': Unknown format. cars can be only instance of Car object or list of Car objects')

    def getCars(self):
        """
        :return: Cars assigned to this marshrut
        """
        print('\n'.join('{}: {}'.format(k, v.whoami['name']) for k, v in enumerate(self.cars)))

    def stat(self):
        print('*' * 10, type(self).__name__, self.km, '*' * 10)
        for car in self.cars:
            t = (self.km / self.averagespeed)
            ftime = "{:.0f}h{:.0f}m".format(t, math.modf(t)[0] * 60)
            print("{} minava {}km marshrut za {} i struva {:.2f} leva"\
                  .format(car.whoami['name'], self.km, ftime, self.cars[car]))

def main():

    audi1 = Car('A6 izvyn-gradsko', razhod=7.2, fuel_type='diesel')
    audi2 = Car('A6 gradsko', 12, fuel_type='diesel')
    subaru12 = Car('Subaru Gas Mitaka gradsko', 12, fuel_type='gas')
    subaru9 = Car('Subaru Gas Mitaka izvyn-gradsko', 9, fuel_type='gas')

    print('Fuel prices in leva: {}'.format(Car.fuelType))

    # prez centera za 16km
    prez_center = Marshrut(16, speed=32)
    prez_center.cars = [audi2, subaru12]
    prez_center.getCars()
    prez_center.stat()

    print('')

    # ringroad za 36km
    ringroad = Marshrut(36, speed=77)
    ringroad.cars = audi1
    ringroad.cars = subaru9
    ringroad.getCars()
    ringroad.stat()

if __name__ == '__main__':
    main()