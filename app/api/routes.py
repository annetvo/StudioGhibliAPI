from flask import Blueprint, json, jsonify, request
from flask.wrappers import Response
from app.models import Movie, db
from .apiauthhelper import token_required

api = Blueprint('api', __name__, url_prefix='/api/')

@api.route('/movies', methods=['GET'])
def movies():
    movies = {a.movie:a.to_dict() for a in Movie.query.all()}
    return jsonify(movies)


@api.route('/movies/<int:id>')
def get_movie(id):
    try:
        movie = Movie.query.get(id).to_dict()
        return jsonify(movie)
    except:
        return jsonify(f'Hero of id: <{id}> does not exist in the database')


@api.route('/movies/<int:id>', methods=['DELETE'])
@token_required
def delete_movie(token, id):
    try:
        movie = Movie.query.get(id)
        db.session.delete(movie)
        db.session.commit()
        return jsonify({'Deleted': movie.to_dict()})
    except:
        return jsonify(f'Movie of id: <{id}> does not exist in the database')


@api.route('/movies/<int:id>', methods=['PUT'])
@token_required
def update_movie(id):
    response = request.get_json()
    print(response)
    movie = Movie.query.get(id)
    movie.from_dict(response)
    print(movie.to_dict())
    db.session.commit()
    return jsonify({'Updated': movie.to_dict()})



@api.route('createmovie',methods=['POST'])
@token_required
def create_movie(token):
    r = request.get_json()
    newMovie = Movie()
    newMovie.from_dict(r)
    print(newMovie.to_dict())
    db.session.add(newMovie)
    db.session.commit()
    return jsonify({'Created': newMovie.query.all()[-1].to_dict()})