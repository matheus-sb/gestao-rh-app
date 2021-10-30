from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired(), Length(min=-1, max=80, message='Campo não deve ter mais do que 80 caracteres.')])
    surname = StringField('Sobrenome', validators=[Length(min=-1, max=100, message='Campo não deve ter mais do que 100 caracteres.')])
    email = StringField('E-Mail', validators=[Email(), Length(min=-1, max=200, message='Campo não deve ter mais do que 200 caracteres.')])
    phone = StringField('Telefone', validators=[Length(min=-1, max=20, message='Campo não deve ter mais do que 20 caracteres.')])
