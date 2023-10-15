from flask_wtf import FlaskForm
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, Email
from wtforms import SubmitField,IntegerField, StringField,DateField
from utils.pickLists import citiesList,provinciaList,paisList,tipoIdList,estadoList,tipoAlquilerList

class InmuebleForm(FlaskForm):

    name            = StringField('Nombres', validators=[DataRequired(), Length(max=10)])
    direccion       = StringField('Apellidos', validators=[DataRequired(), Length(max=200)])

    apartamento    = IntegerField('Apartamento', validators=[DataRequired()])
    habitaciones    = IntegerField('# Habitaciones', validators=[DataRequired()])
    banos           = IntegerField('# Baños')
    cod_agua        = IntegerField('Código agua')
    cod_luz         = IntegerField('Código luz')
    cod_gas         = IntegerField('Código gas')

    tipo            = QuerySelectField('Tipo alquiler', choices = tipoAlquilerList,validators=[DataRequired()])
    ciudad          = QuerySelectField('Ciudad', choices = citiesList,validators=[DataRequired()])
    
    submit = SubmitField('Guardar')

