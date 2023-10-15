from flask import Blueprint, render_template, request,url_for,redirect
import pandas as pd
from markupsafe import escape
from models import Cities,Arrendatario
from utils.db_sqlite import db
from utils.searchQuery import search_Arrendatario
from utils.pickLists import *
from utils.shareFun import *


arrendatario_bp = Blueprint('arrendatario', __name__)

@arrendatario_bp.route('/')
def index():
    results= Arrendatario.query.filter(Arrendatario.estado == 'A').all()
        
    return render_template('arrendatario/arrendatarioTable.html',  results =results)

@arrendatario_bp.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form.get('search_term')
        results = search_Arrendatario(search_term)
        
        return render_template('arrendatario/arrendatarioTable.html', results = results)

    return redirect(url_for('arrendatario.index'))

@arrendatario_bp.route('/form', methods=['GET'])
def create():
    return displayForm()


@arrendatario_bp.route('/edit/<int:person_id>', methods =['GET','POST'])
def edit_person(person_id):
   try:
        arrendatario = Arrendatario.query.filter_by(id=int(person_id)).one()
        return displayForm(arrendatario,person_id)
   
   except :
        return render_template('not_found.html')
   
@arrendatario_bp.route('/update/<edit_id>', methods =['GET','POST'])
def update_person(edit_id):
    typeScape=escape(edit_id)
    if typeScape == 'new':
       addArrendatario = Arrendatario()
    elif typeScape.isdigit():
        addArrendatario = Arrendatario.query.filter_by(id=int(typeScape)).one()
    else:
        return redirect(url_for('arrendatario.index'))
    
    addArrendatario.tipoid    =request.form['tipoid']
    addArrendatario.idnumber    =request.form['idnumber']
    addArrendatario.nombres    =request.form['nombres'].strip()
    addArrendatario.estado    =request.form['estado']
    addArrendatario.apellidos    =request.form['apellidos'].strip()
    addArrendatario.email    =request.form['email'].strip()
    addArrendatario.movil    =request.form['movil']
    addArrendatario.nombreContacto = request.form['nombreContacto'].strip()
    addArrendatario.movilContacto = request.form['movilContacto']
    addArrendatario.profesion = request.form['profesion']
    addArrendatario.fechaNacimiento = strTimeDate(request.form['fechaNacimiento'])
    addArrendatario.pais_exp    =request.form['pais_exp']
    addArrendatario.provincia_exp    =request.form['provincia_exp']
    addArrendatario.ciudad_exp    =request.form['ciudad_exp']
    
    db.session.add(addArrendatario)
    db.session.commit()

    return redirect(url_for('arrendatario.index'))
    

@arrendatario_bp.route('/delete/<int:person_id>', methods =['GET','POST'])
def delete_person(person_id):
    
    try:
        item = Arrendatario.query.filter_by(id=person_id).one()
        if item:
            db.session.delete(item)
            db.session.commit()
        return redirect(url_for('arrendatario.index'))
    except :
        return render_template('not_found.html')

def displayForm(arrendatario = None, edit_id = 'new'):
    if arrendatario is None:
        arrendatario = Arrendatario()
    idsType = tipoIdList
    estados = estadoList
    citiesQuery = Cities.query.all()
    cityData = CityPicklist(cityQuery=citiesQuery)
    ciudades = cityData.getciudades()
    provincias = cityData.getprovincias()
    paises = cityData.getpaises()
    return render_template('arrendatario/formArrendatario.html',
                           edit_id = edit_id,
                           arrendatario = arrendatario,
                           idsType = idsType,
                           estados = estados,
                           ciudades = ciudades,
                           provincias = provincias,
                           paises = paises)





        
    

        
    
   
