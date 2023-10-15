from flask import Blueprint, render_template, request,url_for,redirect
import pandas as pd
from markupsafe import escape
from models import Parqueadero
from utils.db_sqlite import db
from utils.searchQuery import search_Parqueadero
from utils.pickLists import *
from utils.shareFun import *


parqueadero_bp = Blueprint('parqueadero', __name__)

@parqueadero_bp.route('/')
def index():
    results= Parqueadero.query.filter(Parqueadero.estado != 'I').all()
        
    return render_template('parqueadero/parqueaderoTable.html',  results =results)

@parqueadero_bp.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form.get('search_term')
        results = search_Parqueadero(search_term)
        
        return render_template('parqueadero/parqueaderoTable.html', results = results)

    return redirect(url_for('parqueadero.index'))

@parqueadero_bp.route('/form', methods=['GET'])
def create():
    return displayForm()


@parqueadero_bp.route('/edit/<int:item_id>', methods =['GET','POST'])
def edit_parqueadero(item_id):
   try:
        parqueadero = Parqueadero.query.filter_by(id=int(item_id)).one()
        return displayForm(parqueadero,item_id)
   
   except :
        return render_template('not_found.html')
   
@parqueadero_bp.route('/update/<edit_id>', methods =['GET','POST'])
def update_parqueadero(edit_id):
    typeScape=escape(edit_id)
    if typeScape == 'new':
       addParqueadero = Parqueadero()
    elif typeScape.isdigit():
        addParqueadero = Parqueadero.query.filter_by(id=int(typeScape)).one()
    else:
        return redirect(url_for('parqueadero.index'))
    
    addParqueadero.estado    =request.form['estado']
    addParqueadero.nplaca    =request.form['nplaca'].strip()
    addParqueadero.place    =request.form['place']
     
    
    db.session.add(addParqueadero)
    db.session.commit()

    return redirect(url_for('parqueadero.index'))
    

@parqueadero_bp.route('/delete/<int:item_id>', methods =['GET','POST'])
def delete_parqueadero(item_id):
    
    try:
        item = Parqueadero.query.filter_by(id=item_id).one()
        if item:
            db.session.delete(item)
            db.session.commit()
        return redirect(url_for('parqueadero.index'))
    except :
        return render_template('not_found.html')

def displayForm(parqueadero = None, edit_id = 'new'):
    if parqueadero is None:
        parqueadero = Parqueadero()
    
    estados = estadoList
    
    return render_template('parqueadero/formParqueadero.html',
                           edit_id = edit_id,
                           parqueadero = parqueadero,
                           estados = estados
                           )





        
    

        
    
   
