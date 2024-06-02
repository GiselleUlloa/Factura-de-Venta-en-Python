from datetime import datetime

class Factura:
    def __init__(self, numero=None, nit=None, razon_social=None, identificacion=None, cliente=None, direccion=None, telefono=None):
        self.numero = numero
        self.nit = nit
        self.razon_social = razon_social
        self.identificacion = identificacion
        self.cliente = cliente
        self.direccion = direccion
        self.telefono = telefono
        self.fecha_emision = datetime.now()
        self.detalles = []
        self.descuento = 0
        self.iva = 0.19  # 19% de IVA por defecto
        self.comentarios = ""

    # Getters and Setters
    def get_numero(self):
        return self.numero

    def set_numero(self, numero):
        self.numero = numero

    def get_nit(self):
        return self.nit

    def set_nit(self, nit):
        self.nit = nit

    def get_razon_social(self):
        return self.razon_social

    def set_razon_social(self, razon_social):
        self.razon_social = razon_social

    def get_identificacion(self):
        return self.identificacion

    def set_identificacion(self, identificacion):
        self.identificacion = identificacion

    def get_cliente(self):
        return self.cliente

    def set_cliente(self, cliente):
        self.cliente = cliente

    def get_direccion(self):
        return self.direccion

    def set_direccion(self, direccion):
        self.direccion = direccion

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, telefono):
        self.telefono = telefono

    def get_fecha_emision(self):
        return self.fecha_emision

    def set_fecha_emision(self, fecha_emision):
        self.fecha_emision = fecha_emision

    def get_detalles(self):
        return self.detalles

    def set_detalles(self, detalles):
        self.detalles = detalles

    def get_descuento(self):
        return self.descuento

    def set_descuento(self, descuento):
        self.descuento = descuento

    def get_iva(self):
        return self.iva

    def set_iva(self, iva):
        self.iva = iva

    def get_comentarios(self):
        return self.comentarios

    def set_comentarios(self, comentarios):
        self.comentarios = comentarios

    def agregar_detalle(self, detalle):
        if detalle.unidad <= 0:
            raise ValueError("La cantidad de unidades debe ser mayor que cero.")
        self.detalles.append(detalle)

    def calcular_subtotal(self):
        return sum(detalle.subtotal for detalle in self.detalles)

    def calcular_total(self):
        subtotal = self.calcular_subtotal()
        total_descuento = subtotal * self.descuento
        total_iva = (subtotal - total_descuento) * self.iva
        return subtotal - total_descuento + total_iva

    def aplicar_descuento(self, porcentaje):
        if 0 <= porcentaje <= 1:
            self.descuento = porcentaje
        else:
            raise ValueError("El descuento debe estar entre 0 y 1.")

    def agregar_comentarios(self, comentarios):
        self.comentarios = comentarios

    def imprimir_factura(self):
        print(f"Factura: No {self.numero}       Nit: {self.nit}     Razon Social: {self.razon_social}") 
        print(f"Identificacion: {self.identificacion}    Tipo: Persona Natural")
        print(f"Cliente: {self.cliente}")
        print(f"Direccion: {self.direccion}    Telefono: {self.telefono}")
        print(f"Fecha de Emision: {self.fecha_emision.strftime('%Y-%m-%d %H:%M:%S')}")
        print("\nDetalle de la Factura")
        print("Codigo   Detalle   Valor Unidad   Unidad   SubTotal")
        for detalle in self.detalles:
            print(f"{detalle.codigo}   {detalle.descripcion}   {detalle.valor_unidad}   {detalle.unidad}   {detalle.subtotal}")
        subtotal = self.calcular_subtotal()
        print(f"\nSubtotal: {subtotal}")
        print(f"Descuento: {self.descuento * 100}%")
        print(f"IVA: {self.iva * 100}%")
        print(f"Total: {self.calcular_total()}")
        if self.comentarios:
            print(f"\nComentarios: {self.comentarios}")

class Detalle:
    def __init__(self, codigo=None, descripcion=None, valor_unidad=None, unidad=None):
        if unidad is not None and valor_unidad is not None and (unidad <= 0 or valor_unidad <= 0):
            raise ValueError("El valor por unidad y la cantidad de unidades deben ser mayores que cero.")
        self.codigo = codigo
        self.descripcion = descripcion
        self.valor_unidad = valor_unidad
        self.unidad = unidad
        self.subtotal = valor_unidad * unidad if valor_unidad and unidad else 0

    # Getters and Setters
    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo

    def get_descripcion(self):
        return self.descripcion

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def get_valor_unidad(self):
        return self.valor_unidad

    def set_valor_unidad(self, valor_unidad):
        self.valor_unidad = valor_unidad

    def get_unidad(self):
        return self.unidad

    def set_unidad(self, unidad):
        self.unidad = unidad

    def get_subtotal(self):
        return self.subtotal

    def set_subtotal(self, subtotal):
        self.subtotal = subtotal

