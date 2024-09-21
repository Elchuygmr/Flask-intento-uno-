from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Servidor Flask funcionando correctamente!"

# Nueva ruta para recibir datos GPS
@app.route('/gps', methods=['POST'])
def receive_gps_data():
    gps_data = request.json  # Obtener datos JSON del cuerpo de la solicitud
    print(f"Datos recibidos del GPS: {gps_data}")
    return jsonify({"status": "Datos recibidos"}), 200

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mi_base_de_datos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db = SQLAlchemy(app)

# Crear un modelo de ejemplo
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)

# Crear la base de datos y las tablas
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

