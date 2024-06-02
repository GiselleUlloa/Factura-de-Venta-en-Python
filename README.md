# Facturación en Python

Este proyecto implementa un sistema básico de facturación en Python, que incluye la gestión de facturas, detalles de productos y métodos de pago. A continuación se detalla la funcionalidad del código.

## Descripción de Clases

### Clase `Factura`

La clase `Factura` maneja la información de una factura, incluyendo los detalles del cliente y los productos adquiridos. Además, permite calcular el subtotal, aplicar descuentos e IVA, y calcular el total.

**Atributos:**
- `numero`: Número de la factura.
- `nit`: NIT de la empresa.
- `razon_social`: Razón social de la empresa.
- `identificacion`: Identificación del cliente.
- `cliente`: Nombre del cliente.
- `direccion`: Dirección del cliente.
- `telefono`: Teléfono del cliente.
- `fecha_emision`: Fecha de emisión de la factura.
- `detalles`: Lista de detalles de productos.
- `descuento`: Porcentaje de descuento aplicado a la factura.
- `iva`: Porcentaje de IVA aplicado (por defecto 19%).
- `comentarios`: Comentarios adicionales en la factura.

**Métodos:**
- Getters y Setters para cada atributo.
- `agregar_detalle(detalle)`: Agrega un detalle de producto a la factura.
- `calcular_subtotal()`: Calcula el subtotal de la factura.
- `calcular_total()`: Calcula el total de la factura incluyendo descuento e IVA.
- `aplicar_descuento(porcentaje)`: Aplica un porcentaje de descuento a la factura.
- `agregar_comentarios(comentarios)`: Agrega comentarios adicionales a la factura.
- `imprimir_factura()`: Imprime la factura en formato legible.

### Clase `Detalle`

La clase `Detalle` representa un producto o servicio en la factura.

**Atributos:**
- `codigo`: Código del producto.
- `descripcion`: Descripción del producto.
- `valor_unidad`: Valor por unidad del producto.
- `unidad`: Cantidad de unidades del producto.
- `subtotal`: Subtotal calculado del producto (valor_unidad * unidad).

**Métodos:**
- Getters y Setters para cada atributo.

### Clases de Pago

Las clases `Pago`, `PagoDebito`, `PagoCredito` y `PagoEfectivo` representan diferentes métodos de pago.

**Clase `Pago`:**
- `monto`: Monto del pago.
- Métodos: Getters y Setters.

**Clase `PagoDebito` (hereda de `Pago`):**
- `numero_tarjeta`: Número de la tarjeta de débito.
- Métodos: Getters y Setters, `mostrar_pago()`.

**Clase `PagoCredito` (hereda de `Pago`):**
- `numero_tarjeta`: Número de la tarjeta de crédito.
- `numero_cuotas`: Número de cuotas.
- `codigo_verificacion`: Código de verificación de la tarjeta.
- Métodos: Getters y Setters, `mostrar_pago()`.

**Clase `PagoEfectivo` (hereda de `Pago`):**
- Métodos: `mostrar_pago()`.

### Función `seleccionar_metodo_pago(total)`

Permite al usuario seleccionar un método de pago (efectivo, tarjeta de débito o crédito) y valida la información de pago ingresada.