class Pago:
    def __init__(self, monto=None):
        self.monto = monto

    # Getters and Setters
    def get_monto(self):
        return self.monto

    def set_monto(self, monto):
        self.monto = monto

    def mostrar_pago(self):
        print(f"Pago realizado: {self.monto}")

class PagoDebito(Pago):
    def __init__(self, monto=None, numero_tarjeta=None):
        super().__init__(monto)
        self.numero_tarjeta = numero_tarjeta

    # Getters and Setters
    def get_numero_tarjeta(self):
        return self.numero_tarjeta

    def set_numero_tarjeta(self, numero_tarjeta):
        self.numero_tarjeta = numero_tarjeta

    def mostrar_pago(self):
        print(f"Pago con tarjeta de débito: {self.monto}, Número de tarjeta: {self.numero_tarjeta}")

class PagoCredito(Pago):
    def __init__(self, monto=None, numero_tarjeta=None, numero_cuotas=None, codigo_verificacion=None):
        super().__init__(monto)
        self.numero_tarjeta = numero_tarjeta
        self.numero_cuotas = numero_cuotas
        self.codigo_verificacion = codigo_verificacion

    # Getters and Setters
    def get_numero_tarjeta(self):
        return self.numero_tarjeta

    def set_numero_tarjeta(self, numero_tarjeta):
        self.numero_tarjeta = numero_tarjeta

    def get_numero_cuotas(self):
        return self.numero_cuotas

    def set_numero_cuotas(self, numero_cuotas):
        self.numero_cuotas = numero_cuotas

    def get_codigo_verificacion(self):
        return self.codigo_verificacion

    def set_codigo_verificacion(self, codigo_verificacion):
        self.codigo_verificacion = codigo_verificacion

    def mostrar_pago(self):
        print(f"Pago con tarjeta de crédito: {self.monto}, Número de tarjeta: {self.numero_tarjeta}, Número de cuotas: {self.numero_cuotas}, Código de verificación: {self.codigo_verificacion}")

class PagoEfectivo(Pago):
    def __init__(self, monto=None):
        super().__init__(monto)

    def mostrar_pago(self):
        print(f"Pago en efectivo: {self.monto}")

def seleccionar_metodo_pago(total):
    print("\nSeleccione el método de pago:")
    print("1. Efectivo")
    print("2. Tarjeta de Débito")
    print("3. Tarjeta de Crédito")
    opcion = int(input("Ingrese el número correspondiente al método de pago: "))

    if opcion == 1:
        monto_pagado = float(input("Ingrese el monto pagado en efectivo: "))
        pago = PagoEfectivo(monto=total)
        if monto_pagado >= total:
            vuelto = monto_pagado - total
            pago.monto = monto_pagado
            print(f"El vuelto es: {vuelto}")
        else:
            print("El monto pagado en efectivo es insuficiente.")
            return seleccionar_metodo_pago(total)
    elif opcion == 2:
        numero_tarjeta = input("Ingrese el número de la tarjeta de débito: ")
        pago = PagoDebito(monto=total, numero_tarjeta=numero_tarjeta)
    elif opcion == 3:
        numero_tarjeta = input("Ingrese el número de la tarjeta de crédito: ")
        numero_cuotas = int(input("Ingrese el número de cuotas: "))
        codigo_verificacion = input("Ingrese el código de verificación: ")
        pago = PagoCredito(monto=total, numero_tarjeta=numero_tarjeta, numero_cuotas=numero_cuotas, codigo_verificacion=codigo_verificacion)
    else:
        print("Opción no válida.")
        return seleccionar_metodo_pago(total)
    
    return pago

# Crear la factura
factura = Factura(
    numero=123,
    nit="5558955968",
    razon_social="Accesorios ",
    identificacion="1.007.639.609",
    cliente="Giselle Andrea Ulloa De La Rosa ",
    direccion="Cartagena , Bolivár",
    telefono="3004108200"
)

# Crear los detalles de la factura
detalle1 = Detalle(codigo="C001", descripcion="Arroz", valor_unidad=2000, unidad=2)
detalle2 = Detalle(codigo="C002", descripcion="Carne", valor_unidad=3000, unidad=4)
detalle3 = Detalle(codigo="C003", descripcion="Leche", valor_unidad=2500, unidad=2)

# Agregar los detalles a la factura
factura.agregar_detalle(detalle1)
factura.agregar_detalle(detalle2)
factura.agregar_detalle(detalle3)

# Aplicar un descuento del 10%
factura.aplicar_descuento(0.10)

# Agregar comentarios adicionales
factura.agregar_comentarios("Gracias por su compra.")

# Imprimir la factura
factura.imprimir_factura()

# Seleccionar el método de pago
total = factura.calcular_total()
pago = seleccionar_metodo_pago(total)
pago.mostrar_pago()
