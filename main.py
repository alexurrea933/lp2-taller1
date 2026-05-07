from flask import Flask, render_template
from datos import productos
#  crear el flask de la apliacacion 

app = Flask(__name__)

#  definicion de rutas 
@app.route("/")
def imdex ():
    return remnder_template("index.html", productos=productos)

    #programa principal
if __name__ == "__main__":
    app.run( port=8080, debug=True)
