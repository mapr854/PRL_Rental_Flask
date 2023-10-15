from flask import Blueprint, render_template, request,url_for,redirect
import pandas as pd
from markupsafe import escape
from models import Cities,Inmueble
from utils.db_sqlite import db
from utils.searchQuery import search_Inmueble
from utils.pickLists import *
from utils.shareFun import *


inmueble_bp = Blueprint('inmueble', __name__)

@inmueble_bp.route('/')
def index():
    results= Inmueble.query.filter(Inmueble.estado != 'I').all()
        
    return render_template('inmueble/inmuebleTable.html',  results =results)

@inmueble_bp.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form.get('search_term')
        results = search_Inmueble(search_term)
        
        return render_template('inmueble/inmuebleTable.html', results = results)

    return redirect(url_for('inmueble.index'))

@inmueble_bp.route('/form', methods=['GET'])
def create():
    return displayForm()


@inmueble_bp.route('/edit/<int:item_id>', methods =['GET','POST'])
def edit_inmueble(item_id):
   try:
        inmueble = Inmueble.query.filter_by(id=int(item_id)).one()
        return displayForm(inmueble,item_id)
   
   except :
        return render_template('not_found.html')
   
@inmueble_bp.route('/update/<edit_id>', methods =['GET','POST'])
def update_inmueble(edit_id):
    typeScape=escape(edit_id)
    if typeScape == 'new':
       addInmueble = Inmueble()
    elif typeScape.isdigit():
        addInmueble = Inmueble.query.filter_by(id=int(typeScape)).one()
    else:
        return redirect(url_for('inmueble.index'))
    
    addInmueble.tipo   =request.form['tipo']
    addInmueble.name    =request.form['name'].strip()
    addInmueble.estado    =request.form['estado']
    addInmueble.direccion    =request.form['direccion'].strip()
    addInmueble.ciudad    =request.form['ciudad']
    addInmueble.apartamento    =request.form['apartamento']
    addInmueble.habitaciones    =request.form['habitaciones']
    addInmueble.bano    =request.form['bano']
    addInmueble.cod_gas    =request.form['cod_gas']
    addInmueble.cod_luz    =request.form['cod_luz']
    addInmueble.cod_agua    =request.form['cod_agua']
    
    
    db.session.add(addInmueble)
    db.session.commit()

    return redirect(url_for('inmueble.index'))
    

@inmueble_bp.route('/delete/<int:item_id>', methods =['GET','POST'])
def delete_inmueble(item_id):
    
    try:
        item = Inmueble.query.filter_by(id=item_id).one()
        if item:
            db.session.delete(item)
            db.session.commit()
        return redirect(url_for('inmueble.index'))
    except :
        return render_template('not_found.html')

def displayForm(inmueble = None, edit_id = 'new'):
    if inmueble is None:
        inmueble = Inmueble()
    rentalType = tipoAlquilerList
    estados = estadoInmuebleList
    citiesQuery = Cities.query.all()
    cityData = CityPicklist(cityQuery=citiesQuery)
    ciudades = cityData.getciudades()
    
    return render_template('inmueble/formInmueble.html',
                           edit_id = edit_id,
                           inmueble = inmueble,
                           rentalType = rentalType,
                           estados = estados,
                           ciudades = ciudades,
                           )





        
    

        
    
   
