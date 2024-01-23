from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alumnos")
def alumnos():
    titulo = "UTL"
    nombres = ["Shava", "Alexa", "Mariela"]
    return render_template(
        "alumnos.html", 
        titulo = titulo, nombres = nombres
    )

@app.route("/maestros")
def maestros():
    return render_template("maestros.html")

@app.route("/hola")
def hola():
    return "<h1>Saludos desde Hola :D</h1>"

@app.route("/Saludo")
def saludo():
    return "<h1>Saludos desde Saludo</h1>"
    
@app.route("/nombre/<string:nombre>")
def nombre(nombre):
    return "Hola " + nombre + ":D"

@app.route("/numero/<int:n1>")
def numero(n1):
    return "Número: {}".format(n1)

@app.route("/user/<int:id>/<string:nombre>")
def user(id, nombre):
    return "ID: {} Nombre: {}".format(id, nombre)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "La suma de {} + {} = {}".format(n1, n2, n1 + n2)

@app.route("/default")
@app.route("/default/<string:d>")
def func2(d="Dario"):
    return "El nombre de User es: " + d

if __name__ ==  "__main__":
    app.run(debug=True)