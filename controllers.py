from flask import Blueprint, render_template, request, redirect, url_for
from extensions import db
from models import Dog

dog_bp = Blueprint("dogs", __name__)

# Listar perros
@dog_bp.route("/dogs")
def index():
    dogs = Dog.query.all()
    return render_template("index.html", dogs=dogs)

# Crear perro
@dog_bp.route("/dogs/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form["name"]
        breed = request.form["breed"]
        age = request.form["age"]

        new_dog = Dog(name=name, breed=breed, age=age)
        db.session.add(new_dog)
        db.session.commit()
        return redirect(url_for("dogs.index"))

    return render_template("create.html")

# Editar perro
@dog_bp.route("/dogs/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    dog = Dog.query.get_or_404(id)
    if request.method == "POST":
        dog.name = request.form["name"]
        dog.breed = request.form["breed"]
        dog.age = request.form["age"]
        db.session.commit()
        return redirect(url_for("dogs.index"))
    return render_template("edit.html", dog=dog)

# Eliminar perro
@dog_bp.route("/dogs/delete/<int:id>")
def delete(id):
    dog = Dog.query.get_or_404(id)
    db.session.delete(dog)
    db.session.commit()
    return redirect(url_for("dogs.index"))
