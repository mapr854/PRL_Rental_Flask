from flask import Blueprint, render_template, request,url_for,redirect
import pandas as pd
from markupsafe import escape
from models import Arrendador, Arrendatario, Contrato,ElementosContrato, Inmueble, Inventario, Parqueadero
from utils.db_sqlite import db
from utils.searchQuery import *
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
   

@contrato_bp.route('/edit2/<int:item_id>', methods =['GET','POST'])
def edit_contrato2(item_id):
   try:
        contrato = Contrato.query.filter_by(id=int(item_id)).one()
        arrendatarioList = Arrendatario.query.filter(Arrendatario.estado == 'A')
        return render_template('contrato/formContratoP2.html',
                               nuevo_id = item_id,
                               contrato = contrato,
                               arrendatarioList = arrendatarioList
                               )
   
   except :
        return render_template('not_found.html')
   
@contrato_bp.route('/edit3/<int:item_id>', methods =['GET','POST'])
def edit_contrato3(item_id):
   try:
        contrato = Contrato.query.filter_by(id=int(item_id)).one()
        inventarioList = Inventario.query.filter(Inventario.estado == 'A')
        return render_template('contrato/formContratoP3.html',
                               nuevo_id = item_id,
                               contrato = contrato,
                               inventarioList = inventarioList
                               )
   
   except  Exception as e:
        print(e)
        return render_template('not_found.html')
   
@contrato_bp.route('/edit4/<int:item_id>', methods =['GET','POST'])
def edit_contrato4(item_id):
   try:
        contrato = Contrato.query.filter_by(id=int(item_id)).one()
        parqueaderoList = Parqueadero.query.filter(Parqueadero.estado == 'A')
        return render_template('contrato/formContratoP4.html',
                               nuevo_id = item_id,
                               contrato = contrato,
                               parqueaderoList = parqueaderoList
                               )
   
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
    addContrato.arrendador_id    =request.form['arrendador_id']
    addContrato.inmueble_id    =request.form['inmueble_id']
    
    try:
        db.session.add(addContrato)
        db.session.commit()
        nuevo_id = addContrato.id
        arrendatarioList = Arrendatario.query.filter(Arrendatario.estado == 'A')
        return render_template('contrato/formContratoP2.html',
                               nuevo_id = nuevo_id,
                               contrato = addContrato,
                               arrendatarioList = arrendatarioList
                               )

        
    except Exception as e:
        # Print or log the exception for debugging
        print(f"Error during commit: {e}")
    
        return render_template('not_found.html')
    

   

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
    
@contrato_bp.route('<int:nuevo_id>/deletearrendatario/<int:item_id>', methods =['GET','POST'])
def delete_arrendatario(nuevo_id,item_id):

    addContrato = Contrato.query.filter_by(id=nuevo_id).one()
    item = Arrendatario.query.filter_by(id=item_id).one()

    try:
        addContrato.arrendatarios.remove(item)
        db.session.commit()
            
    except Exception as e:
        print(e)
    arrendatarioList = Arrendatario.query.filter(Arrendatario.estado == 'A')
    return render_template('contrato/formContratoP2.html',
                               nuevo_id = nuevo_id,
                               contrato = addContrato,
                               arrendatarioList = arrendatarioList
                               )
    
@contrato_bp.route('<int:nuevo_id>/addarrendatario', methods =['POST'])
def add_arrendatario(nuevo_id):

    addContrato = Contrato.query.filter_by(id=nuevo_id).one()
    addArrendatario = Arrendatario.query.filter_by(id=int(request.form['arrendatario_id'])).one()
    try:        
        
       
        if addArrendatario not in addContrato.arrendatarios:
            addContrato.arrendatarios.append(addArrendatario)
            db.session.commit()
            
    except Exception as e:
        print(e)
    
    arrendatarioList = Arrendatario.query.filter(Arrendatario.estado == 'A')
    
    return render_template('contrato/formContratoP2.html',
                               nuevo_id = nuevo_id,
                               contrato = addContrato,
                               arrendatarioList = arrendatarioList
                               )
