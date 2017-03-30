import math

class Car():
    valuta = 'leva'
    fuelType = {'petrol': 2.08,'diesel': 1.75}

    def __init__(self, literkm, name, fuel_type):
        self.fuel_type = fuel_type
        self.literkm = literkm
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
        :return: (string) name
        """
        return self.name

class marshrut():
    def __init__(self, km, **kwargs):
        self.cars = kwargs.get('cars', [])
        self.averagespeed = kwargs.get('speed', 50)
        self.km = km

    def addCar(self, car):
        self.cars.append(car)

    def getCars(self):
        """
        :return: Cars asigned to this marshrut
        """
        print('\n'.join('{}: {}'.format(k, v.whoami) for k, v in enumerate(self.cars)))

    def razhod(self):
        """
        :param km: (int) Kilometers
        :return: (float) price for the kilometers passed
        """
        for car in self.cars:
            cena = (car.literkm/100) * self.km * car.fuelPrice
        return cena

    def stat(self):
        for car in self.cars:
            t = (self.km / self.averagespeed)
            ftime = "{:.0f}h{:.0f}m".format(t, math.modf(t)[0] * 60)
            print("{} minava {}km marshrut za {} i struva {:.2f} leva"\
                  .format(car.whoami, self.km, ftime, self.razhod()))
        return t

def main():

    audi1 = Car(7.2, 'A6 Okolovrystno', 'diesel')
    audi2 = Car(12, 'A6 Center', 'diesel')

    # prez centera za 16km
    prez_center = marshrut(16, speed=32)
    prez_center.addCar(audi2)
    prez_center.stat()

    # ringroad za 36km
    ringroad = marshrut(36, speed=77)
    ringroad.addCar(audi1)
    ringroad.stat()

if __name__ == '__main__':
    main()