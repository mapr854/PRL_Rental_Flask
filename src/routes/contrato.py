from flask import Blueprint, render_template, request,url_for,redirect
import pandas as pd
from markupsafe import escape
from models import Cities,Contrato
from utils.db_sqlite import db
from utils.searchQuery import search_Contrato
from utils.pickLists import *
from utils.shareFun import *


contrato_bp = Blueprint('contrato', __name__)

@contrato_bp.route('/')
def index():
    results= Contrato.query.filter(Contrato.estado == 'A').all()
        
    return render_template('contrato/contratoTable.html',  results =results)

@contrato_bp.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form.get('search_term')
        contState = request.form.get('contState')
        results = search_Contrato(search_term, contState)
        
        return render_template('contrato/contratoTable.html', results = results)

    return redirect(url_for('contrato.index'))

@contrato_bp.route('/form', methods=['GET'])
def create():
    return displayForm()


@contrato_bp.route('/edit/<int:item_id>', methods =['GET','POST'])
def edit_contrato(item_id):
   try:
        contrato = Contrato.query.filter_by(id=int(item_id)).one()
        return displayForm(contrato,item_id)
   
   except :
        return render_template('not_found.html')
   
@contrato_bp.route('/update/<edit_id>', methods =['GET','POST'])
def update_contrato(edit_id):
    typeScape=escape(edit_id)
    if typeScape == 'new':
       addContrato = Contrato()
    elif typeScape.isdigit():
        addContrato = Contrato.query.filter_by(id=int(typeScape)).one()
    else:
        return redirect(url_for('contrato.index'))
    
    addContrato.contractType    =request.form['contractType']
    addContrato.precio    =request.form['precio']
    addContrato.administracion    =request.form['administracion']
    addContrato.startDate = strTimeDate(request.form['startDate'])
    addContrato.endDate = strTimeDate(request.form['endDate'])
    addContrato.months    =request.form['months']
    addContrato.bono    =request.form['bono']
    addContrato.poliza    =request.form['poliza'].strip()
    addContrato.estado    =request.form['estado']
    
    db.session.add(addContrato)
    db.session.commit()

    return redirect(url_for('contrato.index'))
    

@contrato_bp.route('/delete/<int:item_id>', methods =['GET','POST'])
def delete_contrato(item_id):
    
    try:
        item = Contrato.query.filter_by(id=item_id).one()
        if item:
            db.session.delete(item)
            db.session.commit()
        return redirect(url_for('contrato.index'))
    except :
        return render_template('not_found.html')

def displayForm(contrato = None, edit_id = 'new'):
    if contrato is None:
        contrato = Contrato()
    rentalType = tipoAlquilerList
    estados = estadoList
    
    return render_template('contrato/formContrato.html',
                           edit_id = edit_id,
                           contrato = contrato,
                           rentalType = rentalType,
                           estados = estados,
                           )





        
    

        
    
   
