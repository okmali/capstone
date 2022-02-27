# Capstone - Full Stack API 

This project is a final capstone project. Project models a Casting Agency company that is responsible for creating movies and managing and assigning actors to those movies. There are following roles modeled:
1-Casting Assistant:*Can view actors and movies, 
2-Casting Director: *All permissions a Casting Assistant has and… *Add or delete an actor from the database
Modify actors or movies
3-Executive Producer:*All permissions a Casting Director has and… *Add or delete a movie from the database

### Installing Dependencies 
Developers using this project should already have Python3 and pip installed on their local machines.

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Environment** - It is recommended working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by navigating to the `/backend` directory and running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


4. **Key Dependencies**
 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

### Database Setup
With Postgres running, create an empty postgres db. ".env" file contains necessary environment variables to connect to this db. You should update them properly. Once the app is running it will create the data model itsel within this db

### Running the backend server

From within the `.` directory first ensure you are working using your created virtual environment.

To run the application run the following commands: 
```
python app.py
```

The application is run on `http://127.0.0.1:5000/` by default and is a proxy in the frontend configuration. 


### Tests
In order to run tests : 

```
python test_app.py
```

Before running the tests make sure the "capstone" database is already created as it is described in "running the backend server" section. 

All tests are kept in that file and should be maintained as updates are made to app functionality.

To run the tests successfully correct Authorization Token should be provided within test cases as shown below

"res = self.client().get('/artists',headers={'Authorization':'Bearer MySecretToken'})"

### Getting Started
- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration. 
- Authentication: This version of the application support Auth0 and require authentication Token as API keys. 

### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 404,
    "message": "Resource Not Found"
}
```
The API will return following error types when requests fail:
- 400: Bad Request
- 404: Resource Not Found
- 405: Method Not Allowed 
- 422: Not Processable 
- 500: Internal Server Error 

### Endpoints 
As stated in Tests section to call the endpoints Authorization token should be provided in the header. If it is missing or wrong key provided you will get the following response:
'''
{
    "error": 401,
    "message": "Unauthorized",
    "success": false
}
'''
#### GET
##### /movies
- General:
    - Returns a list of movies, categories, success value, and total number of questions
    - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1. 
- Sample: `curl http://127.0.0.1:5000/movies`
'''
{
    "movies": [
        {
            "genre_id": 1,
            "id": 2,
            "release_date": "Mon, 31 Jan 2022 21:00:00 GMT",
            "title": "red notice"
        },
        {
            "genre_id": 3,
            "id": 3,
            "release_date": "Sun, 31 Jan 2021 21:00:00 GMT",
            "title": "Irish Man"
        },
        {
            "genre_id": 3,
            "id": 31,
            "release_date": "Wed, 30 Apr 1980 21:00:00 GMT",
            "title": "Test Movie"
        }
    ],
    "success": true
}
'''

##### /movies/<movie_id>
- General:
    - Returns a specific movie, along with the starring artists
- Sample: `curl http://127.0.0.1:5000/movies/15`
'''
{
    "movieDetails": {
        "artistList": [
            "Angelina Jolie",
            "Tom Cruise",
            "Brad Pitt"
        ],
        "movie": {
            "genre_id": 3,
            "id": 15,
            "release_date": "Wed, 31 Oct 1990 21:00:00 GMT",
            "title": "Taxi Driver"
        }
    },
    "success": true
}
'''

##### /artists
- General:
    - Returns a list of artists 
- Sample: `curl http://127.0.0.1:5000/artists`
'''
{
    "artists": [
        {
            "age": 55,
            "gender": "Female",
            "id": 2,
            "name": "Angelina Jolie"
        },
        {
            "age": 50,
            "gender": "female",
            "id": 20,
            "name": "Test Artist"
        }
    ],
    "success": true
}
'''
##### /artists/<artist_id>
- General:
    - Returns a list of artists along with the movies in which starred
- Sample: `curl http://127.0.0.1:5000/artists/10`
'''
{
    "artistDetails": {
        "artist": {
            "age": 60,
            "gender": "male",
            "id": 4,
            "name": "Brad Pitt"
        },
        "movieList": [
            "Taxi Driver",
            "Platoon",
            "Event Horizon"
        ]
    },
    "success": true
}
'''
##### /genres
- General:
    - Returns a list of movie genres
