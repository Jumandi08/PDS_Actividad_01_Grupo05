from flask import Flask, render_template, request

from creadores import CreadorAuto, CreadorCamioneta, CreadorCamion
from servicio_matricula import ServicioMatricula

app = Flask(__name__)


# Único lugar que conoce los creadores concretos: elige según el tipo del formulario.
def elegirCreador(f):
    if f["tipo"] == "auto":
        return CreadorAuto()
    if f["tipo"] == "camioneta":
        return CreadorCamioneta(f["capacidad"], f["uso"])
    if f["tipo"] == "camion":
        return CreadorCamion(float(f["tonelaje"]), float(f["capacidadCarga"]))
    raise ValueError("Tipo de vehículo no válido")


@app.route("/", methods=["GET", "POST"])
def index():
    resultado = error = None
    if request.method == "POST":
        f = request.form
        try:
            creador = elegirCreador(f)
            costo = ServicioMatricula().calcularMatricula(
                creador, f["placa"], f["marca"], f["modelo"], int(f["anioFabricacion"]), float(f["avaluo"])
            )
            resultado = {"creador": type(creador).__name__, "costo": costo}
        except (ValueError, KeyError):
            error = "Revisa los datos ingresados."
    return render_template("index.html", resultado=resultado, error=error, d=request.form)


if __name__ == "__main__":
    app.run(port=5001)
