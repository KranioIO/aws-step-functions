const {
  returnCreaPersonaQuery,
  returnCreaSocioQuery,
  returnCreaBeneficioQuery
} = require('./queries')
const mysql = require('mysql')

module.exports.root = (req, res) => {
  res.send('Hola amigos del webinar!')
}

module.exports.creaCliente = (req, res) => {
  console.log('creando cliente...')
  const { nombre, apellido, rut, mail, telefono } = req.body
  const query = returnCreaPersonaQuery(nombre, apellido, rut, mail, telefono)
  console.log(query)
  try {
    connection.query(query, (err, rows, fields) => {
      if (err) {
        console.log(err)
        res
          .status(400)
          .json({ success: false, description: 'cliente ya existe' })
      } else {
        console.log(rows)
        console.log(fields)
        res.json({ success: true, description: 'cliente creado exitosamente', rut: rut, sucursal: req.body.sucursal, quiereTarjeta: req.body.quiereTarjeta })
      }
    })
  } catch (error) {
    console.log(error)
    res.status(500).json({ success: false, description: 'error de conexion' })
  }
}

module.exports.creaSocio = (req, res) => {
  console.log('creando socio...')
  const { rut, sucursal, quiereTarjeta } = req.body
  const query = returnCreaSocioQuery(rut, sucursal)

  console.log(query)
  try {
    connection.query(query, (err, rows, fields) => {
      if (err) {
        console.log(err)
        res
          .status(400)
          .json({ success: false, description: 'socio ya existe' })
      } else {
        console.log(rows)
        console.log(fields)
        res.json({ success: true, description: 'socio creado exitosamente', rut: rut, quiereTarjeta: quiereTarjeta })
      }
    })
  } catch (error) {
    console.log(error)
    res.status(500).json({ success: false, description: 'error de conexion' })
  }
}

module.exports.creaBeneficio = (req, res) => {
  console.log('creando beneficio...')
  const { rut, quiereTarjeta } = req.body
  const query = returnCreaBeneficioQuery(rut, quiereTarjeta)

  console.log(query)
  try {
    connection.query(query, (err, rows, fields) => {
      if (err) {
        console.log(err)
        res.status(400).json({
          success: false,
          description: 'error al crear beneficios. revisar log.'
        })
      } else {
        console.log(rows)
        console.log(fields)
        res.json({ success: true, description: 'cliente quiere tarjeta.' })
      }
    })
  } catch (error) {
    console.log(error)
    res.status(500).json({ success: false, description: 'error de conexion' })
  }
}

// debes reemplazar con tus valores
const USER = 'cartulina'
const PASS = '20202021'
const DATABASE = 'WebinarMariaDB'
const HOST = 'wwq3tvcl5unk7d.cmvhpzzezajb.us-east-2.rds.amazonaws.com'


const connection = mysql.createConnection({
  host: HOST,
  user: USER,
  password: PASS,
  database: DATABASE
})
