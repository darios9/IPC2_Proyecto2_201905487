from flask import Flask, request
from flask.json import jsonify
from flask_cors import CORS
from Datos import articulos


app = Flask(__name__)
app.config["DEBUG"]=True

CORS(app)

@app.route('/')
def home():
    return "Esta corriendo correctamente"


@app.route('/Producto',methods=['GET'])
def Articulos():
        return jsonify(articulos)


@app.route('/ConsultarDatos',methods=['POST'])
def ConsultarDatos():
    print('-------------------------')
    id=request.get_json()
    print(id['id'])
    ID = id['id']
    articulo =[articulo for articulo in articulos if articulo['id']== int(ID)]
    if(len(articulos)<1):
        return jsonify({'mensaje':'el articulo no existe'})    
    return jsonify({'mensaje':"SE ENCONTRO EL SIGUIENTE ARTICULO"},articulo[0])  


@app.route('/CrearEmpresa',methods=['POST'])
def CrearEmpresa():
    print('-------------------------')
    id=request.get_json()
    print(id['id'])
    ID = id['id']
    articulo =[articulo for articulo in articulos if articulo['id']== int(ID)]
    if(len(articulos)<1):
        return jsonify({'mensaje':'el articulo no existe'})    
    return jsonify({'mensaje':"SE ENCONTRO EL SIGUIENTE ARTICULO"},articulo[0])   

@app.route('/CrearCliente',methods=['POST'])
def CrearCliente():
    print('-------------------------')
    id=request.get_json()
    print(id['id'])
    ID = id['id']
    articulo =[articulo for articulo in articulos if articulo['id']== int(ID)]
    if(len(articulos)<1):
        return jsonify({'mensaje':'el articulo no existe'})    
    return jsonify({'mensaje':"SE ENCONTRO EL SIGUIENTE ARTICULO"},articulo[0])     

@app.route('/CrearPlaylist',methods=['POST'])
def CrearPlaylist():
    print('-------------------------')
    id=request.get_json()
    print(id['id'])
    ID = id['id']
    articulo =[articulo for articulo in articulos if articulo['id']== int(ID)]
    if(len(articulos)<1):
        return jsonify({'mensaje':'el articulo no existe'})    
    return jsonify({'mensaje':"SE ENCONTRO EL SIGUIENTE ARTICULO"},articulo[0])   


@app.route('/EliminarCancionPlqylist',methods=['DELETE'])
def eliminarCancion():
    id = request.get_json()
    ID = id['id']
    articulo =[articulo for articulo in articulos if articulo['id']== int(ID)]
    if(len(articulos)<1):
        return jsonify({'mensaje':'el articulo no existe'})
    articulos.remove(articulo[0])    
    return jsonify({"mensaje":"SE ELIMINO EL SIGUIENTE ARTICULO"} ,articulo[0])

@app.route('/EliminarCliente',methods=['DELETE'])
def eliminarCliente():
    id = request.get_json()
    ID = id['id']
    articulo =[articulo for articulo in articulos if articulo['id']== int(ID)]
    if(len(articulos)<1):
        return jsonify({'mensaje':'el articulo no existe'})
    articulos.remove(articulo[0])    
    return jsonify({"mensaje":"SE ELIMINO EL SIGUIENTE ARTICULO"} ,articulo[0])     


if __name__ == "__main__":
    app.run(debug=True)      