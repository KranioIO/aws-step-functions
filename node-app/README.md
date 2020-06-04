# API

## Requisitos
- npm
- node
- serverless

## Servidor local en localhost:3000

presiona F5 para levantar servidor local.
puedes hacer post en `localhost:3000/{endpoint}`
ej: `localhost:3000/crear_cliente`

## POST /crea_cliente

| parameter  | format | desc             |
|------------|--------|------------------|
| nombre     | string | nombre persona   |
| apellido   | string | apellido persona |
| rut        | string | rut persona      |
| telefono   | int    | telefono persona |

## POST /crea_socio

| parameter  | format | desc             |
|------------|--------|------------------|
| rut        | string | rut (11111111-1) |
| sucursal   | string | sucursal cliente |


## POST /crea_beneficio_

| parameter     | format | desc             |
|---------------|--------|------------------|
| rut           | string | rut (11111111-1) |
| quiereTarjeta | string | si / no          |


# Database

DB_USER = 'user'
DB_PASS = 'password'
DATABASE='nombre_de_tu_db'
PORT = puerto
HOST = endpoint_de_tu_db'
