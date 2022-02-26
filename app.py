import os
import sys
from re import match
from datetime import datetime
from flask import Flask, abort, jsonify, request
from models import Genres, MatchTable, setup_db, Artist, Movie, db
from flask_cors import CORS
from auth import AuthError, requires_auth


def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    # CORS(app)
    CORS(app, resources={r"/*": {"origins": "*"}})

    @app.route('/')
    def get_greeting():
        #excited = os.environ['EXCITED']
        greeting = "Hello"
        # if excited == 'true':
        greeting = greeting + "!!!!! You are doing great in this Udacity project."
        return jsonify({'message': greeting}), 200

    @app.route('/coolkids')
    def be_cool():
        return jsonify({'message': "Be cool, man, be coooool! You're almost a FSND grad!"}), 200

# Artist Endpoints - start
    @app.route('/artists', methods=['GET'])
    @requires_auth('get:artists')
    def get_artists(jwt):
        artists = db.session.query(Artist).all()
        formatted_artists = [artist.format() for artist in artists]

        if len(formatted_artists) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'artists': formatted_artists,
        }), 200

    @app.route('/artists/<int:artist_id>', methods=['GET'])
    @requires_auth('get:artists')
    def get_one_artist(jwt, artist_id):

        artist = db.session.query(Artist).filter(
            Artist.id == artist_id).one_or_none()
        searchList = db.session.query(Movie, MatchTable).join(
            MatchTable).filter(MatchTable.artist_id == artist_id).all()
        #movieList=[searchItem[0].title for searchItem in searchList]
        movieList = [searchItem[0].title for searchItem in searchList]

        if artist is None:
            abort(404)

        return jsonify({
            'success': True,
            'artistDetails': {
                'artist': artist.format(),
                'movieList': movieList,
            },
        }), 200

    @app.route('/artists/<int:artist_id>', methods=['DELETE'])
    @requires_auth('delete:artists')
    def delete_artist(jwt, artist_id):

        artist = db.session.query(Artist).filter(
            Artist.id == artist_id).one_or_none()

        if artist is None:
            abort(404)
        else:
            try:
                artist.delete()
            except:
                abort(500)

        return jsonify({
            'success': True,
            'artist': artist.format()
        }), 200

    @app.route('/artists', methods=['POST'])
    @requires_auth('post:artists')
    def create_artist(jwt):

        newArtistReq = request.get_json()

        name = newArtistReq['name']
        age = int(newArtistReq['age'])
        gender = newArtistReq['gender']

        newArtist = Artist(
            name=name,
            age=age,
            gender=gender)

        try:
            newArtist.insert()
        except:
            print(sys.exc_info())
            abort(422)

        return jsonify({
            'success': True,
            'artist': newArtist.format()
        }), 200

    @app.route('/artists/<int:artist_id>', methods=['PATCH'])
    @requires_auth('patch:artists')
    def update_artist(jwt, artist_id):

        updateArtistReq = request.get_json()
        artist = db.session.query(Artist).filter(
            Artist.id == artist_id).one_or_none()

        if artist is None:
            abort(404)
        else:
            try:
                #name = updateArtistReq['name']
                age = int(updateArtistReq['age'])
                gender = updateArtistReq['gender']
                artist.age = age
                artist.gender = gender
                artist.update()
            except:
                abort(500)

        return jsonify({
            'success': True,
            'artist': artist.format()
        }), 200
# Artist Endpoints - End

