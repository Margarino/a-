import RegionClass
import crudRegion
from flask import Flask,render_template,request,flash,redirect,url_for

app = Flask(__name__)

#TODO:
# Rig with html
@app.route('/')

def Index():
    datos = crudRegion.query()
    return render_template('registro-region.html' , region = datos) #check html for this one

@app.route('/crud' ,methods = ['POST'])

def crud():
    if request.method == 'POST': #insert
        try:
            auxInsertBtn = request.form['insertBtn'] #check html for accurate id
            if auxInsertBtn == 'insert': #see above comment
                auxNombre = request.form['txtNombre']
                auxNro_region = request.form['txtNroregion']
                auxRegion = RegionClass.Region(auxNombre,auxNro_region)
                flash ('datos de region insertados correctamente')
        except:
            flash('error al insertar en la base de datos')
        try:
            auxUpdateBtn = request.form['updateBtn']
            if auxUpdateBtn == 'update':
                auxNombre = request.form['txtNombre']
                auxNro_region = request.form['txtNroregion']
                auxRegion = RegionClass.Region(auxNombre,auxNro_region)
                crudRegion.update(auxRegion)
                flash('datos de region actualizados')
        except:
                flash('error al actualizar en la base de datos')
        try:
            auxDeleteBtn = request.form['deleteBtn']
            if auxDeleteBtn == 'delete':
                auxNro_region = request.form['txtNro_region']
                flash ('datos eliminados')
        except:
                flash('error al eliminar de la base de datos')
if __name__ == '__main__':
    app.run(port=3002,debug=True)