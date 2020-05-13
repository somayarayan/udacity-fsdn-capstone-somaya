# FSND: Capstone Project

## Content

1. [Project Motivation and Background](#background)
2. [Start Project locally](#start-locally)
3. [API Documentation](#api)
4. [Authentication](#authentication)

<a name="background"></a>
## Project Motivation and Background

Learning by doing can be hard, but it’s ultimately very beneficial and it's really exciting to finally reach this stage and work on the final project of the `Udacity Full Stack Nanodegree` program to apply and link all the topics and modules that are part of the progrem together in one single project.

The project idea is basically a Casting Agency that models a company which is responsible for creating movies and managing and assigning actors to those movies. 

This project covers the following technical topics in 1 application:

1. Database modeling with `postgres` & `sqlalchemy` (see `models.py`)
2. API to performance CRUD Operations on database with `Flask` (see `app.py`)
3. Automated testing with `Unittest` (see `test_app`)
4. Authorization & Role based Authentication with `Auth0` (see `auth.py`)
5. Deployment on `Heroku`

<a name="start-locally"></a>
## Start Project locally

Make sure you `cd` into the correct folder (with all app files) before following the setup steps.
Also, you need the latest version of [Python 3](https://www.python.org/downloads/)
and [postgres](https://www.postgresql.org/download/) installed on your machine.

To start and run the local development server,

1. Initialize and activate a virtualenv:
  ```bash
  $ virtualenv --no-site-packages env_capstone
  $ source env_capstone/scripts/activate
  ```

2. Install the dependencies:
```bash
$ pip install -r requirements.txt
```

Running this project locally means that it can´t access `Heroku` env variables.
To fix this, you need to edit a few configurations in `config.py`, so it can
correctly connect to a local database

3. Change database config so it can connect to your local postgres database
- Open `config.py` with your editor of choice. 
- Here you can see this configuration:
 ```python
database_setup = {
    "database_name" : "casting",
    "user_name" : "postgres", # default postgres user name
    "password" : "****************", # if applicable. If no password, just type in None
    "port" : "localhost:5432" # default postgres port
}
```

 - Just change `user_name`, `password` and `port` to whatever you choose while installing postgres.
>_tip_: `user_name` usually defaults to `postgres` and `port` always defaults to `localhost:5432` while installing postgres, most of the time you just need to change the `password`.

4. Setup Auth0
If you only want to test the API (i.e. Project Reviewer), you can
simply take the existing bearer tokens in `config.py`.

If you already know your way around `Auth0`, just insert your data 
into `config.py` => auth0_config.

Here are the steps to enable the [authentication](#authentication).

5. Run the development server:
  ```bash 
  $ python app.py
  ```

6. (optional) To execute tests, run
```bash 
$ python test_app.py
```
If you choose to run all tests, it should give this response if everything went fine:

```bash
$ python test_app.py
.........................
----------------------------------------------------------------------
Ran 25 tests in 77.708s

OK

```
## API Documentation
<a name="api"></a>

Here you can find all existing endpoints, which methods can be used, how to work with them and example responses you will get.

Additionally, common issues and error messages are explained, if applicable.

### Base URL

**_https://udacity-fsdn-capstone-somaya.herokuapp.com_**

### Authentication

Please see [API Authentication](#Authentication-bearer)

### Available Endpoints

This is a table about which resources exist and which methods you can use on them.

                          Allowed Methods
       Endpoints    |  GET |  POST |  DELETE | PATCH  |
                    |------|-------|---------|--------|
      /actors       |  [x] |  [x]  |   [x]   |   [x]  |   
      /movies       |  [x] |  [x]  |   [x]   |   [x]  |   

### How to work with each endpoint

Click on a link to directly get to the resource.

1. Actors
   1. [GET /actors](#get-actors)
   2. [POST /actors](#post-actors)
   3. [DELETE /actors](#delete-actors)
   4. [PATCH /actors](#patch-actors)
2. Movies
   1. [GET /movies](#get-movies)
   2. [POST /movies](#post-movies)
   3. [DELETE /movies](#delete-movies)
   4. [PATCH /movies](#patch-movies)

Each resource documentation is clearly structured:
1. Description in a few words
2. `curl` example that can directly be used in terminal
3. More descriptive explanation of inputs and outputs.
4. Required permissions
5. Example Request
7. Example Response.
8. Error Handling (`curl` command to trigger error + error response)

# <a name="get-actors"></a>
### 1. GET /actors

Query paginated actors.

```bash
$ curl -X GET https://udacity-fsdn-capstone-somaya.herokuapp.com/actors?page=1
```
- This API fetches the list of actors
- Request Arguments: 
  1. **integer** `page` (optional, 10 actors per page, defaults to `1` if not given)
- Request Headers: 
  1. **JWT Bearer Token** `Authorization` (<span style="color:red">*</span>required)
- Requires permission: `GET:actors`
- Returns: 
  1. List of actors with following fields:
      - **integer** `id`
      - **string** `name`
      - **string** `gender`
      - **integer** `age`
  2. **boolean** `success`

#### Example Request
```
curl --location --request GET 'https://udacity-fsdn-capstone-somaya.herokuapp.com/actors' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJERTFSVGM0TVRrek9VWTJOalJGTVRoR016RTRRamRGUWpKRFJUaEJRa0l3UVRZeU1qTkNOQSJ9.eyJpc3MiOiJodHRwczovL2ZzbmRzLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWFlZDVlMGVhZjg1MTBiZTdlYTQ2M2UiLCJhdWQiOiJDYXN0aW5nIiwiaWF0IjoxNTg4NTE3MDk0LCJleHAiOjE1ODg1MjQyOTQsImF6cCI6InJlSXE3dGViYzkxN1pTUVpUbWlLY0hUYlk0SThPVE1mIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJERUxFVEU6YWN0b3JzIiwiREVMRVRFOm1vdmllcyIsIkdFVDphY3RvcnMiLCJHRVQ6bW92aWVzIiwiUEFUQ0g6YWN0b3JzIiwiUEFUQ0g6bW92aWVzIiwiUE9TVDphY3RvcnMiLCJQT1NUOm1vdmllcyJdfQ.NplgkoTXsrrMP4bJcba1ZPoS7T2uBSZ7_bdna59bEmIHs_ZsZyiDftjlHBlGwHNX2h2ZAlmFmDib8GaYbYxJCN-yE8gGkqPKDnKK8MQGPFergchKyQnM5wMfdL2r4Mk9HtZMBi0okAsbjtul7kbcYrI8xCGcmZAlxW5vPLHNYkxvb-PyhYWFGi3_As4w5Qa3tA3tTbX_B7AY3kuavALTjKkbWt-SYqx-bgtNlp4p2M3JEOmL1Pr3lLvh9tpCRKt9R2_vF1HEmR2uK1riN_yjRpCQOaTFkC5181BtZO78UchTqR5HapnJ9w1Gc8sGUEdBi-KW4exAn58vWKZKtkescQ'
```
#### Example Response
```js
{
    "actors": [
        {
            "age": 40,
            "gender": "Male",
            "id": 1,
            "name": "Well Smith"
        },
        {
            "age": 30,
            "gender": "Other",
            "id": 2,
            "name": "Actor 2"
        }
    ],
    "success": true
}
```
#### Errors
If you try fetch a page that does not have any actors, you will have an error which looks like this:

```bash
$ curl -X GET https://udacity-fsdn-capstone-somaya.herokuapp.com/actors?page=123124
```

will return

```js
{
  "error": 404,
  "message": "No actors found.",
  "success": false
}
```

# <a name="post-actors"></a>
### 2. POST /actors

Insert a new actor into the database.

```bash
$ curl -X POST https://udacity-fsdn-capstone-somaya.herokuapp.com/actors
```

- Request Arguments: **None**
- Request Headers: (_application/json_)
  1. **JWT Bearer Token** `Authorization` (<span style="color:red">*</span>required)
- Request Body: (_application/json_)
  1. **string** `name` (<span style="color:red">*</span>required)
  2. **integer** `age` (<span style="color:red">*</span>required)
  3. **string** `gender`
- Requires permission: `Post:actors`
- Returns: 
  1. **integer** `id from newly created actor`
  2. **boolean** `success`

#### Example Request
```
curl --location --request POST 'https://udacity-fsdn-capstone-somaya.herokuapp.com/actors' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJERTFSVGM0TVRrek9VWTJOalJGTVRoR016RTRRamRGUWpKRFJUaEJRa0l3UVRZeU1qTkNOQSJ9.eyJpc3MiOiJodHRwczovL2ZzbmRzLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWFlZDVlMGVhZjg1MTBiZTdlYTQ2M2UiLCJhdWQiOiJDYXN0aW5nIiwiaWF0IjoxNTg4NTE3MDk0LCJleHAiOjE1ODg1MjQyOTQsImF6cCI6InJlSXE3dGViYzkxN1pTUVpUbWlLY0hUYlk0SThPVE1mIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJERUxFVEU6YWN0b3JzIiwiREVMRVRFOm1vdmllcyIsIkdFVDphY3RvcnMiLCJHRVQ6bW92aWVzIiwiUEFUQ0g6YWN0b3JzIiwiUEFUQ0g6bW92aWVzIiwiUE9TVDphY3RvcnMiLCJQT1NUOm1vdmllcyJdfQ.NplgkoTXsrrMP4bJcba1ZPoS7T2uBSZ7_bdna59bEmIHs_ZsZyiDftjlHBlGwHNX2h2ZAlmFmDib8GaYbYxJCN-yE8gGkqPKDnKK8MQGPFergchKyQnM5wMfdL2r4Mk9HtZMBi0okAsbjtul7kbcYrI8xCGcmZAlxW5vPLHNYkxvb-PyhYWFGi3_As4w5Qa3tA3tTbX_B7AY3kuavALTjKkbWt-SYqx-bgtNlp4p2M3JEOmL1Pr3lLvh9tpCRKt9R2_vF1HEmR2uK1riN_yjRpCQOaTFkC5181BtZO78UchTqR5HapnJ9w1Gc8sGUEdBi-KW4exAn58vWKZKtkescQ' \
--header 'Content-Type: application/json' \
--data-raw '{
   "age": 30,
   "gender": "Male",
   "name": "Actor 2"
}'
```

#### Example Response
```js
{
    "created": 2,
    "success": true
}

```
#### Errors
If you try to create a new actor without a required field like `name`,
it will throw a `422` error:

```bash
$ curl -X GET https://udacity-fsdn-capstone-somaya.herokuapp.com/actors?page=123124
```

will return

```js
{
  "error": 422,
  "message": "No name provided, name is required.",
  "success": false
}
```

# <a name="patch-actors"></a>
### 3. PATCH /actors

Edit an existing Actor

```bash
$ curl -X PATCH https://udacity-fsdn-capstone-somaya.herokuapp.com/actors/1
```

- Request Arguments: **integer** `id from actor you want to update`
- Request Headers: (_application/json_)
  1. **JWT Bearer Token** `Authorization` (<span style="color:red">*</span>required)
- Request Body: (_application/json_)
  1. **string** `name` (<span style="color:red">*</span>required)
  2. **integer** `age` (<span style="color:red">*</span>required)
  3. **string** `gender`
- Requires permission: `PATCH:actors`
- Returns: 
  1. **integer** `id from updated actor`
  2. **boolean** `success`
  3. List of actors with following fields:
      - **integer** `id`
      - **string** `name`
      - **string** `gender`
      - **integer** `age`

#### Example Request
```
curl --location --request PATCH 'https://udacity-fsdn-capstone-somaya.herokuapp.com/actors/1' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJERTFSVGM0TVRrek9VWTJOalJGTVRoR016RTRRamRGUWpKRFJUaEJRa0l3UVRZeU1qTkNOQSJ9.eyJpc3MiOiJodHRwczovL2ZzbmRzLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWFlZDVlMGVhZjg1MTBiZTdlYTQ2M2UiLCJhdWQiOiJDYXN0aW5nIiwiaWF0IjoxNTg4NTE3MDk0LCJleHAiOjE1ODg1MjQyOTQsImF6cCI6InJlSXE3dGViYzkxN1pTUVpUbWlLY0hUYlk0SThPVE1mIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJERUxFVEU6YWN0b3JzIiwiREVMRVRFOm1vdmllcyIsIkdFVDphY3RvcnMiLCJHRVQ6bW92aWVzIiwiUEFUQ0g6YWN0b3JzIiwiUEFUQ0g6bW92aWVzIiwiUE9TVDphY3RvcnMiLCJQT1NUOm1vdmllcyJdfQ.NplgkoTXsrrMP4bJcba1ZPoS7T2uBSZ7_bdna59bEmIHs_ZsZyiDftjlHBlGwHNX2h2ZAlmFmDib8GaYbYxJCN-yE8gGkqPKDnKK8MQGPFergchKyQnM5wMfdL2r4Mk9HtZMBi0okAsbjtul7kbcYrI8xCGcmZAlxW5vPLHNYkxvb-PyhYWFGi3_As4w5Qa3tA3tTbX_B7AY3kuavALTjKkbWt-SYqx-bgtNlp4p2M3JEOmL1Pr3lLvh9tpCRKt9R2_vF1HEmR2uK1riN_yjRpCQOaTFkC5181BtZO78UchTqR5HapnJ9w1Gc8sGUEdBi-KW4exAn58vWKZKtkescQ' \
--header 'Content-Type: application/json' \
--data-raw '{
   "age": 30,
   "gender": "Male",
   "name": "Well Smith"
}'
```

#### Example Response
```js
{
    "actor": [
        {
            "age": 30,
            "gender": "Male",
            "id": 1,
            "name": "Well Smith"
        }
    ],
    "success": true,
    "updated": 1
}
```
#### Errors
If you try to update an actor with an invalid id it will throw a `404`error:

```bash
$ curl -X PATCH https://udacity-fsdn-capstone-somaya.herokuapp.com/actors/125
```

will return

```js
{
  "error": 404,
  "message": "Actor with id 125 does not exist.",
  "success": false
}
```
Additionally, trying to update an Actor without sending actor ID in the URL will result in a `400` error:

```js
{
  "error": 400,
  "message": "Actor id URL parameter is required, please add an actor id to the request URL.",
  "success": false
}
```

# <a name="delete-actors"></a>
### 4. DELETE /actors

Delete an existing Actor

```bash
$ curl -X DELETE https://udacity-fsdn-capstone-somaya.herokuapp.com/actors/1
```

- Request Arguments: **integer** `id from actor you want to delete`
- Request Headers: 
  1. **JWT Bearer Token** `Authorization` (<span style="color:red">*</span>required)
- Requires permission: `delete:actors`
- Returns: 
  1. **integer** `id from deleted actor`
  2. **boolean** `success`

#### Example Request
```
curl --location --request DELETE 'https://udacity-fsdn-capstone-somaya.herokuapp.com/actors/3' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJERTFSVGM0TVRrek9VWTJOalJGTVRoR016RTRRamRGUWpKRFJUaEJRa0l3UVRZeU1qTkNOQSJ9.eyJpc3MiOiJodHRwczovL2ZzbmRzLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZTkwYTM5ZGY3NTk2MjBjMDhjN2JkYWYiLCJhdWQiOiJDYXN0aW5nIiwiaWF0IjoxNTg4NTE3MjgyLCJleHAiOjE1ODg1MjQ0ODIsImF6cCI6InJlSXE3dGViYzkxN1pTUVpUbWlLY0hUYlk0SThPVE1mIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJERUxFVEU6YWN0b3JzIiwiR0VUOmFjdG9ycyIsIkdFVDptb3ZpZXMiLCJQQVRDSDphY3RvcnMiLCJQQVRDSDptb3ZpZXMiLCJQT1NUOmFjdG9ycyJdfQ.CHN-jNaGGnrLH-cKWDiQSaCH9gT2Pgz0G0TAhFRjCEKwDDyyFOsoLyrYiTaUHH8mpatmeARurMU1Iv8tKmOg21XyOUBv8Q_Dnu7bdfEK-yMlWN_7PGR8cgcziY35Gy0pGOGtoeFxkxtWaum6k_taoIrL8JSyUEWzSLU2l3HrCDV6LQ1qC7ub0rugGrVcoeeU7W0b0p3C7ZG2jOnWJSi5BNWhu6aVRrRzk5TnLogcf3Z7t2-DaoJWLsMAmP5c7M1OG88azXjyxn6nEo4fFtqOALCySDI0WOmStpbRnl76T62jJLoOOIgvkQA_WGp3Sf-yRU9x-HKwMI0rp7aayG6xlQ'
```

#### Example Response
```js
{
    "deleted": 3,
    "success": true
}

```
#### Errors
If you try to delete actor with an invalid id, it will throw a `404`error:

```bash
$ curl -X DELETE https://udacity-fsdn-capstone-somaya.herokuapp.com/actors/125
```

will return

```js
{
  "error": 404,
  "message": "Actor with id 125 does not exist.",
  "success": false
}
```

# <a name="get-movies"></a>
### 5. GET /movies

Query paginated movies.

```bash
$ curl -X GET https://udacity-fsdn-capstone-somaya.herokuapp.com/movies?page=1
```
- This API fetches the list of movies
- Request Arguments: 
  1. **integer** `page` (optional, 10 movies per page, defaults to `1` if not given)
- Request Headers: 
  1. **JWT Bearer Token** `Authorization` (<span style="color:red">*</span>required)
- Requires permission: `GET:movies`
- Returns: 
  1. List of movies with following fields:
      - **integer** `id`
      - **string** `name`
      - **date** `release_date`
  2. **boolean** `success`

#### Example Request
```
curl --location --request GET 'https://udacity-fsdn-capstone-somaya.herokuapp.com/movies' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJERTFSVGM0TVRrek9VWTJOalJGTVRoR016RTRRamRGUWpKRFJUaEJRa0l3UVRZeU1qTkNOQSJ9.eyJpc3MiOiJodHRwczovL2ZzbmRzLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWFlZDVlMGVhZjg1MTBiZTdlYTQ2M2UiLCJhdWQiOiJDYXN0aW5nIiwiaWF0IjoxNTg4NTE3MDk0LCJleHAiOjE1ODg1MjQyOTQsImF6cCI6InJlSXE3dGViYzkxN1pTUVpUbWlLY0hUYlk0SThPVE1mIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJERUxFVEU6YWN0b3JzIiwiREVMRVRFOm1vdmllcyIsIkdFVDphY3RvcnMiLCJHRVQ6bW92aWVzIiwiUEFUQ0g6YWN0b3JzIiwiUEFUQ0g6bW92aWVzIiwiUE9TVDphY3RvcnMiLCJQT1NUOm1vdmllcyJdfQ.NplgkoTXsrrMP4bJcba1ZPoS7T2uBSZ7_bdna59bEmIHs_ZsZyiDftjlHBlGwHNX2h2ZAlmFmDib8GaYbYxJCN-yE8gGkqPKDnKK8MQGPFergchKyQnM5wMfdL2r4Mk9HtZMBi0okAsbjtul7kbcYrI8xCGcmZAlxW5vPLHNYkxvb-PyhYWFGi3_As4w5Qa3tA3tTbX_B7AY3kuavALTjKkbWt-SYqx-bgtNlp4p2M3JEOmL1Pr3lLvh9tpCRKt9R2_vF1HEmR2uK1riN_yjRpCQOaTFkC5181BtZO78UchTqR5HapnJ9w1Gc8sGUEdBi-KW4exAn58vWKZKtkescQ'
```

#### Example Response
```js
{
  "movies": [
    {
      "id": 1,
      "release_date": "Thur, 30 Sep 2004 00:00:00 GMT",
      "title": "Notebook"
    }
  ],
  "success": true
}

```
#### Errors
If you try fetch a page which does not have any movies, you will have an error which looks like this:

```bash
$ curl -X GET https://udacity-fsdn-capstone-somaya.herokuapp.com/movies?page=123124
```

will return

```js
{
  "error": 404,
  "message": "No movies found.",
  "success": false
}
```

# <a name="post-movies"></a>
### 6. POST /movies

Insert new Movie into database.

```bash
$ curl -X POST https://udacity-fsdn-capstone-somaya.herokuapp.com/movies
```

- Request Arguments: **None**
- Request Headers: (_application/json_)
  1. **JWT Bearer Token** `Authorization` (<span style="color:red">*</span>required)
- Request Body: (_application/json_)
  1. **string** `title` (<span style="color:red">*</span>required)
  2. **date** `release_date` (<span style="color:red">*</span>required)
- Requires permission: `POST:movies`
- Returns: 
  1. **integer** `id from newly created movie`
  2. **boolean** `success`

#### Example Request
```
curl --location --request POST 'https://udacity-fsdn-capstone-somaya.herokuapp.com/movies' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJERTFSVGM0TVRrek9VWTJOalJGTVRoR016RTRRamRGUWpKRFJUaEJRa0l3UVRZeU1qTkNOQSJ9.eyJpc3MiOiJodHRwczovL2ZzbmRzLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWFlZDVlMGVhZjg1MTBiZTdlYTQ2M2UiLCJhdWQiOiJDYXN0aW5nIiwiaWF0IjoxNTg4NTE3MDk0LCJleHAiOjE1ODg1MjQyOTQsImF6cCI6InJlSXE3dGViYzkxN1pTUVpUbWlLY0hUYlk0SThPVE1mIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJERUxFVEU6YWN0b3JzIiwiREVMRVRFOm1vdmllcyIsIkdFVDphY3RvcnMiLCJHRVQ6bW92aWVzIiwiUEFUQ0g6YWN0b3JzIiwiUEFUQ0g6bW92aWVzIiwiUE9TVDphY3RvcnMiLCJQT1NUOm1vdmllcyJdfQ.NplgkoTXsrrMP4bJcba1ZPoS7T2uBSZ7_bdna59bEmIHs_ZsZyiDftjlHBlGwHNX2h2ZAlmFmDib8GaYbYxJCN-yE8gGkqPKDnKK8MQGPFergchKyQnM5wMfdL2r4Mk9HtZMBi0okAsbjtul7kbcYrI8xCGcmZAlxW5vPLHNYkxvb-PyhYWFGi3_As4w5Qa3tA3tTbX_B7AY3kuavALTjKkbWt-SYqx-bgtNlp4p2M3JEOmL1Pr3lLvh9tpCRKt9R2_vF1HEmR2uK1riN_yjRpCQOaTFkC5181BtZO78UchTqR5HapnJ9w1Gc8sGUEdBi-KW4exAn58vWKZKtkescQ' \
--header 'Content-Type: application/json' \
--data-raw '{
	"release_date": "Sun, 17 May 2020 00:00:00 GMT",
	"title": "Life after COVID19"
}'
```

#### Example Response
```js
{
    "created": 5,
    "success": true
}
```
#### Errors
If you try to create a new movie without a required field like `title`,
it will throw a `422` error:

```bash
$ curl -X GET https://udacity-fsdn-capstone-somaya.herokuapp.com/movies?page=123124
```

will return

```js
{
  "error": 422,
  "message": "No title provided, the title is required.",
  "success": false
}
```

# <a name="patch-movies"></a>
### 7. PATCH /movies

Edit an existing Movie

```bash
$ curl -X PATCH https://udacity-fsdn-capstone-somaya.herokuapp.com/movies/1
```

- Request Arguments: **integer** `id from movie you want to update`
- Request Headers: (_application/json_)
  1. **JWT Bearer Token** `Authorization` (<span style="color:red">*</span>required)
- Request Body: (_application/json_)
  1. **string** `title` 
  2. **date** `release_date` 
- Requires permission: `PATCH:movies`
- Returns: 
  1. **integer** `id from updated movie`
  2. **boolean** `success`
  3. List of movies with following fields:
        - **integer** `id`
        - **string** `title` 
        - **date** `release_date` 

#### Example Request
```
curl --location --request PATCH 'https://udacity-fsdn-capstone-somaya.herokuapp.com/movies/3' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJERTFSVGM0TVRrek9VWTJOalJGTVRoR016RTRRamRGUWpKRFJUaEJRa0l3UVRZeU1qTkNOQSJ9.eyJpc3MiOiJodHRwczovL2ZzbmRzLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWFlZDVlMGVhZjg1MTBiZTdlYTQ2M2UiLCJhdWQiOiJDYXN0aW5nIiwiaWF0IjoxNTg4NTE3MDk0LCJleHAiOjE1ODg1MjQyOTQsImF6cCI6InJlSXE3dGViYzkxN1pTUVpUbWlLY0hUYlk0SThPVE1mIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJERUxFVEU6YWN0b3JzIiwiREVMRVRFOm1vdmllcyIsIkdFVDphY3RvcnMiLCJHRVQ6bW92aWVzIiwiUEFUQ0g6YWN0b3JzIiwiUEFUQ0g6bW92aWVzIiwiUE9TVDphY3RvcnMiLCJQT1NUOm1vdmllcyJdfQ.NplgkoTXsrrMP4bJcba1ZPoS7T2uBSZ7_bdna59bEmIHs_ZsZyiDftjlHBlGwHNX2h2ZAlmFmDib8GaYbYxJCN-yE8gGkqPKDnKK8MQGPFergchKyQnM5wMfdL2r4Mk9HtZMBi0okAsbjtul7kbcYrI8xCGcmZAlxW5vPLHNYkxvb-PyhYWFGi3_As4w5Qa3tA3tTbX_B7AY3kuavALTjKkbWt-SYqx-bgtNlp4p2M3JEOmL1Pr3lLvh9tpCRKt9R2_vF1HEmR2uK1riN_yjRpCQOaTFkC5181BtZO78UchTqR5HapnJ9w1Gc8sGUEdBi-KW4exAn58vWKZKtkescQ' \
--header 'Content-Type: application/json' \
--data-raw '{
   "title": "Somaya 1st Movie"
}'
```

#### Example Response
```js
{
    "movie": [
        {
            "id": 3,
            "release_date": "Sun, 10 May 2020 16:30:00 GMT",
            "title": "Somaya 1st Movie"
        }
    ],
    "success": true,
    "updated": 3
}

```
#### Errors
If you try to update a movie with an invalid id it will throw a `404`error:

```bash
$ curl -X PATCH https://udacity-fsdn-capstone-somaya.herokuapp.com/movies/125
```

will return

```js
{
  "error": 404,
  "message": "Movie with id 125 does not exist.",
  "success": false
}
```
Additionally, trying to update a Movie without sending the movie ID in the URL will result in a `400` error:

```js
{
  "error": 400,
  "message": "Movie id URL parameter is required, please add a movie id to the request URL.",
  "success": false
}
```

# <a name="delete-movies"></a>
### 8. DELETE /movies

Delete an existing movie

```bash
$ curl -X DELETE https://udacity-fsdn-capstone-somaya.herokuapp.com/movies/1
```

- Request Arguments: 
  1. **integer** `id from movie you want to delete`
- Request Headers: 
  1. **JWT Bearer Token** `Authorization` (<span style="color:red">*</span>required)
- Requires permission: `DELETE:movies`
- Returns: 
  1. **integer** `id from deleted movie`
  2. **boolean** `success`

#### Example Request
```
curl --location --request DELETE 'https://udacity-fsdn-capstone-somaya.herokuapp.com/movies/3' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJERTFSVGM0TVRrek9VWTJOalJGTVRoR016RTRRamRGUWpKRFJUaEJRa0l3UVRZeU1qTkNOQSJ9.eyJpc3MiOiJodHRwczovL2ZzbmRzLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWFlZDVlMGVhZjg1MTBiZTdlYTQ2M2UiLCJhdWQiOiJDYXN0aW5nIiwiaWF0IjoxNTg4NTE3MDk0LCJleHAiOjE1ODg1MjQyOTQsImF6cCI6InJlSXE3dGViYzkxN1pTUVpUbWlLY0hUYlk0SThPVE1mIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJERUxFVEU6YWN0b3JzIiwiREVMRVRFOm1vdmllcyIsIkdFVDphY3RvcnMiLCJHRVQ6bW92aWVzIiwiUEFUQ0g6YWN0b3JzIiwiUEFUQ0g6bW92aWVzIiwiUE9TVDphY3RvcnMiLCJQT1NUOm1vdmllcyJdfQ.NplgkoTXsrrMP4bJcba1ZPoS7T2uBSZ7_bdna59bEmIHs_ZsZyiDftjlHBlGwHNX2h2ZAlmFmDib8GaYbYxJCN-yE8gGkqPKDnKK8MQGPFergchKyQnM5wMfdL2r4Mk9HtZMBi0okAsbjtul7kbcYrI8xCGcmZAlxW5vPLHNYkxvb-PyhYWFGi3_As4w5Qa3tA3tTbX_B7AY3kuavALTjKkbWt-SYqx-bgtNlp4p2M3JEOmL1Pr3lLvh9tpCRKt9R2_vF1HEmR2uK1riN_yjRpCQOaTFkC5181BtZO78UchTqR5HapnJ9w1Gc8sGUEdBi-KW4exAn58vWKZKtkescQ'
```

#### Example Response
```js
{
    "deleted": 3,
    "success": true
}

```
#### Errors
If you try to delete movie with an invalid id, it will throw a `404`error:

```bash
$ curl -X DELETE https://udacity-fsdn-capstone-somaya.herokuapp.com/movies/125
```

will return

```js
{
  "error": 404,
  "message": "Movie with id 125 does not exist.",
  "success": false
}
```

# <a name="authentication"></a>
## Authentication

All API Endpoints are decorated with Auth0 permissions. To use the project locally, you need to configure Auth0 accordingly

### Auth0 for locally use
#### Create an App & API

1. Login to https://manage.auth0.com/ 
2. Click on Applications Tab
3. Create Application
4. Give it a name like `Casting` and select "Regular Web Application". If you want to create Javascript application that integrates with API, select "Single Page Web Applications"
5. Go to Settings and find `domain`. Copy & paste it into config.py => auth0_config['AUTH0_DOMAIN'] (i.e. replace `"fsnds.eu.auth0.com"`)
6. Click on API Tab 
7. Create a new API:
   1. Name: `Casting`
   2. Identifier `Casting`
   3. Keep Algorithm as it is
8. Go to Settings and find `Identifier`. Copy & paste it into config.py => auth0_config['API_AUDIENCE'] (i.e. replace `"Example"`)

#### Create Roles and Permissions

1. Before creating `Roles & Permissions`, you need to enable `Enable RBAC` and `Add Permissions in the Access Token` in your API (API => Click on your API Name => Settings => Enable RBAC and Add Permissions in the Access Token => Save)
2. Also, check the button `Add Permissions in the Access Token`.
2. First, create a new Role under `Users and Roles` => `Roles` => `Create Roles`
3. Give it a descriptive name like `Casting Assistant`.
4. Go back to the API Tab and find your newly created API. Click on Permissions.
5. Create & assign all needed permissions accordingly 
6. After you created all permissions this app needs, go back to `Users and Roles` => `Roles` and select the role you recently created.
6. Under `Permissions`, assign all permissions you want this role to have. 

# <a name="authentication-bearer"></a>
### Auth0 to use an Existing API
If you want to access the real, temporary API, bearer tokens for all 3 roles are included in the `config.py` file.

## Existing Roles

They are 3 Roles with distinct permission sets:

1. Casting Assistant:
  - GET /actors (GET:actors): Can see all actors
  - GET /movies (GET:movies): Can see all movies
2. Casting Director (everything from Casting Assistant plus)
  - POST /actors (POST:actors): Can create new Actors
  - PATCH /actors (PATCH:actors): Can edit existing Actors
  - DELETE /actors (DELETE:actors): Can remove existing Actors from database
  - PATCH /movies (PATCH:movies): Can edit existing Movies
3. Exectutive Dircector (everything from Casting Director plus)
  - POST /movies (POST:movies): Can create new Movies
  - DELETE /movies (DELETE:movies): Can remove existing Motives from database

In your API Calls, add them as Header, with `Authorization` as key and the `Bearer token` as value. Don´t forget to also
prepend `Bearer` to the token (seperated by space).

For example: (Bearer token for `Executive Director`)
```js
{
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJERTFSVGM0TVRrek9VWTJOalJGTVRoR016RTRRamRGUWpKRFJUaEJRa0l3UVRZeU1qTkNOQSJ9.eyJpc3MiOiJodHRwczovL2ZzbmRzLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWFlZDVlMGVhZjg1MTBiZTdlYTQ2M2UiLCJhdWQiOiJDYXN0aW5nIiwiaWF0IjoxNTg4NTE3MDk0LCJleHAiOjE1ODg1MjQyOTQsImF6cCI6InJlSXE3dGViYzkxN1pTUVpUbWlLY0hUYlk0SThPVE1mIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJERUxFVEU6YWN0b3JzIiwiREVMRVRFOm1vdmllcyIsIkdFVDphY3RvcnMiLCJHRVQ6bW92aWVzIiwiUEFUQ0g6YWN0b3JzIiwiUEFUQ0g6bW92aWVzIiwiUE9TVDphY3RvcnMiLCJQT1NUOm1vdmllcyJdfQ.NplgkoTXsrrMP4bJcba1ZPoS7T2uBSZ7_bdna59bEmIHs_ZsZyiDftjlHBlGwHNX2h2ZAlmFmDib8GaYbYxJCN-yE8gGkqPKDnKK8MQGPFergchKyQnM5wMfdL2r4Mk9HtZMBi0okAsbjtul7kbcYrI8xCGcmZAlxW5vPLHNYkxvb-PyhYWFGi3_As4w5Qa3tA3tTbX_B7AY3kuavALTjKkbWt-SYqx-bgtNlp4p2M3JEOmL1Pr3lLvh9tpCRKt9R2_vF1HEmR2uK1riN_yjRpCQOaTFkC5181BtZO78UchTqR5HapnJ9w1Gc8sGUEdBi-KW4exAn58vWKZKtkescQ"
}
```