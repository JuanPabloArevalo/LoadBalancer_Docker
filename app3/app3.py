from flask import request, Flask, jsonify
from flask_pymongo import  PyMongo
from bson.json_util import dumps
from datetime import datetime
import json

app1 = Flask(__name__)

app1.config['MONGO_DBNAME'] = 'cadenas'
app1.config['MONGO_URI'] = 'mongodb://mongo:27017/cadenas'
mongo = PyMongo(app1)

@app1.route('/')
def index():
    try:
        args = request.args
        cadena_param = args['cadena']
    except:
        cadena_param = 'Sin Cadena'
    ip = request.remote_addr
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    cadena = mongo.db.cadena
    cadena.insert({'fecha':dt_string, 'cadena':cadena_param, 'ip':ip})
    resultados = cadena.find().sort([('fecha', -1)]).limit(10)
    return jsonify({'Resultado Servicio 3':dumps(resultados)})
    

if __name__ == '__main__':
    app1.run(debug=True, host='0.0.0.0')