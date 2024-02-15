from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    nombre = StringField('nombre', [
        validators.DataRequired(message = 'Campo requerido'),
        validators.length(min=4, max=10, message='Ingresa un nombre valido')
    ])
    primerApellido = StringField('primer apellido')
    segundoApellido = StringField('segundo apellido')
    correo = EmailField('email', [ validators.Email(message='Ingresa un correo valido')])
    edad = IntegerField('edad')