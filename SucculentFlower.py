from datetime import datetime, timedelta
from Flower import Flower


class SucculentFlower(Flower):

    def __init__(self, id, name, fertilize, last_watered, last_fertilized):

        super().__init__(
            id,
            name,
            "SUCCULENT",
            fertilize,
            last_watered,
            last_fertilized
        )

    def needs_watering(self):

        return (
            datetime.now() - self.last_watered
            > timedelta(days=14)
        )
    
    def needs_fertilize(self):

        return (
            datetime.now() - self.last_fertilized
             > timedelta(days=14)
        )