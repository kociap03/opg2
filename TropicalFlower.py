from datetime import datetime, timedelta
from Flower import Flower


class TropicalFlower(Flower):

    def __init__(self, id, name, fertilize, last_watered, last_fertilized):

        super().__init__(
            id,
            name,
            "TROPICAL",
            fertilize,
            last_watered,
            last_fertilized
        )

    def needs_watering(self):

        return (
            datetime.now() - self.last_watered
            > timedelta(days=2)
        )
    
    def needs_fertilize(self):

        return (
            datetime.now() - self.last_fertilized
            > timedelta(days=14)
        )