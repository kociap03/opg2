from datetime import datetime
from abc import ABC, abstractmethod

class Flower(ABC): # abystraktní rodičovská třída 
    def __init__(self, id, name, type, fertilize, last_watered, last_fertilized): #konstruktor, když se vytvoří objekt (např Normal Flower), automatický se zavolá __init__
        self.id = id  #uloží id, jméno.. do objektu, objekt si pak pamatuje své id atd
        self.name = name
        self.type = type
        self.last_watered = last_watered or datetime.now() #použije datetime posledního zalití nebo současné datetime
        self.last_fertilized = last_fertilized or datetime.now()
        self.fertilize = fertilize #uloží info zda rostlina potřebuje fertilizer (boolean yes/no)

    @abstractmethod    #abstr. metoda, definuje, že každá flower musí mít needs_fertilize a needs_watering
    def needs_fertilize(self): #každá třída dědící od této rodičovské musí implementovat abstraktní metody, jinak mě to nepustí dál - chyba
        pass

    @abstractmethod
    def needs_watering(self):
        pass