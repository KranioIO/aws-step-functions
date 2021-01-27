// queries para la DB. se arman con los datos del req.body
module.exports.returnCreaPersonaQuery = (
  nombre,
  apellido,
  rut,
  mail,
  telefono
) => {
  const creaPersonaQuery = `
    INSERT INTO personas (nombre,apellido,rut,mail,telefono) 
    VALUES ('${nombre}', '${apellido}', '${rut}', '${mail}', '${telefono}')`;
  return creaPersonaQuery;
};

module.exports.returnCreaSocioQuery = (rut, sucursal) => {
  const creaSocioQuery = `
    INSERT INTO socios (rut, sucursal) 
    VALUES ('${rut}', '${sucursal}')`;
  return creaSocioQuery;
};

module.exports.returnCreaBeneficioQuery = (rut, quiereTarjeta) => {
  const creaBeneficioQuery = `
    INSERT INTO beneficios (rut, quiere_tarjeta) 
    VALUES ('${rut}', '${quiereTarjeta}')`;
  return creaBeneficioQuery;
};
