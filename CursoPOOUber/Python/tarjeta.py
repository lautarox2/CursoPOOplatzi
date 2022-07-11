from calendar import c
from datetime import date

from zmq import CURVE_SERVER
from payments import Payments

class Tarjeta(Payments):
    banco = str
    fecha = date
    cvv = str

    def __init__(self, id, banco, fecha, cvv):
        self.banco = banco
        self.fecha = fecha
        self.cvv = cvv
