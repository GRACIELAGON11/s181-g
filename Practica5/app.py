#paquteria de flas
from flask import Flask

#la inicializacion del app 
app=Flask(__name__)
#declaracion o inicializacion de las rutas y le pertenece a http://localhost:5000
@app.route('/')
def index():
        return "Hola mundo Flask"

@app.route('/guardar')
def guardar():
    return "se guardo"

@app.route('/eliminar')
def eliminar():
    return "se elimino "


#ejecucion del servidor y asignacion del puerto a trabajar
if __name__ == '__main__':
        app.run(port=4000 ,debug= True)

