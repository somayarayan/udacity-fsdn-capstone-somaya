import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, db_drop_and_create_all, Actor, Movie, Performance, db_drop_and_create_all
from config import bearer_tokens
from sqlalchemy import desc
from datetime import date

# Create dict with Authorization key and Bearer token as values. 
# Later used by test classes as Header

casting_assistant_auth_header = {
    'Authorization': bearer_tokens['casting_assistant']
}

casting_director_auth_header = {
    'Authorization': bearer_tokens['casting_director']
}

executive_producer_auth_header = {
    'Authorization': bearer_tokens['executive_producer']
}


#----------------------------------------------------------------------------#
# RBAC Tests I: Missing Authorization | Missing Authentificaton
#   Casting Assistant:
#   - test_error_401_get_all_movies (Authorization)
#   Casting Director:
#   - test_error_401_delete_actor (Authorization)
#   - test_error_403_delete_actor (Authentificaton)
#   Executive Producer:
#   - test_error_401_delete_movie (Authorization)
#   - test_error_403_delete_movie (Authentificaton)

# RBAC Tests II: Missing Authentificaton (i.e. missing permissions)

#----------------------------------------------------------------------------#

#----------------------------------------------------------------------------#
# Setup of Unittest
#----------------------------------------------------------------------------#

class AgencyTestCase(unittest.TestCase):
    """This class represents the agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""

        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ['DATABASE_URL']
        setup_db(self.app, self.database_path)
        db_drop_and_create_all()
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

# Test driven development (TDD): Create testcases first, then add endpoints to pass tests

#----------------------------------------------------------------------------#
# Tests for /actors POST
#----------------------------------------------------------------------------#

    def test_create_new_actor(self):
        """Test POST new actor."""

        json_create_actor = {
            'name' : 'Fernando',
            'age' : 29
        } 

        res = self.client().post('/actors', json = json_create_actor, headers = casting_director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['created'], 2)
    
    def test_error_401_new_actor(self):
        """Test POST new actor w/o Authorization."""

        json_create_actor = {
            'name' : 'Fernando',
            'age' : 29
        } 

        res = self.client().post('/actors', json = json_create_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Authorization header is expected.')

    def test_error_422_create_new_actor(self):
        """Test Error POST new actor."""

        json_create_actor_without_name = {
            'age' : 29
        } 

        res = self.client().post('/actors', json = json_create_actor_without_name, headers = casting_director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'No name provided, name is required.')

#----------------------------------------------------------------------------#
# Tests for /actors GET
#----------------------------------------------------------------------------#

    def test_get_all_actors(self):
        """Test GET all actors."""
        res = self.client().get('/actors?page=1', headers = casting_assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['actors']) > 0)

    def test_error_401_get_all_actors(self):
        """Test GET all actors w/o Authorization."""
        res = self.client().get('/actors?page=1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Authorization header is expected.')

    def test_error_404_get_actors(self):
        """Test Error GET all actors."""
        res = self.client().get('/actors?page=123456789', headers = casting_assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'] , 'No actors found.')

#----------------------------------------------------------------------------#
# Tests for /actors PATCH
#----------------------------------------------------------------------------#

    def test_edit_actor(self):
        """Test PATCH existing actors"""
        json_edit_actor_with_new_age = {
            'age' : 30
        } 
        res = self.client().patch('/actors/1', json = json_edit_actor_with_new_age, headers = casting_director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['actor']) > 0)
        self.assertEqual(data['updated'], 1)

    def test_error_400_edit_actor(self):
            """Test PATCH with non json body"""

            res = self.client().patch('/actors/123456', headers = casting_director_auth_header)
            data = json.loads(res.data)

            self.assertEqual(res.status_code, 400)
            self.assertFalse(data['success'])
            self.assertEqual(data['message'] , 'Request does not contain a valid JSON body.')

    def test_error_404_edit_actor(self):
        """Test PATCH with non valid id"""
        json_edit_actor_with_new_age = {
            'age' : 30
        } 
        res = self.client().patch('/actors/12345', json = json_edit_actor_with_new_age, headers = casting_director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'] , 'Actor with id 12345 does not exist.')

#----------------------------------------------------------------------------#
# Tests for /actors DELETE
#----------------------------------------------------------------------------#

    def test_error_401_delete_actor(self):
        """Test DELETE existing actor w/o Authorization"""
        res = self.client().delete('/actors/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Authorization header is expected.')

    def test_error_403_delete_actor(self):
        """Test DELETE existing actor with missing permissions"""
        res = self.client().delete('/actors/1', headers = casting_assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Permission not found.')

    def test_delete_actor(self):
        """Test DELETE existing actor"""
        res = self.client().delete('/actors/1', headers = casting_director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['deleted'], '1')

    def test_error_404_delete_actor(self):
        """Test DELETE non existing actor"""
        res = self.client().delete('/actors/12345', headers = casting_director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'] , 'Actor with id 12345 does not exist.')

#----------------------------------------------------------------------------#
# Tests for /movies POST
#----------------------------------------------------------------------------#

    def test_create_new_movie(self):
        """Test POST new movie."""

        json_create_movie = {
            'title' : 'Notebook',
            'release_date' : date.today()
        } 

        res = self.client().post('/movies', json = json_create_movie, headers = executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['created'], 2)

    def test_error_422_create_new_movie(self):
        """Test Error POST new movie."""

        json_create_movie_without_name = {
            'release_date' : date.today()
        } 

        res = self.client().post('/movies', json = json_create_movie_without_name, headers = executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'No title provided, the title is required.')

#----------------------------------------------------------------------------#
# Tests for /movies GET
#----------------------------------------------------------------------------#

    def test_get_all_movies(self):
        """Test GET all movies."""
        res = self.client().get('/movies?page=1', headers = casting_assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['movies']) > 0)

    def test_error_401_get_all_movies(self):
        """Test GET all movies w/o Authorization."""
        res = self.client().get('/movies?page=1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Authorization header is expected.')

    def test_error_404_get_movies(self):
        """Test Error GET all movies."""
        res = self.client().get('/movies?page=123456', headers = casting_assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'] , 'No movies found.')

#----------------------------------------------------------------------------#
# Tests for /movies PATCH
#----------------------------------------------------------------------------#

    def test_edit_movie(self):
        """Test PATCH existing movies"""
        json_edit_movie = {
            'release_date' : date.today()
        } 
        res = self.client().patch('/movies/1', json = json_edit_movie, headers = executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['movie']) > 0)

    def test_error_400_edit_movie(self):
        """Test PATCH with non valid id json body"""
        res = self.client().patch('/movies/1', headers = executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'] , 'Request does not contain a valid JSON body.')

    def test_error_404_edit_movie(self):
        """Test PATCH with non valid id"""
        json_edit_movie = {
            'release_date' : date.today()
        } 
        res = self.client().patch('/movies/12345', json = json_edit_movie, headers = executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'] , 'Movie with id 12345 does not exist.')

#----------------------------------------------------------------------------#
# Tests for /movies DELETE
#----------------------------------------------------------------------------#

    def test_error_401_delete_movie(self):
        """Test DELETE existing movie w/o Authorization"""
        res = self.client().delete('/movies/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Authorization header is expected.')

    def test_error_403_delete_movie(self):
        """Test DELETE existing movie with wrong permissions"""
        res = self.client().delete('/movies/1', headers = casting_assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Permission not found.')

    def test_delete_movie(self):
        """Test DELETE existing movie"""
        res = self.client().delete('/movies/1', headers = executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['deleted'], '1')

    def test_error_404_delete_movie(self):
        """Test DELETE non existing movie"""
        res = self.client().delete('/movies/123456', headers = executive_producer_auth_header) 
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'] , 'Movie with id 123456 does not exist.')

# Make the tests conveniently executable.
# From app directory, run 'python test_app.py' to start tests
if __name__ == "__main__":
    unittest.main()