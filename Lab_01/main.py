from flask import Flask, jsonify, request

app = Flask(__name__)
peliculas = [
    {'id': 1, 'titulo': 'Indiana Jones', 'genero': 'Acción'},
    {'id': 2, 'titulo': 'Star Wars', 'genero': 'Acción'},
    {'id': 3, 'titulo': 'Interstellar', 'genero': 'Ciencia ficción'},
    {'id': 4, 'titulo': 'Jurassic Park', 'genero': 'Aventura'},
    {'id': 5, 'titulo': 'The Avengers', 'genero': 'Acción'},
    {'id': 6, 'titulo': 'Back to the Future', 'genero': 'Ciencia ficción'},
    {'id': 7, 'titulo': 'The Lord of the Rings', 'genero': 'Fantasía'},
    {'id': 8, 'titulo': 'The Dark Knight', 'genero': 'Acción'},
    {'id': 9, 'titulo': 'Inception', 'genero': 'Ciencia ficción'},
    {'id': 10, 'titulo': 'The Shawshank Redemption', 'genero': 'Drama'},
    {'id': 11, 'titulo': 'Pulp Fiction', 'genero': 'Crimen'},
    {'id': 12, 'titulo': 'Fight Club', 'genero': 'Drama'}
]


def obtener_peliculas():
    return jsonify(peliculas)


def obtener_pelicula(id):
    # Lógica para buscar la película por su ID y devolver sus detalles
    pelicula_encontrada = None               #inicializamos la pelicula
    for pelicula in peliculas:               #recorremos todas las peliculas 
        if pelicula['id'] == id:
            pelicula_encontrada = pelicula
    if pelicula_encontrada:
        return jsonify(pelicula_encontrada)  #si la encontramos la devolvemos
    else:
        return jsonify({'error': 'Película no encontrada'}), 404  #si no la encontramos da error


def agregar_pelicula():
    nueva_pelicula = {
        'id': obtener_nuevo_id(),
        'titulo': request.json['titulo'],
        'genero': request.json['genero']
    }
    peliculas.append(nueva_pelicula)
    print(peliculas)
    return jsonify(nueva_pelicula), 201


def actualizar_pelicula(id):
    # Lógica para buscar la película por su ID y actualizar sus detalles
    pelicula_actualizada = None
    for pelicula in peliculas:
        if pelicula['id'] == id:
            pelicula_actualizada = pelicula
    if pelicula_actualizada is None:
        return jsonify({'mensaje': 'Película no encontrada'}), 404
    pelicula_actualizada['titulo'] = request.json['titulo']
    pelicula_actualizada['genero'] = request.json['genero']   
    return jsonify(pelicula_actualizada)


def eliminar_pelicula(id):
    # Lógica para buscar la película por su ID y eliminarla
    pelicula_a_eliminar = None
    for pelicula in peliculas:
        if pelicula['id'] == id:
            pelicula_a_eliminar = pelicula
    if pelicula_a_eliminar is None:
        return jsonify({'mensaje': 'Película no encontrada'}), 404
    peliculas.remove(pelicula_a_eliminar)
    return jsonify({'mensaje': 'Película eliminada correctamente'})


def obtener_nuevo_id():
    if len(peliculas) > 0:
        ultimo_id = peliculas[-1]['id']
        return ultimo_id + 1
    else:
        return 1
    
#inciso b#
def peliculas_filtradas(genero):
    peliculas_filtradas = []
    for pelicula in peliculas:
        if pelicula['genero'].lower() == genero.lower():
            peliculas_filtradas.append(pelicula)
        if not peliculas_filtradas:
            return jsonify({'mensaje': 'Película no encontrada'}), 404
    return jsonify(peliculas_filtradas)




app.add_url_rule('/peliculas', 'obtener_peliculas', obtener_peliculas, methods=['GET'])
app.add_url_rule('/peliculas/<int:id>', 'obtener_pelicula', obtener_pelicula, methods=['GET'])
app.add_url_rule('/peliculas', 'agregar_pelicula', agregar_pelicula, methods=['POST'])
app.add_url_rule('/peliculas/<int:id>', 'actualizar_pelicula', actualizar_pelicula, methods=['PUT'])
app.add_url_rule('/peliculas/<int:id>', 'eliminar_pelicula', eliminar_pelicula, methods=['DELETE'])
#endpoint inciso b
app.add_url_rule('/peliculas/genero/<string:genero>', 'peliculas_filtradas', peliculas_filtradas, methods=['GET'])


if __name__ == '__main__':
    app.run()
