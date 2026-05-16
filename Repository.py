from Database import get_connection
from datetime import datetime

from TropicalFlower import TropicalFlower
from NormalFlower import NormalFlower
from SucculentFlower import SucculentFlower


class FlowerRepository:

    def add_flower(self, flower):

        conn = get_connection()

        cursor = conn.execute("""
            INSERT INTO flowers (name, type, last_watered, fertilize, last_fertilized)
            VALUES (?, ?, ?, ?, ?)
        """, (
            flower.name,
            flower.type,
            flower.last_watered.isoformat(),
            flower.fertilize,
            flower.last_watered.isoformat()
        ))

        conn.commit()

        flower.id = cursor.lastrowid

        conn.close()

        return flower


    def get_all_flowers(self):

        conn = get_connection()

        rows = conn.execute("""
            SELECT * FROM flowers
            ORDER BY last_watered ASC
        """).fetchall()

        conn.close()
        flowers = []

        for row in rows:
            print(row["fertilize"], type(row["fertilize"]))
            if row["type"] == "TROPICAL":

                flower = TropicalFlower(
                    id=row["id"],
                    name=row["name"],
                    last_watered=datetime.fromisoformat(
                        row["last_watered"]
                    ),
                    last_fertilized=(
    datetime.fromisoformat(row["last_fertilized"])
    if row["last_fertilized"]
    else None
),
                    fertilize=bool(row["fertilize"])
                )

            elif row["type"] == "NORMAL":

                flower = NormalFlower(
                    id=row["id"],
                    name=row["name"],
                    last_watered=datetime.fromisoformat(
                        row["last_watered"]
                    ),
                     last_fertilized=(
    datetime.fromisoformat(row["last_fertilized"])
    if row["last_fertilized"]
    else None
),
                   fertilize=bool(row["fertilize"])
                )

            elif row["type"] == "SUCCULENT":

                flower = SucculentFlower(
                    id=row["id"],
                    name=row["name"],
                    last_watered=datetime.fromisoformat(
                        row["last_watered"]
                    ),
                    last_fertilized=(
    datetime.fromisoformat(row["last_fertilized"])
    if row["last_fertilized"]
    else None
),
                    fertilize=bool(row["fertilize"])
                )

            else:
                continue

            flowers.append(flower)

        return flowers


    def delete_flower(self, flower_id):

        conn = get_connection()

        conn.execute(
            "DELETE FROM flowers WHERE id = ?",
            (flower_id,)
        )

        conn.commit()
        conn.close()


    def water_flower(self, flower_id):

        conn = get_connection()

        now = datetime.now().isoformat()

        conn.execute("""
            UPDATE flowers
            SET last_watered = ?
            WHERE id = ?
        """, (now, flower_id))

        conn.commit()
        conn.close()

    def fertilize_flower(self, flower_id):

        conn = get_connection()

        now = datetime.now().isoformat()

        conn.execute("""
            UPDATE flowers
            SET last_fertilized = ?
            WHERE id = ?
        """, (now, flower_id))

        conn.commit()
        conn.close()