from flask_wtf import FlaskForm
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, Email
from wtforms import SubmitField,IntegerField, StringField,DateField
from utils.pickLists import CityPicklist,tipoIdList,estadoList
from models import Cities

cityData = CityPicklist()

class ArrendadorForm(FlaskForm):

    nombres         = StringField('Nombres', validators=[DataRequired(), Length(max=100)])
    apellidos       = StringField('Apellidos', validators=[DataRequired(), Length(max=100)])
    email           = StringField('Email', validators=[DataRequired(), Email()])

    idnumber        = IntegerField('Número', validators=[DataRequired()])
    movil           = IntegerField('Móvil', validators=[DataRequired()])

    tipoid          = QuerySelectField('tipo Id', choices = tipoIdList,validators=[DataRequired()])
    estado          = QuerySelectField('Estado', choices = estadoList,validators=[DataRequired()])
    pais_exp        = QuerySelectField('Pais', choices = cityData.getpaises(),validators=[DataRequired()])
    provincia_exp   = QuerySelectField('Departamento', choices = cityData.getprovincias(),validators=[DataRequired()])
    ciudad_exp      = QuerySelectField('Ciudad', choices = cityData.getciudades(),validators=[DataRequired()])
    
    submit = SubmitField('Guardar')

    