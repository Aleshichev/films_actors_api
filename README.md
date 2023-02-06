# Films_actors Flask Restful Api 
**(Sqlalchemy, SQLite, flask, pipenv, pytest, flask_migrate, jwt authentication 
, Marshmallow, Swagger, Docker)**
### This is a simple application can insert/select/update/delete data in the database using sqlalchemy and flask rest framework.
### Docker https://hub.docker.com/r/aleshichev/films_api

## Database has 4 tables:

- **Actors**
- **Films**
- **Movies-actors**
- **Users**

## Swagger:
- **/swagger** - users can interactively view the project documentation.

## The application accepts the following requests:

- **/register** - To register a new user you need to enter your username and password and get a token, then create a new user with json data.

- **/login** - Enter your login to sign in (igor 123).

- **/films** - list of all films.

-**/films/uuid** -  **GET** method has an optional parameter "uuid", it returns films equal to parameter's value. In the **POST** method and **DELETE** method you can add new film or remove existing film. In the **PUT** and **PATCH** methods you can change an existing film.

- **/actors** - list of all actors.

- **/actors/id** - **GET** method has an optional parameter "id", it returns actor who has this parameter's value . In the **POST** method and **DELETE** method you can add new actor or remove existing actor. In the **PUT** and **PATCH** methods you can change an existing actor.

- **/aggregations** - this page shows: films_count, 'max': max_rating, 'min': min_rating, 'avg': avg_rating, 'sum': sum_rating

- **/smoke** - api test  page

## Pytests :
- **test_actors.py** - checks response api.
- **test_films.py** - checks feeresponse api.
- **test_smoke.py** - checks response api.
