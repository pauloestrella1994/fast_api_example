# Fast Api example

## Instalation
Install [python >= 3.9](https://www.python.org/downloads/) and install poetry:

```
pip install poetry
```

To install dependencies and create a virtual environment

```
poetry install
```

Run Postgresql and PGAdmin:

```
docker-compose up
```

to access PGAdmin, run in your browser:

```
http://localhost:5050
```

Login

```
Email Adress: admin@gmail.com
Password: admin
```

After log into PGAdmin, access the server using the same password. Open the server and create a new connection by clicking with the second button in Server > Register > Server with the values bellow.

```
Name: fastapi
```

in Connection, use these values bellow:

```
Host: postgresql
Password: admin
```

Copy local.env to a .env file, to run connection into the database
```
cp local.env .env
```

After create a database and install dependencies, with the containers of postgresql running in other terminal,
create a bash variable with your locally path. To see what is your local path in Linux, just run:

```
$ pwd
/home/user/your_local_path
```

Copy this path and add in your bash, the variable PYTHONPATH:

```
export PYTHONPATH="/home/user/your_local_path"
```

Reload the terminal with source, and then run to create the tables:

```
poetry run python database/init_db.py
```

Now you can check your tables created in your database.
To create random data to test the endpoints, run:

```
poetry run python populate.py
```

## Documentation

To see the endpoints, run the project with:

```
make server
```

And you can access the Swagger Documentation in your browser

```
http://127.0.0.1:8000/docs
```

Or even, accessing redoc:

```
http://127.0.0.1:8000/redoc
```