- Sample: `curl http://127.0.0.1:5000/genres`
'''
{
    "genres": [
        {
            "genre": "Horror",
            "id": 1
        },
        {
            "genre": "Science Fiction",
            "id": 2
        },
        {
            "genre": "Drama",
            "id": 3
        },
        {
            "genre": "Comedy",
            "id": 4
        },
        {
            "genre": "Action",
            "id": 5
        },
        {
            "genre": "Documentery",
            "id": 6
        }
    ],
    "success": true
}
'''

#### DELETE
##### /movies/<movie_id>
- General:
    - Deletes the movie of given id if it exists. Returns success value 
- Sample: `curl -X DELETE http://127.0.0.1:5000/movies/23`
'''
{
    "movie": {
        "genre_id": 3,
        "id": 31,
        "release_date": "Wed, 30 Apr 1980 21:00:00 GMT",
        "title": "Test Movie"
    },
    "success": true
}
'''
##### /artists/<artist_id>
- General:
    - Deletes the artist of given id if it exists. Returns success value 
- Sample: `curl -X DELETE http://127.0.0.1:5000/artists/23`
'''
{
    "artist": {
        "age": 50,
        "gender": "female",
        "id": 20,
        "name": "Test Artist"
    },
    "success": true
}
'''
##### /genres/<genre_id>
- General:
    - Deletes the genre of given id if it exists. Returns success value 
- Sample: `curl -X DELETE http://127.0.0.1:5000/genres/14`
'''
{
    "genre": {
        "genre": "to delete",
        "id": 14
    },
    "success": true
}
'''
#### POST
##### /artists
- General:
    - Creates a new artist. Returns the the created artist and success value. 
- `curl http://127.0.0.1:5000/artists -X POST -H "Content-Type: application/json" -d ' 
    {
    "name": "Test Artist",
    "age": 50,
    "gender": "female"
    }'`
'''
{
    "artist": {
        "age": 50,
        "gender": "female",
        "id": 21,
        "name": "Test Artist"
    },
    "success": true
}
'''
##### /movies
- General:
    - Creates a new movie. ID of artists provided should already had been created. Returns the the created movie and success value. 
- `curl http://127.0.0.1:5000/movies -X POST -H "Content-Type: application/json" -d ' 
    {
    "title": "Test Movie",
    "release_date": "1980-05-01 00:00:00",
    "genre_id": 3,
    "artists":[
        {"id" :4},
        {"id" :6},
        {"id" :7}
    ]}'`
'''
{
    "movie": {
        "genre_id": 3,
        "id": 32,
        "release_date": "Wed, 30 Apr 1980 21:00:00 GMT",
        "title": "Test Movie"
    },
    "success": true
}
'''
##### /genres
- General:
    - Creates a new genre.  Returns the the created movie and success value. 
- `curl http://127.0.0.1:5000/genres -X POST -H "Content-Type: application/json" -d ' 
    {
    "genre": "to delete"}'`
'''
{
    "genre": {
        "genre": "to delete",
        "id": 15
    },
    "success": true
}
'''
#### PATCH
##### /artists/
- General:
    - Updates an artist. Returns the updated artist and success value. 
- `curl http://127.0.0.1:5000/artists/6 -X PATCH -H "Content-Type: application/json" -d ' 
    {
    "age": 58,
    "gender": "male"}'`
'''
{
    "artist": {
        "age": 58,
        "gender": "male",
        "id": 6,
        "name": "Mick Jagger"
    },
    "success": true
}
'''
##### /movies/
- General:
    - Updates an movie. Returns the updated movie and success value. 
- `curl http://127.0.0.1:5000/movies/30 -X PATCH -H "Content-Type: application/json" -d ' 
    {
    "title": "Test Movie 2",
    "release_date": "1980-05-01 00:00:00",
    "genre_id": 4}'`
'''
{
    "artist": {
        "genre_id": 4,
        "id": 30,
        "release_date": "Wed, 30 Apr 1980 21:00:00 GMT",
        "title": "Test Movie 2"
    },
    "success": true
}
'''
## Deployment 
- Project is up and running in Heroku environemt. You can find the environment details within HerokuEnv.json file. This file also contains valid tokens which belong to executive, asistant and director roles. 

- postman_collection.json contains requests and tests to test project endpoints

## Authors
Mehmet Ali OK & Udacity Team 

## Acknowledgements 
The awesome team at Udacity! 