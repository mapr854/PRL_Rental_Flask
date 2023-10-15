from flask import Blueprint, render_template, request,url_for,redirect
import pandas as pd
from markupsafe import escape
from models import Cities,Arrendador
from utils.db_sqlite import db
from utils.searchQuery import search_Arrendador
from utils.pickLists import *


arrendador_bp = Blueprint('arrendador', __name__)

@arrendador_bp.route('/')
def index():
    results= Arrendador.query.filter(Arrendador.estado == 'A').all()
        
    return render_template('arrendador/arrendadorTable.html',  results =results)

@arrendador_bp.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form.get('search_term')
        results = search_Arrendador(search_term)
        
        return render_template('arrendador/arrendadorTable.html', results = results)

    return redirect(url_for('arrendador.index'))

@arrendador_bp.route('/form', methods=['GET'])
def create():
    return displayForm()


@arrendador_bp.route('/edit/<int:person_id>', methods =['GET','POST'])
def edit_person(person_id):
   try:
        arrendador = Arrendador.query.filter_by(id=int(person_id)).one()
        print(arrendador.nombres)
        return displayForm(arrendador,person_id)
   
   except :
        return render_template('not_found.html')
   
@arrendador_bp.route('/update/<edit_id>', methods =['GET','POST'])
def update_person(edit_id):
    typeScape=escape(edit_id)
    if typeScape == 'new':
       addArrendador = Arrendador()
    elif typeScape.isdigit():
        addArrendador = Arrendador.query.filter_by(id=int(typeScape)).one()
    else:
        return redirect(url_for('arrendador.index'))
    
    addArrendador.tipoid    =request.form['tipoid']
    addArrendador.idnumber    =request.form['idnumber']
    addArrendador.nombres    =request.form['nombres'].strip()
    addArrendador.estado    =request.form['estado']
    addArrendador.apellidos    =request.form['apellidos'].strip()
    addArrendador.email    =request.form['email'].strip()
    addArrendador.movil    =request.form['movil']
    addArrendador.pais_exp    =request.form['pais_exp']
    addArrendador.provincia_exp    =request.form['provincia_exp']
    addArrendador.ciudad_exp    =request.form['ciudad_exp']
    
    db.session.add(addArrendador)
    db.session.commit()

    return redirect(url_for('arrendador.index'))
    

@arrendador_bp.route('/delete/<int:person_id>', methods =['GET','POST'])
def delete_person(person_id):
    
    try:
        item = Arrendador.query.filter_by(id=person_id).one()
        if item:
            db.session.delete(item)
            db.session.commit()
        return redirect(url_for('arrendador.index'))
    except :
        return render_template('not_found.html')

def displayForm(arrendador = None, edit_id = 'new'):
    if arrendador is None:
        arrendador = Arrendador()
    idsType = tipoIdList
    estados = estadoList
    citiesQuery = Cities.query.all()
    cityData = CityPicklist(cityQuery=citiesQuery)
    ciudades = cityData.getciudades()
    provincias = cityData.getprovincias()
    paises = cityData.getpaises()
    return render_template('arrendador/formArrendador.html',
                           edit_id = edit_id,
                           arrendador = arrendador,
                           idsType = idsType,
                           estados = estados,
                           ciudades = ciudades,
                           provincias = provincias,
                           paises = paises)





        
    

        
    
   
