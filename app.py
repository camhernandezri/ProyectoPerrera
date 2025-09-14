from flask import Flask, redirect, url_for
from extensions import db
from controllers import dog_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "super_secret_key"

# Inicializar base de datos
db.init_app(app)

# Importar modelos después de inicializar db
import models

# Registrar blueprint
app.register_blueprint(dog_bp)

# Redirigir la raíz a la lista de perros
@app.route("/")
def home():
    return redirect(url_for("dogs.index"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
