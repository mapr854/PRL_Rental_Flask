from flask_wtf import FlaskForm
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, Email
from wtforms import SubmitField,IntegerField, StringField,DateField
from utils.pickLists import citiesList,provinciaList,paisList,tipoIdList,estadoList

class ArrendatarioForm(FlaskForm):

    nombres         = StringField('Nombres', validators=[DataRequired(), Length(max=100)])
    apellidos       = StringField('Apellidos', validators=[DataRequired(), Length(max=100)])
    email           = StringField('Email', validators=[DataRequired(), Email()])
    nombreContacto  = StringField('Nombre contacto', validators=[Length(max=100)])
    profesion       = StringField('Profesión', validators=[Length(max=100)])

    idnumber        = IntegerField('Número', validators=[DataRequired()])
    movil           = IntegerField('Móvil', validators=[DataRequired()])
    movilContacto   = IntegerField('Móvil contacto', validators=[DataRequired()])
    fechaNacimiento = DateField('Fecha de Nacimiento', format='%Y-%m-%d', validators=[DataRequired()])

    tipoid          = QuerySelectField('tipo Id', choices = tipoIdList,validators=[DataRequired()])
    estado          = QuerySelectField('Estado', choices = estadoList,validators=[DataRequired()])
    pais_exp        = QuerySelectField('Pais', choices = paisList,validators=[DataRequired()])
    provincia_exp   = QuerySelectField('Departamento', choices = provinciaList,validators=[DataRequired()])
    ciudad_exp      = QuerySelectField('Ciudad', choices = citiesList,validators=[DataRequired()])
    
    submit = SubmitField('Guardar')

   