from datetime import datetime

def strTimeDate(fecha_str):
    return  datetime.strptime(fecha_str, '%Y-%m-%d') 