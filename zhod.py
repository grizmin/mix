class Car():

    valuta = 'leva'
    fuelType = {'petrol': 2.08,'diesel': 1.75}

    def __init__(self, literkm, fuel_type):
        self.fuel_type = fuel_type
        self.literkm = literkm

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

    def razhod(self, km):
        """
        :param km: (int) Kilometers
        :return: (float) price for the kilometers passed
        """
        cena = (self.literkm/100) * km * self.fuelPrice
        print(cena, Car.valuta)
        return cena

class marshrut():
    def __init__(self):
        self.cars = []

    def addCar(self, car):
        self.cars.append(car)

    def getCars(self):
        print([i for i in enumerate(self.cars)])

audi = Car(7.3, 'diesel')
citroen = Car(9.5, 'diesel')

p1 = Car(7, 'diesel')
p2 = Car(9, 'diesel')


p1.razhod(26)
p2.razhod(16)

m1 = marshrut()
m1.addCar(p1)
m1.getCars()
