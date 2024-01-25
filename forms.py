from wtforms import Form
from wtforms import StringField, TelField 

class UserForm(Form):
    nombre = StringField('nombre')
    correo = StringField('email') # Crear campo de validación correcto
    primerApellido = TelField('primerAp')