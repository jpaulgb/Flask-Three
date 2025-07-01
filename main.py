from flask import Flask

app = Flask(__name__)
#creamos el servidor y lo guardamos en app
#rutas:
#defino una ruta /app/v1/users e asociamos ruta
@app.route('/app/v1/users/<id>')
def user_action(id):
    if(id == "8"):
        return "porque me pedis 8"
    else:
        return id

#siempre se pone al final:
app.run(debug=True)