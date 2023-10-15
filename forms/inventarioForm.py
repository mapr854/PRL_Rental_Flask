from flask_wtf import FlaskForm
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, Email
from wtforms import SubmitField,IntegerField, StringField,DateField
from utils.pickLists import citiesList,provinciaList,paisList,tipoIdList,estadoList

class ArrendadorForm(FlaskForm):

    descripcion   = StringField('Descripción', validators=[DataRequired(), Length(max=200)])
    
    Precio        = IntegerField('Número', validators=[DataRequired()])

    estado          = QuerySelectField('Estado', choices = estadoList,validators=[DataRequired()])
   
    
    submit = SubmitField('Guardar')

    