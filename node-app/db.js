const mysql = require('mysql')

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

// connection.connect()

module.exports.db = () => connection
