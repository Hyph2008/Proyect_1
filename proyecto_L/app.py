from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():

    # Si el usuario acaba de entrar a la página
    if request.method == "GET":
        return render_template("index.html")


    # Si el usuario envió el formulario
    if request.method == "POST":

        # Obtenemos el nombre escrito en index.html
        nombre = request.form["nombre"].strip().lower().split(" ")


        # Comprobamos si el nombre es correcto
        if "lesly" in nombre and "tatiana" in nombre and "cando" in nombre and "buñay" in nombre:

            # Si es correcto, mostramos imagen.html
            return render_template("imagen.html")


        # Si es incorrecto
        return render_template(
            "index.html",
            mensaje="❌ Nombre incorrecto. Inténtalo nuevamente."
        )


if __name__ == "__main__":
    app.run(debug=True)

