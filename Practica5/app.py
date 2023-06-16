#paquteria de flas
from flask import Flask,render_template,request
from flask_mysqldb import MySQL

#la inicializacion del app 
app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='dbflask'
MySQL=MySQL(app)
#declaracion o inicializacion de las rutas y le pertenece a http://localhost:5000
@app.route('/')
def index():
        return render_template('index.html')
@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method == 'POST':
        titulo=request.form['txtTitulo']
        artista=request.form['textArtista']
        anio=request.form['txtAnio']
        print(titulo,artista,anio)

    return "Se guardo en la Base de Datos"

@app.route('/eliminar')
def eliminar():
    return "Se elimino de la Base de Datos"


#ejecucion del servidor y asignacion del puerto a trabajar
if __name__ == '__main__':
        app.run(port=5000 ,debug= True)

