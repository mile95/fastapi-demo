# FastAPI demo 2021-10-15

Demo of how to write backend with Python using FastAPI. Took place at Devies 2021-10-15.

## Setup environment and install requirements

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements
```

## Start webserver with the API

```
uvicorn main:app --reload
```

The API is now running on `localhost:8000`, go to `localhost:8000/docs` for interactive docs.


## Run the tests

```
pytest .
```

## Build and run docker image

```
docker build -t api .
docker run -d -p 80:80 api
```

The API is not running on `127.0.0.1`, go to `127.0.0.1/docs` for interactive docs.
