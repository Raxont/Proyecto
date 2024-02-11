"""Creacion de las rutas en los diccionarios: 
- Fundamentos de programación (Introducción a la algoritmia, PSeInt y Python)
- Programación Web (HTML, CSS y Bootstrap).
- Programación formal (Java, JavaScript, C#).
- Bases de datos (Mysql, MongoDb y Postgresql). Cada ruta tiene un SGDB principal y un alternativo.
- Backend (NetCore, Spring Boot, NodeJS y Express)."""
def rutas(d):
    d = {
    1: {
        'name': 'Fundamentos de programación ',
        'sala': {'name': 'Sala 1', 'capacidad': 33, 'campers': []},
        'sgdb_principal': {'name': 'Introducción a la algoritmia', 'peso_teorico': 30, 'peso_practico': 60},
        'sgdb_alternativo1': {'name': 'PSeInt', 'peso_teorico': 30, 'peso_practico': 60},
        'sgdb_alternativo2': {'name': 'Python', 'peso_teorico': 30, 'peso_practico': 60},
        'trainers': [],
        'modulos': [
            {'name': 'Modulo 1'},
            {'name': 'Modulo 2'},
            {'name': 'Modulo 3'}
        ]
    },
    2: {
        'name': 'Programación Web ',
        'sala': {'name': 'Sala 1', 'capacidad': 33, 'campers': []},
        'sgdb_principal': {'name': 'HTML', 'peso_teorico': 30, 'peso_practico': 60},
        'sgdb_alternativo1': {'name': 'CSS', 'peso_teorico': 30, 'peso_practico': 60},
        'sgdb_alternativo2': {'name': 'Bootstrap', 'peso_teorico': 30, 'peso_practico': 60},
        'trainers': [],
        'modulos': [
            {'name': 'Modulo 1'},
            {'name': 'Modulo 2'},
            {'name': 'Modulo 3'}
        ]
    },
    3: {
        'name': 'Programación formal ',
        'sala': {'name': 'Sala 1', 'capacidad': 33, 'campers': []},
        'sgdb_principal': {'name': 'Java', 'peso_teorico': 30, 'peso_practico': 60},
        'sgdb_alternativo1': {'name': 'JavaScript', 'peso_teorico': 30, 'peso_practico': 60},
        'sgdb_alternativo2': {'name': 'C#', 'peso_teorico': 30, 'peso_practico': 60},
        'trainers': [],
        'modulos': [
            {'name': 'Modulo 1'},
            {'name': 'Modulo 2'},
            {'name': 'Modulo 3'}
        ]
    },
    4: {
        'name': 'Bases de datos ',
        'sala': {'name': 'Sala 1', 'capacidad': 33, 'campers': []},
        'sgdb_principal': {'name': 'Mysql', 'peso_teorico': 30, 'peso_practico': 60},
        'sgdb_alternativo1': {'name': 'MongoDb', 'peso_teorico': 30, 'peso_practico': 60},
        'sgdb_alternativo2': {'name': 'Postgresql', 'peso_teorico': 30, 'peso_practico': 60},
        'trainers': [],
        'modulos': [
            {'name': 'Modulo 1'},
            {'name': 'Modulo 2'},
            {'name': 'Modulo 3'}
        ]
    },
    6: {
        'name': 'Backend ',
        'sala': {'name': 'Sala 1', 'capacidad': 33, 'campers': []},
        'sgdb_principal': {'name': 'NetCore', 'peso_teorico': 30, 'peso_practico': 60},
        'sgdb_alternativo1': {'name': 'Spring Boot', 'peso_teorico': 30, 'peso_practico': 60},
        'sgdb_alternativo2': {'name': 'NodeJS y Express', 'peso_teorico': 30, 'peso_practico': 60},
        'trainers': [],
        'modulos': [
            {'name': 'Modulo 1'},
            {'name': 'Modulo 2'},
            {'name': 'Modulo 3'}
        ]
    }
}
    return d