@contrato_bp.route('<int:nuevo_id>/deleteparqueadero/<int:item_id>', methods =['GET','POST'])
def delete_parqueadero(nuevo_id,item_id):
    
    addContrato = Contrato.query.filter_by(id=nuevo_id).one()
    try:
        
        item = Parqueadero.query.filter_by(id=item_id).one()

        addContrato.parqueaderos.remove(item)
        db.session.commit()
            
    except Exception as e:
        print(e)
    parqueaderoList = Parqueadero.query.filter(Parqueadero.estado == 'A')
    return render_template('contrato/formContratoP4.html',
                               nuevo_id = nuevo_id,
                               contrato = addContrato,
                               parqueaderoList = parqueaderoList
                               )
    
@contrato_bp.route('<int:nuevo_id>/addparqueadero', methods =['POST'])
def add_parqueadero(nuevo_id):
    
    addContrato = Contrato.query.filter_by(id=nuevo_id).one()
    try:
        
        addParqueadero = Parqueadero.query.filter_by(id=int(request.form['parqueadero_id'])).one()
       
        if addParqueadero not in addContrato.parqueaderos:
            addContrato.parqueaderos.append(addParqueadero)
            db.session.commit()
            
    except Exception as e:
        print(e)
        
    parqueaderoList = Parqueadero.query.filter(Parqueadero.estado == 'A')
    return render_template('contrato/formContratoP4.html',
                               nuevo_id = nuevo_id,
                               contrato = addContrato,
                               parqueaderoList = parqueaderoList
                               )

@contrato_bp.route('<int:nuevo_id>/deleteinventario/<int:item_id>', methods =['GET','POST'])
def delete_inventario(nuevo_id,item_id):

    addContrato = Contrato.query.filter_by(id=nuevo_id).one()
    try:        
        item = ElementosContrato.query.filter_by(id=item_id).one()

        addContrato.elementos.remove(item)
        db.session.commit()
            
    except Exception as e:
        print(e)
    inventarioList = Inventario.query.filter(Inventario.estado == 'A')
    return render_template('contrato/formContratoP3.html',
                               nuevo_id = nuevo_id,
                               contrato = addContrato,
                               inventarioList = inventarioList
                               )
    
@contrato_bp.route('<int:nuevo_id>/addinventario', methods =['POST'])
def add_inventario(nuevo_id):
    inventarioSelected =Inventario.query.filter_by(id=int(request.form['inventario_id'])).one()
    addElemento = ElementosContrato(    
        descripcion = inventarioSelected.descripcion,
        valor = inventarioSelected.valor,
        cantidad = request.form['cantidad'],
        contrato_id = nuevo_id
        )
        
    try:
        db.session.add(addElemento)
        db.session.commit()
            
    except Exception as e:
        print(e)
    addContrato = Contrato.query.filter_by(id=nuevo_id).one()
    inventarioList = Inventario.query.filter(Inventario.estado == 'A')
    return render_template('contrato/formContratoP3.html',
                               nuevo_id = nuevo_id,
                               contrato = addContrato,
                               inventarioList = inventarioList
                               )




def displayForm(contrato = None, edit_id = 'new'):
    if contrato is None:
        contrato = Contrato()
    rentalType = tipoAlquilerList
    estados = estadoList
    arrendadorList = Arrendador.query.filter(Arrendador.estado == 'A')
    inmuebleList = Inmueble.query.filter(Inmueble.estado == 'D')
    return render_template('contrato/formContrato.html',
                           edit_id = edit_id,
                           contrato = contrato,
                           arrendadorList = arrendadorList,
                           rentalType = rentalType,
                           inmuebleList = inmuebleList,
                           estados = estados
                           )







        
    

        
    
   
