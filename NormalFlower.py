from datetime import datetime, timedelta
from Flower import Flower


class NormalFlower(Flower):

    def __init__(self, id, name, fertilize, last_watered, last_fertilized):

        super().__init__(
            id,
            name,
            "NORMAL",
            fertilize,
            last_watered,
            last_fertilized
        )

    def needs_watering(self):

        return (
            datetime.now() - self.last_watered > timedelta(days=7)
        )
    def needs_fertilize(self):

        return (
            datetime.now() - self.last_fertilized
            > timedelta(days=14)
        )