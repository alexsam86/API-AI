from rest_framework.serializers import ModelSerializer
from Inicio.models import *

class USUARIOSerializer(ModelSerializer):
    class Meta:
        model=USUARIO
        fields=['id','nombreusuario','email','contrasena']
        
class REGIONSerializer(ModelSerializer):
    class Meta:
        model=REGION
        fields=['id','nombre']

class PROVINCIASerializer(ModelSerializer):
    class Meta:
        model=PROVINCIA
        fields=['id','nombre','id_region']

class COMUNASerializer(ModelSerializer):
    class Meta:
        model=COMUNA
        fields=['id','nombrecomuna', 'id_region']

class CLIENTESerializer(ModelSerializer):
    class Meta:
        model=CLIENTE
        fields=['id','nombrecliente', 'direccioncli', 'telefonocli', 'id_comuna','idusuario']

class SUCURSALSerializer(ModelSerializer):
    class Meta:
        model=SUCURSAL
        fields=['id','direccion', 'telefono', 'id_comuna']

class CATEGORIASerializer(ModelSerializer):
    class Meta:
        model=CATEGORIA
        fields=['id','nombre', 'descripcion']

class PROVEEDORSerializer(ModelSerializer):
    class Meta:
        model=PROVEEDOR
        fields=['id','nombreproveedor', 'direccion', 'telefono', 'email', 'id_comuna']

class PRODUCTOSerializer(ModelSerializer):
    class Meta:
        model=PRODUCTO
        fields=['id','nombreproducto', 'descripcion', 'id_categoria', 'id_proveedor', 'precio']

class TIPO_EMPLEADOSerializer(ModelSerializer):
    class Meta:
        model=TIPO_EMPLEADO
        fields=['id','cargo']

class EMPLEADOSerializer(ModelSerializer):
    class Meta:
        model=EMPLEADO
        fields=['id','rutempleado', 'rutdv','nombreempleado', 'apellidoempleado', 'id_tipo', 'fechacontrato', 'id_sucursal', 'sueldo','idusuario']

class VENTASerializer(ModelSerializer):
    class Meta:
        model=VENTA
        fields=['id','id_cliente','fecha', 'total', 'id_empleado']
        
class TIPOEMISIONSerializer(ModelSerializer):
    class Meta:
        model=TIPOEMISION
        fields=['id','tipoemision']

class VENTA_DETALLESerializer(ModelSerializer):
    class Meta:
        model=VENTA_DETALLE
        fields=['id','id_venta','id_producto', 'cantidad', 'precio', 'total','id_tipoemision']

class COURRIERSerializer(ModelSerializer):
    class Meta:
        model=COURRIER
        fields=['id','nombrecourrier']

class DESPACHOSerializer(ModelSerializer):
    class Meta:
        model=DESPACHO
        fields=['id','id_cliente', 'id_venta', 'id_comuna', 'direcciondespacho', 'id_courrier']

class BODEGASerializer(ModelSerializer):
    class Meta:
        model=BODEGA
        fields=['id','direccion', 'id_comuna', 'cantidadespacio']

class ESPACIOSSerializer(ModelSerializer):
    class Meta:
        model=ESPACIOS
        fields=['id','nombre']

class BODEGA_DETALLESerializer(ModelSerializer):
    class Meta:
        model=BODEGA_DETALLE
        fields=['id','id_bodega', 'id_producto', 'stock', 'espacio']


class GUIA_DESPACHOSerializer(ModelSerializer):
    class Meta:
        model=GUIA_DESPACHO
        fields=['id','fecha', 'tipo', 'id_producto', 'cantidad', 'id_bodega', 'detalle']


class COMPRASerializer(ModelSerializer):
    class Meta:
        model=COMPRA
        fields=['id','id_proveedor', 'fecha', 'total', 'id_empleado']


class COMPRA_DETALLESerializer(ModelSerializer):
    class Meta:
        model=COMPRA_DETALLE
        fields=['id','id_compra', 'id_producto', 'cantidad', 'precio', 'id_guiadp']

