from sqlalchemy import or_, and_
from models import Arrendador, Arrendatario, Contrato,Inmueble,Inventario, Parqueadero

def search_Arrendador(search_term):
    # Assuming `search_term` is a user-provided input for search
    search_pattern = f"%{search_term}%"  # For case-insensitive partial matching

    # Query to filter by name, idnumber, or apellido
    results = Arrendador.query.filter(
        or_(
            Arrendador.idnumber.ilike(search_pattern),
            Arrendador.nombres.ilike(search_pattern),
            Arrendador.apellidos.ilike(search_pattern)
        )
    ).all()

    return results
def search_Arrendatario(search_term):
    # Assuming `search_term` is a user-provided input for search
    search_pattern = f"%{search_term}%"  # For case-insensitive partial matching

    # Query to filter by name, idnumber, or apellido
    results = Arrendatario.query.filter(
        or_(
            Arrendatario.idnumber.ilike(search_pattern),
            Arrendatario.nombres.ilike(search_pattern),
            Arrendatario.apellidos.ilike(search_pattern)
        )
    ).all()

    return results

def search_Inmueble(search_term):
    # Assuming `search_term` is a user-provided input for search
    search_pattern = f"%{search_term}%"  # For case-insensitive partial matching

    # Query to filter by name, idnumber, or apellido
    results = Inmueble.query.filter(
        or_(
            Inmueble.name.ilike(search_pattern),
            Inmueble.apartamento.ilike(search_pattern),
            Inmueble.habitaciones.ilike(search_pattern)
        )
    ).all()

    return results
def search_Inventario(search_term):
    # Assuming `search_term` is a user-provided input for search
    search_pattern = f"%{search_term}%"  # For case-insensitive partial matching

    # Query to filter by name, idnumber, or apellido
    results = Inventario.query.filter(
        Inventario.descripcion.ilike(search_pattern) 
    ).all()

    return results
def search_Parqueadero(search_term):
    # Assuming `search_term` is a user-provided input for search
    search_pattern = f"%{search_term}%"  # For case-insensitive partial matching

    # Query to filter by name, idnumber, or apellido
    results = Parqueadero.query.filter(
        or_(
            Parqueadero.nplaca.ilike(search_pattern),
            Parqueadero.place.ilike(search_pattern)
        )
    ).all()

    return results
    
def search_Contrato(search_term,conState):
    # Assuming `search_term` is a user-provided input for search
    search_pattern = f"%{search_term}%"  # For case-insensitive partial matching

    # Query to filter by name, idnumber, or apellido
    results = Contrato.query.filter(
        or_(
            Contrato.inmueble.name.ilike(search_pattern),
            Contrato.inmueble.apartamento.ilike(search_pattern),
            Contrato.habitaciones.ilike(search_pattern)
        ),
        and_(
        Contrato.estado == conState
    )
    ).all()

    return results


