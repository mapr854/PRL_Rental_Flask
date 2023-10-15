from flask import Blueprint, render_template, request,url_for,redirect
import pandas as pd
from markupsafe import escape
from models import Cities,Inventario
from utils.db_sqlite import db
from utils.searchQuery import search_Inventario
from utils.pickLists import *
from utils.shareFun import *


inventario_bp = Blueprint('inventario', __name__)

@inventario_bp.route('/')
def index():
    results= Inventario.query.filter(Inventario.estado == 'A').all()
        
    return render_template('inventario/inventarioTable.html',  results =results)

@inventario_bp.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form.get('search_term')
        results = search_Inventario(search_term)
        
        return render_template('inventario/inventarioTable.html', results = results)

    return redirect(url_for('inventario.index'))

@inventario_bp.route('/form', methods=['GET'])
def create():
    return displayForm()


@inventario_bp.route('/edit/<int:item_id>', methods =['GET','POST'])
def edit_inventario(item_id):
   try:
        inventario = Inventario.query.filter_by(id=int(item_id)).one()
        return displayForm(inventario,item_id)
   
   except :
        return render_template('not_found.html')
   
@inventario_bp.route('/update/<edit_id>', methods =['GET','POST'])
def update_inventario(edit_id):
    typeScape=escape(edit_id)
    if typeScape == 'new':
       addInventario = Inventario()
    elif typeScape.isdigit():
        addInventario = Inventario.query.filter_by(id=int(typeScape)).one()
    else:
        return redirect(url_for('inventario.index'))
    
    addInventario.estado    =request.form['estado']
    addInventario.descripcion    =request.form['descripcion'].strip()
    addInventario.valor    =request.form['valor']
     
    
    db.session.add(addInventario)
    db.session.commit()

    return redirect(url_for('inventario.index'))
    

@inventario_bp.route('/delete/<int:item_id>', methods =['GET','POST'])
def delete_inventario(item_id):
    
    try:
        item = Inventario.query.filter_by(id=item_id).one()
        if item:
            db.session.delete(item)
            db.session.commit()
        return redirect(url_for('inventario.index'))
    except :
        return render_template('not_found.html')

def displayForm(inventario = None, edit_id = 'new'):
    if inventario is None:
        inventario = Inventario()
    
    estados = estadoList
    
    return render_template('inventario/formInventario.html',
                           edit_id = edit_id,
                           inventario = inventario,
                           estados = estados
                           )





        
    

        
    
   
