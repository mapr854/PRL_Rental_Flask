from flask_wtf import FlaskForm
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, Email
from wtforms import SubmitField,IntegerField, StringField,DateField
from utils.pickLists import tipoAlquilerList, estadoList

class ArrendatarioForm(FlaskForm):

    poliza         = StringField('Poliza', validators=[DataRequired(), Length(max=50)])
    

    precio          = IntegerField('Precio', validators=[DataRequired()])
    administracion  = IntegerField('Administración', validators=[DataRequired()])
    months          = IntegerField('Meses', validators=[DataRequired()])
    bono            = IntegerField('Bono', validators=[DataRequired()])

    inicio          = DateField('Fecha de Inicio', format='%Y-%m-%d', validators=[DataRequired()])
    fin             = DateField('Fecha de Fin', format='%Y-%m-%d')

    contratType     = QuerySelectField('Tipo Alquiler', choices = tipoAlquilerList,validators=[DataRequired()])
    estado          = QuerySelectField('Estado', choices = estadoList,validators=[DataRequired()])

    submit = SubmitField('Guardar')

   

