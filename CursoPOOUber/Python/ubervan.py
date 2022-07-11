from car import Car

class UberVan(Car):
    typeCarAccepted = ["Fiat"]
    seatsMaterial = ["Cuero"]

    def __init__(self, license, driver, typeCarAccepted, seatsMaterial):
        super().__init__(license,driver)
        self.typeCarAccepted = typeCarAccepted
        self.seatsMaterial = seatsMaterial
