const { root, creaCliente, creaSocio, creaBeneficio } = require('./service')
// este require serverless-http te permite hacer deploy de tu rest, en un API GATEWAY de AWS.
const serverless = require('serverless-http')
const express = require('express')
const app = express()
const port = 3000

app.use(express.urlencoded())

app.get('/', root)
app.post('/crea_cliente', creaCliente)
app.post('/crea_socio', creaSocio)
app.post('/crea_beneficio', creaBeneficio)

app.listen(port, () => console.log('Conectado'))

// el nombre luego de exports (en este caso handler) es el nombre de eśte módulo como lambda para AWS.
module.exports.handler = serverless(app)
