from flask import Flask, render_template, request
import forms

app = Flask(__name__)

## Ruta de index
@app.route("/")
def index():
    return render_template("index.html")

## Ruta para alumnos
@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    alumno_class = forms.UserForm(request.form)
    if request.method == "POST":
        pass
    
    return render_template("alumnos.html", form=alumno_class)

## Ruta para profesores
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

@app.route("/calcular", methods=["GET", "POST"])
def calcular():
    if request.method == "POST":
        n1 = request.form.get("n1")
        n2 = request.form.get("n2")
        return "La multiplicación de {} x {} = {}".format(n1, n2, str(int(n1) * int(n2)))
    else:
        return '''
            <form action="/calcular" method="POST">
                <label>Número 1:</label>
                <input type="text" name="n1"><br>
                <label>Número 2:</label>
                <input type="text" name="n2"><br>
                <input type="submit"/>
            </form>
        '''

@app.route("/operasbas")
def operaciones():
    return render_template("operasBas.html")

@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    if request.method == "POST":
        n1 = request.form.get("n1")
        n2 = request.form.get("n2")
        return "La multiplicación de {} x {} = {}".format(n1, n2, str(int(n1) * int(n2)))

if __name__ ==  "__main__":
    app.run(debug=True)