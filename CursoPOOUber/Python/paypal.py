from payments import Payments

class Paypay(Payments):
    refertencia = str
    sucursal = str

    def __init__(self, id, referencia, sucursal):
        self.refertencia = referencia
        self.sucursal = sucursal