# Movie Endpoints - Start
    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(jwt):
        movies = db.session.query(Movie).all()
        formatted_movies = [movie.format() for movie in movies]

        if len(formatted_movies) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'movies': formatted_movies,
        }), 200

    @app.route('/movies/<int:movie_id>', methods=['GET'])
    @requires_auth('get:movies')
    def get_one_movie(jwt, movie_id):

        movie = db.session.query(Movie).filter(
            Movie.id == movie_id).one_or_none()
        searchList = db.session.query(Artist, MatchTable).join(
            MatchTable).filter(MatchTable.movie_id == movie_id).all()

        artistList = [searchItem[0].name for searchItem in searchList]

        if movie is None:
            abort(404)

        return jsonify({
            'success': True,
            'movieDetails': {
                'movie': movie.format(),
                'artistList': artistList,
            },
        }), 200

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(jwt, movie_id):

        movie = db.session.query(Movie).filter(
            Movie.id == movie_id).one_or_none()
        matchTable = db.session.query(MatchTable).filter(
            MatchTable.movie_id == movie_id).all()

        if movie is None:
            abort(404)
        else:
            try:
                if len(matchTable) > 0:
                    for match in matchTable:
                        match.delete()
                movie.delete()
                db.session.commit()
            except:
                print(sys.exc_info())
                db.session.rollback()
                abort(500)

        return jsonify({
            'success': True,
            'movie': movie.format()
        }), 200

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie(jwt):

        newMovieReq = request.get_json()

        title = newMovieReq['title']
        release_date = datetime.strptime(
            newMovieReq['release_date'], ("%Y-%m-%d %H:%M:%S"))
        genre_id = newMovieReq['genre_id']
        artists = newMovieReq['artists']

        newMovie = Movie(
            title=title,
            release_date=release_date,
            genre_id=genre_id)

        try:
            newMovie.insert()
            movie_id = newMovie.id

            for artist in artists:
                artist_id = artist['id']
                newMatchTable = MatchTable(
                    artist_id=artist_id,
                    movie_id=movie_id
                )
                newMatchTable.insert()
            db.session.commit()
        except:
            print(sys.exc_info())
            db.session.rollback()
            abort(422)

        return jsonify({
            'success': True,
            'movie': newMovie.format()
        }), 200

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(jwt, movie_id):

        updateMovieReq = request.get_json()
        movie = db.session.query(Movie).filter(
            Movie.id == movie_id).one_or_none()

        if movie is None:
            abort(404)
        else:
            try:
                #name = updateArtistReq['name']
                title = updateMovieReq['title']
                genre_id = updateMovieReq['genre_id']
                release_date = datetime.strptime(
                    updateMovieReq['release_date'], ("%Y-%m-%d %H:%M:%S"))
                movie.title = title
                movie.genre_id = genre_id
                movie.release_date = release_date
                movie.update()
            except:
                abort(500)

        return jsonify({
            'success': True,
            'artist': movie.format()
        }), 200
# Movie Endpoints - End

# Genres Endpoints - Start
    @app.route('/genres', methods=['GET'])
    @requires_auth('get:genres')
    def get_genres(jwt):
        genres = db.session.query(Genres).all()
        formatted_genres = [genre.format() for genre in genres]

        if len(formatted_genres) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'genres': formatted_genres,
        }), 200

    @app.route('/genres/<int:genre_id>', methods=['DELETE'])
    @requires_auth('delete:genres')
    def delete_genre(jwt, genre_id):

        genre = db.session.query(Genres).filter(
            Genres.id == genre_id).one_or_none()

        if genre is None:
            abort(404)
        else:
            try:
                genre.delete()
            except:
                abort(500)

        return jsonify({
            'success': True,
            'genre': genre.format()
        }), 200

    @app.route('/genres', methods=['POST'])
    @requires_auth('post:genres')
    def create_genre(jwt):

        newGenreReq = request.get_json()

        genre = newGenreReq['genre']

        newGenre = Genres(
            genre=genre)

        try:
            newGenre.insert()
        except:
            print(sys.exc_info())
            abort(422)

        return jsonify({
            'success': True,
            'genre': newGenre.format()
        }), 200


# Genres Endpoints - End

    # Error Handlers - Start


    @app.errorhandler(422)
    def unprocessable_error(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    '''
    @TODO implement error handlers using the @app.errorhandler(error) decorator
        each error handler should return (with approprate messages):
                jsonify({
                        "success": False,
                        "error": 404,
                        "message": "resource not found"
                        }), 404

    '''

    '''
    @TODO implement error handler for 404
        error handler should conform to general task above
    '''

    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Resource Not Found'

        }), 404

    '''
    @TODO implement error handler for AuthError
        error handler should conform to general task above
    '''

    @app.errorhandler(AuthError)
    def not_found_error(error):
        return jsonify(error.error), error.status_code

    @app.errorhandler(401)
    def unauthorized_error(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': 'Unauthorized'
        }), 401

    @app.errorhandler(403)
    def forbidden_error(error):
        return jsonify({
            'success': False,
            'error': 403,
            'message': 'Forbidden'
        }), 403

    @app.errorhandler(400)
    def badrequest_error(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Bad Request'
        }), 400

# Error Handlers - End

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
