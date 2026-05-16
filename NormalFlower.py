from datetime import datetime, timedelta
from Flower import Flower


class NormalFlower(Flower): #dědí z flower, díky tomu automaticky získá id, name.. atd

    def __init__(self, id, name, fertilize, last_watered, last_fertilized):  

        super().__init__(   #zavolá konstruktor rodičovské třídy, nemusím vypisovat např self.name=name, type="NORMAL" atd
            id,
            name,
            "NORMAL",
            fertilize,
            last_watered,
            last_fertilized
        )

    def needs_watering(self):

        return (
            datetime.now() - self.last_watered > timedelta(days=7) #vytvoří interval od posledního zalití a porovná s intervalem(timedelta) jestli je to víc nebo ne
        )
    def needs_fertilize(self):

        return (
            datetime.now() - self.last_fertilized #vytvoří interval, který se porovná s intervalem a vrací boolean (operátor porovnání vždy vrací bolean)
            > timedelta(days=14)
        )