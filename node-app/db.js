const mysql = require('mysql')

const USER = 'root'
const PASS = 'lN2eeHp8r'
const DATABASE = 'WebinarMariaDB'
const HOST = 'wwwmfot5xbet9i.cmvhpzzezajb.us-east-2.rds.amazonaws.com'

const connection = mysql.createConnection({
  host: HOST,
  user: USER,
  password: PASS,
  database: DATABASE
})

// connection.connect()

module.exports.db = () => connection
