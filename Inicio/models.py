from django.db import models

class USUARIO(models.Model):
    nombreusuario = models.CharField(max_length=100)
    email = models.EmailField()
    contrasena = models.CharField(max_length=100)
    def __str__(self):
        return self.nombreusuario
    
class REGION(models.Model):
     nombre=models.CharField(max_length=50)
     def __str__(self):
        return self.nombre
     
class PROVINCIA(models.Model):
     nombre=models.CharField(max_length=50)
     id_region=models.ForeignKey(REGION, on_delete=models.CASCADE)
     def __str__(self):
        return self.nombre
class COMUNA(models.Model):
     nombrecomuna=models.CharField(max_length=50)
     id_region=models.ForeignKey(PROVINCIA, on_delete=models.CASCADE)
     def __str__(self):
        return self.nombrecomuna
   
class CLIENTE(models.Model):
     nombrecliente=models.CharField(max_length=50)
     direccioncli=models.CharField(max_length=50)
     telefonocli=models.CharField(max_length=50)
     id_comuna=models.ForeignKey(COMUNA, on_delete=models.CASCADE)
     idusuario=models.ForeignKey(USUARIO,on_delete=models.CASCADE)
     def __str__(self):
        return self.nombrecliente
     
class SUCURSAL(models.Model):
     direccion=models.CharField(max_length=50)
     telefono=models.CharField(max_length=50)
     id_comuna=models.ForeignKey(COMUNA, on_delete=models.CASCADE)
     def __str__(self):
        return self.id_comuna.nombrecomuna
     
class CATEGORIA(models.Model):
     nombre=models.CharField(max_length=50)
     descripcion=models.CharField(max_length=150)
     def __str__(self):
        return self.nombre
     
class PROVEEDOR(models.Model):
     nombreproveedor=models.CharField(max_length=50)
     direccion=models.CharField(max_length=50)
     telefono=models.CharField(max_length=50)
     email=models.CharField(max_length=50)
     id_comuna=models.ForeignKey(COMUNA, on_delete=models.CASCADE)
     def __str__(self):
        return self.nombreproveedor
   
class PRODUCTO(models.Model):
     nombreproducto=models.CharField(max_length=50)
     descripcion=models.CharField(max_length=150)
     id_categoria=models.ForeignKey(CATEGORIA, on_delete=models.CASCADE)
     id_proveedor=models.ForeignKey(PROVEEDOR, on_delete=models.CASCADE)
     precio=models.IntegerField()
     def __str__(self):
        return self.nombreproducto
     
class TIPO_EMPLEADO(models.Model):
     cargo=models.CharField(max_length=50)
     def __str__(self):
        return self.cargo
     
class EMPLEADO(models.Model):
     rutempleado=models.CharField(max_length=14)
     rutdv=models.CharField(max_length=1)
     nombreempleado=models.CharField(max_length=50)
     apellidoempleado=models.CharField(max_length=50)
     id_tipo=models.ForeignKey(TIPO_EMPLEADO, on_delete=models.CASCADE)
     fechacontrato=models.DateField()
     id_sucursal=models.ForeignKey(SUCURSAL, on_delete=models.CASCADE)
     sueldo=models.IntegerField()
     idusuario=models.ForeignKey(USUARIO,on_delete=models.CASCADE)
     def __str__(self):
        return f"{self.nombreempleado} {self.apellidoempleado}"
     
class VENTA(models.Model):
     id_cliente=models.ForeignKey(CLIENTE, on_delete=models.CASCADE)
     fecha=models.DateField()
     total=models.IntegerField()
     id_empleado=models.ForeignKey(EMPLEADO, on_delete=models.CASCADE)
     def __str__(self):
        return f"{self.id_cliente} {self.id}"
     
class TIPOEMISION(models.Model):
     tipoemision=models.CharField(max_length=50)
     def __str__(self):
        return self.tipoemision
     
class VENTA_DETALLE(models.Model):
     id_venta=models.ForeignKey(VENTA, on_delete=models.CASCADE)
     id_producto=models.ForeignKey(PRODUCTO, on_delete=models.CASCADE)
     cantidad=models.IntegerField()
     precio=models.IntegerField()
     total=models.IntegerField()
     id_tipoemision=models.ForeignKey(TIPOEMISION, on_delete=models.CASCADE)
     def __str__(self):
        return f"{self.id_venta} {self.id_producto.nombreproducto}"
     
class COURRIER(models.Model):
     nombrecourrier=models.CharField(max_length=50)
     def __str__(self):
        return self.nombrecourrier
     
class DESPACHO(models.Model):
     id_cliente=models.ForeignKey(CLIENTE, on_delete=models.CASCADE)
     id_venta=models.ForeignKey(VENTA, on_delete=models.CASCADE)
     id_comuna=models.ForeignKey(COMUNA, on_delete=models.CASCADE)
     direcciondespacho=models.CharField(max_length=50)
     id_courrier=models.ForeignKey(COURRIER, on_delete=models.CASCADE)
     def __str__(self):
        return self.id_cliente.nombrecliente
     
class BODEGA(models.Model):
     direccion=models.CharField(max_length=50)
     id_comuna=models.ForeignKey(COMUNA, on_delete=models.CASCADE)
     cantidadespacio=models.IntegerField()
     def __str__(self):
        return f"{self.id_comuna.nombrecomuna} {self.direccion}"

class ESPACIOS(models.Model):
     nombre=models.CharField(max_length=50)
     def __str__(self):
        return self.nombre
     
class BODEGA_DETALLE(models.Model):
     id_bodega=models.ForeignKey(BODEGA, on_delete=models.CASCADE)
     id_producto=models.ForeignKey(PRODUCTO, on_delete=models.CASCADE)
     stock=models.IntegerField()
     espacio=models.ForeignKey(ESPACIOS, on_delete=models.CASCADE)
     def __str__(self):
        return f"{self.id_bodega} {self.id_producto.nombreproducto}"
     
class GUIA_DESPACHO(models.Model):
     fecha=models.DateField()
     tipo=models.IntegerField()
     id_producto=models.ForeignKey(PRODUCTO, on_delete=models.CASCADE)
     cantidad=models.IntegerField()
     id_bodega=models.ForeignKey(BODEGA, on_delete=models.CASCADE)
     detalle=models.CharField(max_length=50)
     def __str__(self):
        return self.id
     
class COMPRA(models.Model):
     id_proveedor=models.ForeignKey(PROVEEDOR, on_delete=models.CASCADE)
     fecha=models.DateField()
     total=models.IntegerField()
     id_empleado=models.ForeignKey(EMPLEADO, on_delete=models.CASCADE)
     def __str__(self):
        return self.id

class COMPRA_DETALLE(models.Model):
     id_compra=models.ForeignKey(COMPRA, on_delete=models.CASCADE)
     id_producto=models.ForeignKey(PRODUCTO, on_delete=models.CASCADE)
     cantidad=models.IntegerField()
     precio=models.IntegerField()
     id_guiadp=models.ForeignKey(GUIA_DESPACHO, on_delete=models.CASCADE)
     def __str__(self):
        return f"{self.id_compra} {self.id_producto.nombreproducto}"
     
