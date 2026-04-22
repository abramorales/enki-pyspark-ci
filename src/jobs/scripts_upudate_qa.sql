SELECT cuenta FROM ventas;

SELECT
    id,
    monto
FROM ventas;

SELECT
    id,
    monto
FROM ventas;

SELECT v.ventas FROM ventas AS v, clientes AS c
WHERE v.id = c.id;

SELECT monto * 1.16 AS monto_con_iva
FROM ventas;

SELECT ic.d
FROM ventas AS v
INNER JOIN clientes AS c ON v.id = c.id;

SELECT
    id,
    nombre,
    direccion,
    telefono,
    correo,
    fecha_registro
FROM clientes
WHERE estado = 'ACTIVO';

SELECT id FROM ventas;