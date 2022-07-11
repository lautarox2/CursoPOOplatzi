from ubervan import UberVan
from uberx import Uberx
from account import Account
from car import Car
from driver import Driver
from user import User


def run():
    print("hola mundo")

    user = User("Duham", "41599127", "duham.brc@gmail.com")
    print("Usuario: ")
    print(vars(user))

    driver = Driver("Agus", "48562324", "agus.brc@gmail.com")
    print("Usuario: ")
    print(vars(driver))

    uberx = Uberx("AMS789", Account("Lauti Fleitas", "40324995", "lautaro.brc@gmail.com"), 5, "Fiat", "uno")
    print("Auto X: ")           
    print(vars(uberx))
    print(vars(uberx.driver))
    print(vars(uberx.passenger))

#    ubervan = UberVan("JSH554", Account("Emi Lerin", "16973253", "emilse.brc@gmail.com"), "4", "Fiat", "Cuero")
 #   print("Auto Van: ")
  #  print(vars(ubervan))
   # print(vars(ubervan.driver))
    
if __name__ == "__main__":
    run()
