from wtforms import Form
from wtforms import StringField, TelField, IntegerField
from wtforms import EmailField
# Aquí de los validadores importamos el dato obligatorio y el email
from wtforms.validators import DataRequired, Email

class UserForm(Form):
    nombre = StringField('nombre')
    primerApellido = StringField('primer apellido')
    segundoApellido = StringField('segundo apellido')
    correo = EmailField('email')
    edad = IntegerField('edad')