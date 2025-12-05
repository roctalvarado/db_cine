from flask import Flask, render_template, request, redirect, url_for, flash
from entities.cliente import Cliente
from entities.pelicula import Pelicula

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_flash'  # Necesario para mensajes flash

# --- RUTA PRINCIPAL ---
@app.route('/')
def index():
    return render_template('index.html')

# ==========================================
# RUTAS PARA CLIENTES
# ==========================================

@app.route('/clientes')
def clientes():
    lista_clientes = Cliente.get_all()
    return render_template('clientes.html', clientes=lista_clientes)

@app.route('/save_cliente', methods=['POST'])
def save_cliente():
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    email = request.form['email']
    fecha = request.form['fecha_registro']
    
    nuevo_cliente = Cliente(nombre=nombre, telefono=telefono, email=email, fecha_registro=fecha)
    if nuevo_cliente.save():
        flash('Cliente guardado exitosamente', 'success')
    else:
        flash('Error al guardar cliente', 'danger')
        
    return redirect(url_for('clientes'))

@app.route('/update_cliente', methods=['POST'])
def update_cliente():
    id_cliente = request.form['id']
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    email = request.form['email']
    fecha = request.form['fecha_registro']
    
    cliente = Cliente(id=id_cliente, nombre=nombre, telefono=telefono, email=email, fecha_registro=fecha)
    
    if cliente.update():
        flash('Cliente actualizado exitosamente', 'success')
    else:
        flash('Error al actualizar cliente', 'danger')
        
    return redirect(url_for('clientes'))

@app.route('/delete_cliente/<int:id>')
def delete_cliente(id):
    cliente = Cliente(id=id)
    if cliente.delete():
        flash('Cliente eliminado exitosamente', 'success')
    else:
        flash('Error al eliminar cliente', 'danger')
    return redirect(url_for('clientes'))

# ==========================================
# RUTAS PARA PELICULAS
# ==========================================

@app.route('/peliculas')
def peliculas():
    lista_peliculas = Pelicula.get_all()
    return render_template('peliculas.html', peliculas=lista_peliculas)

@app.route('/save_pelicula', methods=['POST'])
def save_pelicula():
    titulo = request.form['titulo']
    duracion = request.form['duracion_minutos']
    clasificacion = request.form['clasificacion']
    genero = request.form['genero']
    
    nueva_pelicula = Pelicula(titulo=titulo, duracion_minutos=duracion, clasificacion=clasificacion, genero=genero)
    
    if nueva_pelicula.save():
        flash('Película guardada exitosamente', 'success')
    else:
        flash('Error al guardar película', 'danger')
        
    return redirect(url_for('peliculas'))

@app.route('/update_pelicula', methods=['POST'])
def update_pelicula():
    id_pelicula = request.form['id']
    titulo = request.form['titulo']
    duracion = request.form['duracion_minutos']
    clasificacion = request.form['clasificacion']
    genero = request.form['genero']
    
    pelicula = Pelicula(id=id_pelicula, titulo=titulo, duracion_minutos=duracion, clasificacion=clasificacion, genero=genero)
    
    if pelicula.update():
        flash('Película actualizada exitosamente', 'success')
    else:
        flash('Error al actualizar película', 'danger')
        
    return redirect(url_for('peliculas'))

@app.route('/delete_pelicula/<int:id>')
def delete_pelicula(id):
    pelicula = Pelicula(id=id)
    if pelicula.delete():
        flash('Película eliminada exitosamente', 'success')
    else:
        flash('Error al eliminar película', 'danger')
    return redirect(url_for('peliculas'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)