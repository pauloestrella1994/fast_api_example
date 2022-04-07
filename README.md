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

After log into PGAdmin, access the server using the same password

Copy local.env to a .env file, to run connection into the database
```
cp local.env .env
```
