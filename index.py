#!/usr/bin/python -tt
# Importar Flask
import time
from flask import Flask, redirect, render_template, request
# Instancia de Flask. Aplicación
app = Flask(__name__, template_folder='template')

# Lista de productos para el carrito de compra
productos = []
mensajelista = []

# Define la ruta principal


@app.route('/')
# Función para llamar a la página index.html
def index():
    return render_template("principal.html")

# Define la ruta


@app.route('/ofertas')
# Función para llamar a la página index.html
def ofertas():
    return render_template("ofertas.html")

# Define la ruta


@app.route('/tips')
# Función para llamar a la página index.html
def tips():
    return render_template("tips.html")

# Define la ruta

#####################################################

@app.route('/contacto', methods=["GET", "POST"])
# Función para llamar a la página index.html
def contacto():
    """ Crea la fincion enviarContacto()
            Parametros
            --------------------------------------
            nombre : str
            apellido : str
            correo : str
            telefono : num
            mensaje : str

            Retorna
            --------------------------------------
            redireccion : contacto
                redirecciona a la pagina de contacto

        """
    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    correo = request.form.get("correo")
    telefono = request.form.get("telefono")
    mensajee = request.form.get("mensajee")

    if request.method == "GET":
        return render_template("contactos.html")
    else:
        mensajelista = [
            nombre,
            apellido,
            correo,
            telefono,
            mensajee
            ]
        mensaje.append(mensajelista)
        return redirect("/contacto")

##########################################################
# Define la ruta
# Recibe los datos de los productos para agregarlos al carrito


@app.route('/enviar', methods=["GET", "POST"])
# Función para obtener los productos para agregarlos al carrito
def enviarDatos():
    """ Crea la fincion enviarDatos()
            Parametros
            --------------------------------------
            producto : str
            precio : str
            cantidad : str

            Retorna
            --------------------------------------
            redireccion : 
                redirecciona a la pagina de carrito
        """
    producto = request.form.get("producto")
    precio = request.form.get("precio")
    cantidad = request.form.get("cantidad")

    if request.method == "GET":
        return render_template("sandaliasCuña.html")
    else:
        data =[
            producto,
            precio,
            cantidad
        ]
        productos.append(data)
        return redirect("/carrito")


###########################################################
# Define la ruta envia datos sandilias- dedo
@app.route('/enviar-sandalias-dedo', methods=["GET", "POST"])
# Función para llamar obtener los datos de los productos sandalias dedo
def enviarSandaliasDedo():
    """ Crea la fincion enviarSandaliasDedo()
            Parametros
            --------------------------------------
            producto : str
            precio : str
            cantidad : str

            Retorna
            --------------------------------------
            redireccion : 
                redirecciona a la pagina de carrito
        """ 
    producto = request.form.get("producto")
    precio = request.form.get("precio")
    cantidad = request.form.get("cantidad")
    #Dastos sandalias
    if request.method == "GET":
        return render_template("sandaliasDedo.html")
    else:
        data =[
            producto,
            precio,
            cantidad
        ]
        productos.append(data)
        return redirect("/carrito")

#############################################################
# Define la ruta envia datos sandilias-planas
@app.route('/enviar-sandalias-plana', methods=["GET", "POST"])
# Función para llamar obtener los datos de los productos sandalias planas
def enviarSandaliasPlana():
    """ Crea la fincion enviarSandaliasPlana()
            Parametros
            --------------------------------------
            producto : str
            precio : str
            cantidad : str

            Retorna
            --------------------------------------
            redireccion : 
                redirecciona a la pagina de carrito
        """ 
    
    producto = request.form.get("producto")
    precio = request.form.get("precio")
    cantidad = request.form.get("cantidad")

    if request.method == "GET":
        return render_template("sandaliasPlanas.html")
    else:
        data =[
            producto,
            precio,
            cantidad
        ]
        productos.append(data)
        return redirect("/carrito")

#############################################################
# Define la ruta envia datos sandilias-verano
@app.route('/enviar-sandalias-verano', methods=["GET", "POST"])
# Función para llamar obtener los datos de los productos sandalias verano
def enviarSandaliasVerano():
    
    """Crea la fincion enviarSandaliasPlana()
            Parametros
            --------------------------------------
            producto : str
            precio : str
            cantidad : str

            Retorna
            --------------------------------------
            redireccion : 
                redirecciona a la pagina de carrito
        """ 
    producto = request.form.get("producto")
    precio = request.form.get("precio")
    cantidad = request.form.get("cantidad")

    if request.method == "GET":
        return render_template("sandaliasVerano.html")
    else:
        data =[
            producto,
            precio,
            cantidad
        ]
        productos.append(data)
        return redirect("/carrito")

# Define la ruta
@app.route('/mensaje')
# Función para llamar a la pagina carrito
def mensaje():
    return render_template("mensajes.html", mensajelista=mensajelista)

# Define la ruta
@app.route('/carrito')
# Función para llamar a la pagina carrito
def carrito():
    return render_template("carrito.html", productos= productos)

# Definimos la ruta

@app.route('/comprar')
# Función para  limpiar la lista  imita la compra de productos
def comprar():

    productos.clear()
    time.sleep(2)
    return render_template("carrito.html")

# main del programa
if __name__ == "__main__":
    # Iniciamos la apicación en modo debug
    app.run(debug=True)
