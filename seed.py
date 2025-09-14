from app import app
from extensions import db
from models import Dog

# Datos de ejemplo
dogs_data = [
    {"name": "Firulais", "breed": "Labrador", "age": 3},
    {"name": "Max", "breed": "Pastor Alemán", "age": 5},
    {"name": "Luna", "breed": "Golden Retriever", "age": 2},
    {"name": "Rocky", "breed": "Bulldog", "age": 4},
    {"name": "Canela", "breed": "Beagle", "age": 1}
]

with app.app_context():
    # Borrar datos anteriores
    db.drop_all()
    db.create_all()

    # Insertar perros de prueba
    for dog in dogs_data:
        new_dog = Dog(name=dog["name"], breed=dog["breed"], age=dog["age"])
        db.session.add(new_dog)

    db.session.commit()
    print("✅ Base de datos poblada con perros de prueba")
