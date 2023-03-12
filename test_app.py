import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app, Flask
from models import setup_db, Movies, Actors

app = Flask(__name__)

class CapstoneTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = os.environ['DATABASE_URL']
        if self.database_path.startswith("postgres://"):
            self.database_path = self.database_path.replace("postgres://", "postgresql://", 1)
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        pass

    # get movies
    def test_retrieve_movies(self):
        res = self.client().get("/movies")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_retrieve_movies_failure(self):
        res = self.client().get("/movies")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')


    # get Actors
    def test_retrieve_actors(self):
        res = self.client().get("/actors")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_retrieve_actors_failure(self):
        res = self.client().get("/actors")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found') 

    #Delete Movies 
    def test_delete_movies(self):
        with app.app_context():
            res = self.client().delete("/movies/1")
            data = json.loads(res.data)

            movie = Movies.query.filter(Movies.id == 10).one_or_none()

            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertTrue(data['deleted'],10)

    #Delete Movies for failure
    def test_delete_movies_failure(self):
        with app.app_context():
            res = self.client().delete("/movies/")
            data = json.loads(res.data)

            movie = Movies.query.filter(Movies.id == 10).one_or_none()

            self.assertEqual(res.status_code, 404)
            self.assertEqual(data['success'], False)
            self.assertEqual(data['message'], 'resource not found')
    
    #Delete Movies 
    def test_delete_actors(self):
        with app.app_context():
            res = self.client().delete("/actors/1")
            data = json.loads(res.data)

            actor = Actors.query.filter(Actors.id == 10).one_or_none()

            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertTrue(data['deleted'],10)

    #Delete actors for failure
    def test_delete_actors_failure(self):
        with app.app_context():
            res = self.client().delete("/actors/")
            data = json.loads(res.data)

            actor = Actors.query.filter(Actors.id == 10).one_or_none()

            self.assertEqual(res.status_code, 404)
            self.assertEqual(data['success'], False)
            self.assertEqual(data['message'], 'resource not found')

    # Add Movies
    def test_create_movies(self):
        test_movies = {'title': 'test title', 'release_date': 'test release_date'}
        res = self.client().post('/movies', json=test_movies)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # Add Movies for failure
    def test_create_question_failure(self):
        test_movies = {'title': 'test title', 'release_date': 'test release_date'}
        res = self.client().post('/movies/', json=test_movies)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data['message'], 'resource not found')


    # Add Actors
    def test_create_actors(self):
        test_actors = {'name': 'test name', 'age': 'test age', 'gender': 'test gender'}
        res = self.client().post('/actors', json=test_actors)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # Add Actors for failure
    def test_create_question_failure(self):
        test_actors = {'name': 'test name', 'age': 'test age', 'gender': 'test gender'}
        res = self.client().post('/actors/', json=test_actors)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data['message'], 'resource not found')


    # Update Movies
    def test_create_actors(self):
        test_movies = {'name': 'test name', 'age': 'test age', 'gender': 'test gender'}
        res = self.client().patch('/movies/1', json=test_movies)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_actors_failure(self):
        res = self.client().patch('/movies/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')

    # Update Actors
    def test_create_actors(self):
        test_actors = {'name': 'test name', 'age': 'test age', 'gender': 'test gender'}
        res = self.client().patch('/actors/1', json=test_actors)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_actors_failure(self):
        res = self.client().patch('/actors/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')