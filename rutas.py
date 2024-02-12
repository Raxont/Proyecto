"""Creacion de las rutas en los diccionarios: 
- Fundamentos de programación (Introducción a la algoritmia, PSeInt y Python)
- Programación Web (HTML, CSS y Bootstrap).
- Programación formal (Java, JavaScript, C#).
- Bases de datos (Mysql, MongoDb y Postgresql). Cada ruta tiene un SGDB principal y un alternativo.
- Backend (NetCore, Spring Boot, NodeJS y Express)."""
def rutass(campers,trainers):
    d={
        "Fundamentos de programación":{
            1:{
              'hora':[{1:"0-4",'nombre': 'Introducción a la algoritmia','capacidad': 33,'campers': campers},
                     {2:"4-8",'nombre': 'PSeInt','capacidad': 33,'campers': campers},
                     {3:"8-12",'nombre': 'Python','capacidad': 33,'campers': campers}],
              'trainers': trainers
              },
            2:{
              'hora':[{1:"0-4",'nombre': 'Introducción a la algoritmia','capacidad': 33,'campers': campers},
                     {2:"4-8",'nombre': 'PSeInt','capacidad': 33,'campers': campers},
                     {3:"8-12",'nombre': 'Python','capacidad': 33,'campers': campers}],
              'trainers': trainers
              },
            3:{
              'hora':[{1:"0-4",'nombre': 'Introducción a la algoritmia','capacidad': 33,'campers': campers},
                     {2:"4-8",'nombre': 'PSeInt','capacidad': 33,'campers': campers},
                     {3:"8-12",'nombre': 'Python','capacidad': 33,'campers': campers}],
              'trainers': trainers
              }
            },
        "Programación Web": {
            1:{'hora':[{1:"0-4",'nombre': 'Html','capacidad': 33,'campers': campers},
                     {2:"4-8",'nombre': 'CSS','capacidad': 33,'campers': campers},
                     {3:"8-12",'nombre': 'Bootstrap','capacidad': 33,'campers': campers}],
              'trainers': trainers
              },
            2:{'hora':[{1:"0-4",'nombre': 'Html','capacidad': 33,'campers': campers},
                     {2:"4-8",'nombre': 'CSS','capacidad': 33,'campers': campers},
                     {3:"8-12",'nombre': 'Bootstrap','capacidad': 33,'campers': campers}],
              'trainers': trainers
              },
            3:{'hora':[{1:"0-4",'nombre': 'Html','capacidad': 33,'campers': campers},
                     {2:"4-8",'nombre': 'CSS','capacidad': 33,'campers': campers},
                     {3:"8-12",'nombre': 'Bootstrap','capacidad': 33,'campers': campers}],
              'trainers': trainers
              },
            },
        "Programación formal": {
            '0-4':{'sala':1,
                   'capacidad': 33,
                   'campers': campers,
                   'nombre': 'Java'},
            '4-8':{'sala':2,
                   'capacidad': 33,
                   'campers': campers,
                   'nombre': 'JavaScript'},
            '8-12':{'sala':3,
                    'capacidad': 33,
                    'campers': campers,
                    'nombre': 'C#'},
            'teorico': 30, 
            'practico': 60,
            "trabajo":10,
            'trainers': trainers,
            },
        "Bases de datos": {
            '0-4':{'sala':1,
                   'capacidad': 33,
                   'campers': campers,
                   'nombre': 'Mysql'},
            '4-8':{'sala':2,
                   'capacidad': 33,
                   'campers': campers,
                   'nombre': 'MongoDb'},
            '8-12':{'sala':3,
                    'capacidad': 33,
                    'campers': campers,
                    'nombre': 'Postgresql'},
            'teorico': 30, 
            'practico': 60,
            "trabajo":10,
            'trainers': trainers,
            },
        "Backend": {
            '0-4':{'sala':1,
                   'capacidad': 33,
                   'campers': campers,
                   'nombre': 'NetCore'},
            '4-8':{'sala':2,
                   'capacidad': 33,
                   'campers': campers,
                   'nombre': 'Spring Boot'},
            '8-12':{'sala':3,
                    'capacidad': 33,
                    'campers': campers,
                    'nombre': 'NodeJS y Express'},
            'teorico': 30, 
            'practico': 60,
            "trabajo":10,
            'trainers': trainers,
            },
    }
    return d
