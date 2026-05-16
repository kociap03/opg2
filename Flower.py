from datetime import datetime
from abc import ABC, abstractmethod

class Flower(ABC):
    def __init__(self, id, name, type, fertilize, last_watered, last_fertilized):
        self.id = id
        self.name = name
        self.type = type
        self.last_watered = last_watered or datetime.now()
        self.last_fertilized = last_fertilized or datetime.now()
        self.fertilize = fertilize

    @abstractmethod
    def needs_fertilize(self): 
        pass

    @abstractmethod
    def needs_watering(self):
        pass