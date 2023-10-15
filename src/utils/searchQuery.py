from sqlalchemy import or_
from models import Arrendador, Arrendatario

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
    