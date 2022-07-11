from account import Account

class Car:
    id = int
    license = str
    driver = Account("","","")
    passenger = int


    def __init__(self, license, driver, passenger):
        self.license = license
        self.driver = driver


    def setpassenger (self, passengerNum):
        if passengerNum >=4:
            self.__passenger = int(passengerNum)
            print("Pasajeros asignados = ") + str(self.__passenger)
        else:
            print("El número no es correcto")


    def passenger(self):
        if self.__passenger != int:
            print(self.__passenger)
