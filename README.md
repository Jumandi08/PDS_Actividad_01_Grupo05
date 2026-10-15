# PDS Actividad 01: Patrones creacionales (Grupo 05)

Maestría en Software, asignatura Patrones de Diseño de Software.

| Carpeta | Escenario | Patrón |
|---|---|---|
| `escenario01-factory-method/` | 01: matrícula de vehículos | Factory Method |
| `escenario02-builder/` | 02: activos fijos | Builder (pendiente de subir) |

## Escenario 01: Factory Method

Aplicación web que registra un vehículo (Auto, Camioneta o Camión) y calcula el costo de su matrícula. El código sigue el diagrama de clases final de la Figura 1 del informe.

### Cómo ejecutarla

Requiere Python 3.

```
cd escenario01-factory-method
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Se abre en http://localhost:5001.

### Correspondencia con el diagrama

| Participante | Clase | Archivo |
|---|---|---|
| Product | `Vehiculo` | `vehiculos.py` |
| ConcreteProduct | `Auto`, `Camioneta`, `Camion` | `vehiculos.py` |
| Creator | `CreadorVehiculo` | `creadores.py` |
| ConcreteCreator | `CreadorAuto`, `CreadorCamioneta`, `CreadorCamion` | `creadores.py` |
| Cliente | `ServicioMatricula` | `servicio_matricula.py` |

`ServicioMatricula` solo usa `CreadorVehiculo` y `Vehiculo`. Los datos propios de cada tipo (capacidad y uso en la camioneta; tonelaje y capacidad de carga en el camión) entran por el constructor del creador concreto. `app.py` es el único archivo que conoce los creadores concretos: elige uno según el tipo del formulario y se lo pasa al servicio.

### Fórmulas de matrícula

El enunciado no las define, así que se usaron estas. Cada una está en el método `calcularCostoMatricula` de su clase.

- Auto: 1,5 % del avalúo + 10 USD por año de antigüedad.
- Camioneta: lo mismo que el Auto, más un recargo sobre el avalúo según el uso (personal 0 %, trabajo 2 %, carga 5 %).
- Camión: 2 % del avalúo + 20 USD por tonelada + 0,5 USD por kg de capacidad de carga.
