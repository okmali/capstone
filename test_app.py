import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Artist, Movie
from dotenv import load_dotenv

load_dotenv()

dbUser = os.getenv("DB_USER")
dbPwd = os.getenv("DB_PWD")
dbName = os.getenv("DB_NAME")
dbHost = os.getenv("DB_HOST")


class CapstoneTestCase(unittest.TestCase):
    """This class represents the capstone test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            dbUser, dbPwd, dbHost, dbName)
        setup_db(self.app, self.database_path)

        self.new_artist = {
            "name": "Test Artist",
            "age": 50,
            "gender": "female"
        }

        self.new_movie = {
            "title": "Test Movie",
            "release_date": "1980-05-01 00:00:00",
            "genre_id": 3,
            "artists": [
                {"id": 4},
                {"id": 6},
                {"id": 7}
            ]
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    '''
    @TODO:Write at least one test for each test
    for successful operation and for expected errors.
    '''

    '''Hello Test'''

    def test_hello(self):
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)

    # Get Movies Positive Test

    def test_getMovies_positive(self):
        res = self.client().get('/movies', headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IndpQ3FoRjMtcGw0MWo0Qmx1M0lXRiJ9.eyJpc3MiOiJodHRwczovL2FwaXNlcnZlci1va21hbGktZGV2LmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExNjU4Mzk5MTc4NTUxMjYxOTQxMyIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNjQ1ODY5MzI3LCJleHAiOjE2NDU5NTU3MjcsImF6cCI6InR3c1JPNTRvTmZodkN0WmxTZTJEeUZ5QWg0bzhUYmcxIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YXJ0aXN0cyIsImRlbGV0ZTpnZW5yZXMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFydGlzdHMiLCJnZXQ6Z2VucmVzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFydGlzdHMiLCJwYXRjaDpnZW5yZXMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFydGlzdHMiLCJwb3N0OmdlbnJlcyIsInBvc3Q6bW92aWVzIl19.dTl6g8GlZtcNHRqxo14TIvAMvg8BSJRN4E5EjmUIlv3z7mfzosRLUJMwzD-awKGXrTZjRYv0LVUO2gZ0swC7gX8aloWBfT00Twl6YLZO1NjHVDnaGGJGe77BpdKmeCiqH8Q_f9zUTmDj6BJ7OMYqLxsJ2E65Mt0QFjRNmt7XWJTSyjA7_QmafH8nzupN_YbYBHsQ4ZERcE1KzOR_BwVkFX0hiIXZgera1qfuYvZ9QweAv-IXzFm4pmFAmbV8h1wzMhqYGECDNgmN0NQOvSOhW1prHKXQq0Ww-Jss97xlDGt3vArVxt6MSjSNX8T-rum1GbPTbtjPOx35UJHC8l8j1Q'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    # Get Movie Negative Test

    def test_getMovie_negative(self):
        res = self.client().get('/movies/1000', headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IndpQ3FoRjMtcGw0MWo0Qmx1M0lXRiJ9.eyJpc3MiOiJodHRwczovL2FwaXNlcnZlci1va21hbGktZGV2LmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExNjU4Mzk5MTc4NTUxMjYxOTQxMyIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNjQ1ODY5MzI3LCJleHAiOjE2NDU5NTU3MjcsImF6cCI6InR3c1JPNTRvTmZodkN0WmxTZTJEeUZ5QWg0bzhUYmcxIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YXJ0aXN0cyIsImRlbGV0ZTpnZW5yZXMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFydGlzdHMiLCJnZXQ6Z2VucmVzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFydGlzdHMiLCJwYXRjaDpnZW5yZXMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFydGlzdHMiLCJwb3N0OmdlbnJlcyIsInBvc3Q6bW92aWVzIl19.dTl6g8GlZtcNHRqxo14TIvAMvg8BSJRN4E5EjmUIlv3z7mfzosRLUJMwzD-awKGXrTZjRYv0LVUO2gZ0swC7gX8aloWBfT00Twl6YLZO1NjHVDnaGGJGe77BpdKmeCiqH8Q_f9zUTmDj6BJ7OMYqLxsJ2E65Mt0QFjRNmt7XWJTSyjA7_QmafH8nzupN_YbYBHsQ4ZERcE1KzOR_BwVkFX0hiIXZgera1qfuYvZ9QweAv-IXzFm4pmFAmbV8h1wzMhqYGECDNgmN0NQOvSOhW1prHKXQq0Ww-Jss97xlDGt3vArVxt6MSjSNX8T-rum1GbPTbtjPOx35UJHC8l8j1Q'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    # Delete Movie Positive Test

    def test_deleteMovie_positive(self):
        res = self.client().delete('/movies/23', headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IndpQ3FoRjMtcGw0MWo0Qmx1M0lXRiJ9.eyJpc3MiOiJodHRwczovL2FwaXNlcnZlci1va21hbGktZGV2LmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExNjU4Mzk5MTc4NTUxMjYxOTQxMyIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNjQ1ODY5MzI3LCJleHAiOjE2NDU5NTU3MjcsImF6cCI6InR3c1JPNTRvTmZodkN0WmxTZTJEeUZ5QWg0bzhUYmcxIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YXJ0aXN0cyIsImRlbGV0ZTpnZW5yZXMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFydGlzdHMiLCJnZXQ6Z2VucmVzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFydGlzdHMiLCJwYXRjaDpnZW5yZXMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFydGlzdHMiLCJwb3N0OmdlbnJlcyIsInBvc3Q6bW92aWVzIl19.dTl6g8GlZtcNHRqxo14TIvAMvg8BSJRN4E5EjmUIlv3z7mfzosRLUJMwzD-awKGXrTZjRYv0LVUO2gZ0swC7gX8aloWBfT00Twl6YLZO1NjHVDnaGGJGe77BpdKmeCiqH8Q_f9zUTmDj6BJ7OMYqLxsJ2E65Mt0QFjRNmt7XWJTSyjA7_QmafH8nzupN_YbYBHsQ4ZERcE1KzOR_BwVkFX0hiIXZgera1qfuYvZ9QweAv-IXzFm4pmFAmbV8h1wzMhqYGECDNgmN0NQOvSOhW1prHKXQq0Ww-Jss97xlDGt3vArVxt6MSjSNX8T-rum1GbPTbtjPOx35UJHC8l8j1Q'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    # Delete Movie Negative Test

    def test_deleteMovie_negative(self):
        res = self.client().delete('/movies/1000', headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IndpQ3FoRjMtcGw0MWo0Qmx1M0lXRiJ9.eyJpc3MiOiJodHRwczovL2FwaXNlcnZlci1va21hbGktZGV2LmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExNjU4Mzk5MTc4NTUxMjYxOTQxMyIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNjQ1ODY5MzI3LCJleHAiOjE2NDU5NTU3MjcsImF6cCI6InR3c1JPNTRvTmZodkN0WmxTZTJEeUZ5QWg0bzhUYmcxIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YXJ0aXN0cyIsImRlbGV0ZTpnZW5yZXMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFydGlzdHMiLCJnZXQ6Z2VucmVzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFydGlzdHMiLCJwYXRjaDpnZW5yZXMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFydGlzdHMiLCJwb3N0OmdlbnJlcyIsInBvc3Q6bW92aWVzIl19.dTl6g8GlZtcNHRqxo14TIvAMvg8BSJRN4E5EjmUIlv3z7mfzosRLUJMwzD-awKGXrTZjRYv0LVUO2gZ0swC7gX8aloWBfT00Twl6YLZO1NjHVDnaGGJGe77BpdKmeCiqH8Q_f9zUTmDj6BJ7OMYqLxsJ2E65Mt0QFjRNmt7XWJTSyjA7_QmafH8nzupN_YbYBHsQ4ZERcE1KzOR_BwVkFX0hiIXZgera1qfuYvZ9QweAv-IXzFm4pmFAmbV8h1wzMhqYGECDNgmN0NQOvSOhW1prHKXQq0Ww-Jss97xlDGt3vArVxt6MSjSNX8T-rum1GbPTbtjPOx35UJHC8l8j1Q'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    # Create a new Movie positive Test

    def test_createMovie_positive(self):
        res = self.client().post('/movies', headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IndpQ3FoRjMtcGw0MWo0Qmx1M0lXRiJ9.eyJpc3MiOiJodHRwczovL2FwaXNlcnZlci1va21hbGktZGV2LmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExNjU4Mzk5MTc4NTUxMjYxOTQxMyIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNjQ1ODY5MzI3LCJleHAiOjE2NDU5NTU3MjcsImF6cCI6InR3c1JPNTRvTmZodkN0WmxTZTJEeUZ5QWg0bzhUYmcxIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YXJ0aXN0cyIsImRlbGV0ZTpnZW5yZXMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFydGlzdHMiLCJnZXQ6Z2VucmVzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFydGlzdHMiLCJwYXRjaDpnZW5yZXMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFydGlzdHMiLCJwb3N0OmdlbnJlcyIsInBvc3Q6bW92aWVzIl19.dTl6g8GlZtcNHRqxo14TIvAMvg8BSJRN4E5EjmUIlv3z7mfzosRLUJMwzD-awKGXrTZjRYv0LVUO2gZ0swC7gX8aloWBfT00Twl6YLZO1NjHVDnaGGJGe77BpdKmeCiqH8Q_f9zUTmDj6BJ7OMYqLxsJ2E65Mt0QFjRNmt7XWJTSyjA7_QmafH8nzupN_YbYBHsQ4ZERcE1KzOR_BwVkFX0hiIXZgera1qfuYvZ9QweAv-IXzFm4pmFAmbV8h1wzMhqYGECDNgmN0NQOvSOhW1prHKXQq0Ww-Jss97xlDGt3vArVxt6MSjSNX8T-rum1GbPTbtjPOx35UJHC8l8j1Q'}, json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    # Get Artists Positive Test

    def test_getArtists_positive(self):
        res = self.client().get('/artists', headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IndpQ3FoRjMtcGw0MWo0Qmx1M0lXRiJ9.eyJpc3MiOiJodHRwczovL2FwaXNlcnZlci1va21hbGktZGV2LmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExNjU4Mzk5MTc4NTUxMjYxOTQxMyIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNjQ1ODY5MzI3LCJleHAiOjE2NDU5NTU3MjcsImF6cCI6InR3c1JPNTRvTmZodkN0WmxTZTJEeUZ5QWg0bzhUYmcxIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YXJ0aXN0cyIsImRlbGV0ZTpnZW5yZXMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFydGlzdHMiLCJnZXQ6Z2VucmVzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFydGlzdHMiLCJwYXRjaDpnZW5yZXMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFydGlzdHMiLCJwb3N0OmdlbnJlcyIsInBvc3Q6bW92aWVzIl19.dTl6g8GlZtcNHRqxo14TIvAMvg8BSJRN4E5EjmUIlv3z7mfzosRLUJMwzD-awKGXrTZjRYv0LVUO2gZ0swC7gX8aloWBfT00Twl6YLZO1NjHVDnaGGJGe77BpdKmeCiqH8Q_f9zUTmDj6BJ7OMYqLxsJ2E65Mt0QFjRNmt7XWJTSyjA7_QmafH8nzupN_YbYBHsQ4ZERcE1KzOR_BwVkFX0hiIXZgera1qfuYvZ9QweAv-IXzFm4pmFAmbV8h1wzMhqYGECDNgmN0NQOvSOhW1prHKXQq0Ww-Jss97xlDGt3vArVxt6MSjSNX8T-rum1GbPTbtjPOx35UJHC8l8j1Q'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['artists'])

    # Get Artist Negative Test

    def test_getArtists_negative(self):
        res = self.client().get('/artists/1000', headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IndpQ3FoRjMtcGw0MWo0Qmx1M0lXRiJ9.eyJpc3MiOiJodHRwczovL2FwaXNlcnZlci1va21hbGktZGV2LmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExNjU4Mzk5MTc4NTUxMjYxOTQxMyIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNjQ1ODY5MzI3LCJleHAiOjE2NDU5NTU3MjcsImF6cCI6InR3c1JPNTRvTmZodkN0WmxTZTJEeUZ5QWg0bzhUYmcxIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YXJ0aXN0cyIsImRlbGV0ZTpnZW5yZXMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFydGlzdHMiLCJnZXQ6Z2VucmVzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFydGlzdHMiLCJwYXRjaDpnZW5yZXMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFydGlzdHMiLCJwb3N0OmdlbnJlcyIsInBvc3Q6bW92aWVzIl19.dTl6g8GlZtcNHRqxo14TIvAMvg8BSJRN4E5EjmUIlv3z7mfzosRLUJMwzD-awKGXrTZjRYv0LVUO2gZ0swC7gX8aloWBfT00Twl6YLZO1NjHVDnaGGJGe77BpdKmeCiqH8Q_f9zUTmDj6BJ7OMYqLxsJ2E65Mt0QFjRNmt7XWJTSyjA7_QmafH8nzupN_YbYBHsQ4ZERcE1KzOR_BwVkFX0hiIXZgera1qfuYvZ9QweAv-IXzFm4pmFAmbV8h1wzMhqYGECDNgmN0NQOvSOhW1prHKXQq0Ww-Jss97xlDGt3vArVxt6MSjSNX8T-rum1GbPTbtjPOx35UJHC8l8j1Q'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
