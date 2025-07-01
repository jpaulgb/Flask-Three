from flask import Flask

app = Flask(__name__)
#creamos el servidor y lo guardamos en app
#rutas:
#defino una ruta /app/v1/users e asociamos ruta
@app.route('/app/v1/users')
def user_action():
    print("estoy aca")
    return "tu usuario"

#siempre se pone al final:
app.run(debug=True)