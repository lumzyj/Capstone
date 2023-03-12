import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json

from models import setup_db, Movies, Actors
from auth.auth import AuthError, requires_auth
# rtyuikolkjhgfcv

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)


# GET ACTORS
  @app.route('/actor')
  def getActors():
    try:
      actor = Actors.query.all()
      actor = [actor.short() for Actor in actor]
      return jsonify({
        'success': True,
        'status_code': 200,
        'actor': actor,
      })
    except:
      abort(422)
  

  # GET MOVIES
  @app.route('/movies')
  def getMovies():
    try:
      movies = Movies.query.all()
      movies = [movies.short() for Actor in movies]
      return jsonify({
        'success': True,
        'status_code': 200,
        'movies': movies,
      })
    except:
      abort(422)

# POST MOVIES

  @app.route('/movies', methods=['POST'])
  @requires_auth('post:movies')
  def new_movies(payload):
    try:
      body = request.get_json()
      if body is None:
        abort(404)
      new_title = body.get('title')
      new_release_date = body.get('release_date')
      new_movies = Movies(title=new_title, release_date=json.dumps(new_release_date))
      new_movies.insert()
      new_movies = Movies.query.filter_by(id=new_movies.id).first()
      return jsonify({
        'success': True,
        'movie': [new_movies.long()]
      })
    except:
      abort(422)
  
# POST ACTORS

  @app.route('/actor', methods=['POST'])
  @requires_auth('post:actors')
  def new_actor(payload):
    try:
      body = request.get_json()
      if body is None:
        abort(404)
      new_name = body.get('name')
      new_age = body.get('age')
      new_gender = body.get('gender')
      new_actor = Actors(name=new_name, age=json.dumps(new_age), gender=json.dumps(new_gender))
      new_actor.insert()
      new_actor = Actors.query.filter_by(id=new_actor.id).first()
      return jsonify({
        'success': True,
        'actor': [new_actor.long()]
      })
    except:
      abort(422)


# PATCH MOVIES

  @app.route('/movies/<int:movies_id>', methods=['PATCH'])
  @requires_auth('patch:movies')
  def edit_movies(payload, movies_id):
    movie = Movies.query.filter_by(id=movies_id).first()
    if movie is None:
      abort(404)
    data = lambda val: request.get_json().get(val)
    try:
      if data('title'):
        movie.title = request.get_json()['title']
      if data('release_date'):
        movie.release_date = json.dumps(request.get_json()['release_date'])
      movie.update()
      return jsonify({
        'success': True,
        'movie': [movie.long()]
      }), 200
    except Exception:
      abort(422)


# PATCH ACTORS

  @app.route('/actor/<int:actors_id>', methods=['PATCH'])
  @requires_auth('patch:actors')
  def edit_actors(payload, actors_id):
    actors = Actors.query.filter_by(id=actors_id).first()
    if actors is None:
      abort(404)
    data = lambda val: request.get_json().get(val)
    try:
      if data('name'):
        actors.name = request.get_json()['name']
      if data('age'):
        actors.age = json.dumps(request.get_json()['age'])
      if data('age'):
        actors.gender = json.dumps(request.get_json()['gender'])
      actors.update()
      return jsonify({
        'success': True,
        'actors': [actors.long()]
      }), 200
    except Exception:
      abort(422)

# DELETE MOVIES
  @app.route('/movies/<int:movies_id>', methods=['DELETE'])
  @requires_auth('delete:movies')
  def delete_movies(payload, movies_id):
    movie = Movies.query.filter_by(id=movies_id).first()
    if movie is None:
      abort(404)
    try:
      movie.delete()
      return jsonify({
        'success': True,
        'delete': movies_id
      }), 200
    except:
      abort(422)


  # Error Handling


  @app.errorhandler(422)
  def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422


  @app.errorhandler(404)
  def not_found(error):
        return jsonify({
                "success": False, 
                "error": 404,
                "message": "resource not found"
                }), 404

  @app.errorhandler(AuthError)
  def authError(error):
        return jsonify({
                "success": False, 
                "error": 401,
                "message": "Authorized error"
                }), 401

  @app.errorhandler(403)
  def permissionError(error):
        return jsonify({
                "success": False, 
                "error": 403,
                "message": "Permission denied"
                }), 403

  return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)