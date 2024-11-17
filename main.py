# Importaciones
from flask import Flask
from flask_restful import Api

import vinoteca

# API
from recursos import *

# Configurar la app de Flask
app = Flask(__name__)
api = Api(app)

# Inicializar la vinoteca
if __name__ == "__main__":
    vinoteca.Vinoteca.inicializar()

    api = Api(app)
    api.add_resource(RecursoBodega, '/api/bodegas/<id>')
    api.add_resource(RecursoBodegas, '/api/bodegas')
    api.add_resource(RecursoCepa, '/api/cepas/<id>')
    api.add_resource(RecursoCepas, '/api/cepas')
    api.add_resource(RecursoVino, '/api/vinos/<id>')
    api.add_resource(RecursoVinos, '/api/vinos')

    app.run(debug=True)
