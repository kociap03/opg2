from flask import Flask, request, jsonify, render_template

from Repository import FlowerRepository
from Database import create_table
from datetime import datetime

from TropicalFlower import TropicalFlower
from NormalFlower import NormalFlower
from SucculentFlower import SucculentFlower

app = Flask(__name__)

create_table()

repository = FlowerRepository()


@app.route("/")
def home():

    flowers = repository.get_all_flowers()

    return render_template(
        "index.html",
        flowers=flowers
    )


@app.route("/flowers", methods=["GET"])
def get_flowers():

    flowers = repository.get_all_flowers()

    return jsonify([
        flower.to_dict()
        for flower in flowers
    ])


@app.route("/add-form", methods=["POST"])
def add_flower_form():

    name = request.form["name"]
    flower_type = request.form["type"]
    fertilize = request.form["fertilize"]

    if flower_type == "tropical":

        flower = TropicalFlower(
            id=None,
            name=name,
            fertilize=fertilize == "fertilize_yes",
            last_watered=datetime.now(),
            last_fertilized=datetime.now()
        )

    elif flower_type == "normal":

        flower = NormalFlower(
            id=None,
            name=name,
            fertilize=fertilize == "fertilize_yes",
            last_watered=datetime.now(),
            last_fertilized=datetime.now()
        )

    elif flower_type == "succulent":

        flower = SucculentFlower(
            id=None,
            name=name,
            fertilize=fertilize == "fertilize_yes",
            last_watered=datetime.now(),
            last_fertilized=datetime.now()
        )

    else:
        return "Invalid flower type", 400

    repository.add_flower(flower)

    return home()


@app.route("/delete/<int:flower_id>", methods=["POST"])
def delete_flower_form(flower_id):

    repository.delete_flower(flower_id)

    return home()


@app.route("/water/<int:flower_id>", methods=["POST"])
def water_flower_form(flower_id):

    repository.water_flower(flower_id)

    return home()

@app.route("/fertilize/<int:flower_id>", methods=["POST"])
def fertilize_flower_form(flower_id):

    repository.fertilize_flower(flower_id)

    return home()

if __name__ == "__main__":

    app.run(
        port=8080,
        debug=True
    )