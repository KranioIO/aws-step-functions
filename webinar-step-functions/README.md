# Requerimientos

- python3.+
- node y npm
- instalar serverless de forma global

# Instalar plugins via terminal en el siguiente orden:

Esto actualizará tu item plugins en serverless.yml

`sls plugin install -n serverless-python-requirements`
`sls plugin install -n serverless-pseudo-parameters`
`sls plugin install -n serverless-step-functions`


# Actualiza json de dependencias
`npm install`

# Deploy

`sls deploy -s dev`

