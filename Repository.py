from Database import get_connection #import funkce pro připojení k databázi
from datetime import datetime

from TropicalFlower import TropicalFlower
from NormalFlower import NormalFlower
from SucculentFlower import SucculentFlower


class FlowerRepository:  #nová třída 

    def add_flower(self, flower): #metoda pro přidání rostliiny do databáze (self-repository objekt, flower - objekt flower)

        conn = get_connection()  #otevření spojení s sqlite databazi

        cursor = conn.execute("""     #spustí sql příkaz - vlož do flowers...
            INSERT INTO flowers (
                name,
                type,
                last_watered,
                fertilize,
                last_fertilized
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            flower.name,   #bere data z objektu
            flower.type,
            flower.last_watered.isoformat(),  #převod datetime na text 
            flower.fertilize,
            flower.last_fertilized.isoformat()
        ))

        conn.commit()  #uložení změn do databáze

        flower.id = cursor.lastrowid   #vytvoření automatického id

        conn.close()   #uzavření spojení

        return flower


    def get_all_flowers(self):

        conn = get_connection()

        rows = conn.execute("""
            SELECT * FROM flowers
        """).fetchall()

        conn.close()

        flowers = []

        for row in rows:

            if row["type"] == "TROPICAL":

                flower = TropicalFlower(
                    id=row["id"],
                    name=row["name"],
                    fertilize=bool(row["fertilize"]),
                    last_watered=datetime.fromisoformat(
                        row["last_watered"]
                    ),
                    last_fertilized=(
                        datetime.fromisoformat(
                            row["last_fertilized"]
                        )
                        if row["last_fertilized"]
                        else None
                    )
                )

            elif row["type"] == "NORMAL":

                flower = NormalFlower(
                    id=row["id"],
                    name=row["name"],
                    fertilize=bool(row["fertilize"]),
                    last_watered=datetime.fromisoformat(
                        row["last_watered"]
                    ),
                    last_fertilized=(
                        datetime.fromisoformat(
                            row["last_fertilized"]
                        )
                        if row["last_fertilized"]
                        else None
                    )
                )

            elif row["type"] == "SUCCULENT":

                flower = SucculentFlower(
                    id=row["id"],
                    name=row["name"],
                    fertilize=bool(row["fertilize"]),
                    last_watered=datetime.fromisoformat(
                        row["last_watered"]
                    ),
                    last_fertilized=(
                        datetime.fromisoformat(
                            row["last_fertilized"]
                        )
                        if row["last_fertilized"]
                        else None
                    )
                )

            else:
                continue

            flowers.append(flower)

        # priority sorting

        flowers.sort(

            key=lambda flower: (

                # 1. water + fertilizer
                not (
                    flower.needs_watering()
                    and (
                        flower.fertilize
                        and flower.needs_fertilize()
                    )
                ),

                # 2. only water
                not flower.needs_watering(),

                # 3. only fertilizer
                not (
                    flower.fertilize
                    and flower.needs_fertilize()
                )

            )
        )

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
        """, (
            now,
            flower_id
        ))

        conn.commit()

        conn.close()


    def fertilize_flower(self, flower_id):

        conn = get_connection()

        now = datetime.now().isoformat()

        conn.execute("""
            UPDATE flowers
            SET last_fertilized = ?
            WHERE id = ?
        """, (
            now,
            flower_id
        ))

        conn.commit()

        conn.close()