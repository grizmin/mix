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
            print("{} struva {:.3}".format(car.whoami, cena), Car.valuta)
        return cena

    def vreme(self):
        for car in self.cars:
            vreme = (self.km / self.averagespeed)
            ftime = "{:.0f}h{:.0f}m".format(vreme, math.modf(vreme)[0] * 60)
            print("{} minava marshruta za {}".format(car.whoami, ftime))
        return vreme

def main():

    audi1 = Car(7.5, 'A6 Okolovrystno', 'diesel')
    audi2 = Car(11, 'A6 Center', 'diesel')

    # prez centera za 17km
    prez_center = marshrut(17, speed=35)
    prez_center.addCar(audi2)
    prez_center.razhod()
    prez_center.vreme()

    # ringroad za 28km
    ringroad = marshrut(27, speed=70)
    ringroad.addCar(audi1)
    ringroad.razhod()
    ringroad.vreme()

if __name__ == '__main__':
    main()