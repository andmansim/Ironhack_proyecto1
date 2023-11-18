from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/guardar_datos', methods=['POST'])
def guardar_datos():
    # Recoge los datos del formulario enviados por el cliente
    fortaleza = request.form.get('fortaleza')
    reflejos = request.form.get('reflejos')
    voluntad = request.form.get('voluntad')
    inteligencia = request.form.get('inteligencia')

    # Puedes hacer lo que quieras con los datos, por ejemplo, imprimirlos en la consola
    print("Fortaleza:", fortaleza)
    print("Reflejos:", reflejos)
    print("Voluntad:", voluntad)
    print("Inteligencia:", inteligencia)

    # Puedes realizar otras operaciones aquí, como almacenar los datos en una base de datos, etc.

    # Devuelve una respuesta al cliente (puede ser opcional)
    return 'Datos recibidos con éxito'

if __name__ == '__main__':
    app.run(debug=True)
