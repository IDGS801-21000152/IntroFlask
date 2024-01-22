from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "¡¡Hola Mundo!!"

@app.route("/hola")
def hola():
    return "<h1>Saludos desde Hola</h1>"

@app.route("/Saludo")
def saludo():
    return "<h1>Saludos desde Saludo</h1>"
    
if __name__ ==  "__main__":
    app.run()