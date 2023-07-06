#paquteria de flas
from flask import Flask,render_template,request, redirect,url_for,flash
from flask_mysqldb import MySQL

#la inicializacion del app 
app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='dbflas'
app.secret_key='mysecretkey'
MySQL=MySQL(app)
#declaracion o inicializacion de las rutas y le pertenece a http://localhost:5000
@app.route('/')
def index():
        cc=MySQL.connection.cursor();
        cc.execute('select * from Albums')
        #guardar consulta
        conAlbums=cc.fetchall();
        print(conAlbums)
        return render_template('index.html',listalbums=conAlbums)
@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method == 'POST':
        #pasamos a variables el contenido de los input
        Vtitulo=request.form['txtTitulo']
        Vartista=request.form['txtArtista']
        Vanio=request.form['txtAnio']
    
        #conectar y ejecutar el insert
        CS= MySQL.connection.cursor()
        CS. execute('insert into Albums(titulo,artista,anio) values(%s,%s,%s)',(Vtitulo,Vartista,Vanio))
        MySQL.connection.commit()
    flash('EL ALBUM FUE AGREGADO EXITOSAMENTE')
    return redirect(url_for('index'))

@app.route('/editar/<id>')
def editar(id):
    CursorId= MySQL.connection.cursor()
    CursorId.execute('select * from Albums where id= %s',(id,))
    consulId= CursorId.fetchone()  
    return render_template('Editar.html', Album=consulId)

@app.route('/update/<id>', methods=['POST'])
def update(id):
   if request.method == 'POST':
    Vtitulo=request.form['txtTitulo']
    Vartista=request.form['txtArtista']
    Vanio=request.form['txtAnio']
    curAct= MySQL.connection.cursor()
    curAct.execute('update Albums set titulo= %s,artista= %s, anio= %s  where id= %s',(Vtitulo,Vartista,Vanio,id))
    MySQL.connection.commit()
    
    
    flash('Se actualizo el Album'+Vtitulo)    
    return redirect(url_for('index'))
   
@app.route('/eliminar/<id>')
def eliminar(id):
    CursorId= MySQL.connection.cursor()
    CursorId.execute('select * from Albums where id=%s',(id,))
    consulId= CursorId.fetchone()  
    return render_template('eliminar.html', Album=consulId)

@app.route('/delete/<id>', methods=['POST'])
def delete(id):
   if request.method == 'POST':
    Vtitulo=request.form['txtTitulo']


    curAct= MySQL.connection.cursor()
    curAct.execute('delete from Albums where id= %s',(id))
    MySQL.connection.commit()
    
    
    flash('Se borro el Album'+Vtitulo)    
    return redirect(url_for('index'))

#ejecucion del servidor y asignacion del puerto a trabajar
if __name__ == '__main__':
    app.run(port=5000 ,debug= True)