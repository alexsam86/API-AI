from Inicio.models import *
from django.shortcuts import render
from Inicio.api.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
import bcrypt

def home(request):
    return render(request,'home.html')

# ------------------------------------------------------------------------
@api_view(['GET','POST'])
def usuario_api_view(request):
    if request.method == 'GET':
        usuarios = USUARIO.objects.all()
        usuarios_serializer = USUARIOSerializer(usuarios,many = True)
        return Response(usuarios_serializer.data)
    elif request.method == 'POST':
        usuarios_serializer = USUARIOSerializer(data = request.data)
        raw_password = request.data.get('contrasena')
        hashed_password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())
        request.data['contrasena'] = hashed_password.decode('utf-8')
        if usuarios_serializer.is_valid():
            usuarios_serializer.save()
            return Response(usuarios_serializer.data)
        return Response(usuarios_serializer.errors)
    else:
        return Response('Metodo no permitido') 
@api_view(['GET','PUT','DELETE'])
def usuario_detail_view(request,pk=None):
    if request.method == 'GET':
        usuarios = USUARIO.objects.filter(id = pk).first()
        usuarios_serializer =  USUARIOSerializer(usuarios)
        return Response(usuarios_serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
            usuario = USUARIO.objects.filter(id = pk).first()
            raw_password = request.data.get('contrasena')
            hashed_password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())
            request.data['contrasena'] = hashed_password.decode('utf-8')
            usuario_serializar = USUARIOSerializer(usuario,data = request.data)
            if usuario_serializar.is_valid():
                usuario_serializar.save()
                return Response(usuario_serializar.errors)
    elif request.method == 'DELETE':
        usuario = USUARIO.objects.filter(id = pk).first()
        usuario.delete()
        return Response('Eliminado')
    else:
        return Response('Metodo no permitido')
@api_view(['GET'])
def usuarioc(request, pk, contrasena):
    if request.method == 'GET':
        usuario = USUARIO.objects.filter(id=pk).first()
        is_password_correct = bcrypt.checkpw(contrasena.encode('utf-8'), usuario.contrasena.encode('utf-8'))
        response_data = {
            'id': usuario.id,
            'nombreusuario': usuario.nombreusuario,
            'email': usuario.email,
            'contrasena': is_password_correct,
        }
        return Response(response_data)
    else:
        return Response('Metodo no permitido')

# ------------------------------------------------------------------------
@api_view(['GET'])
def region_api_view(request):
    if request.method == 'GET':
        regiones = REGION.objects.all()
        regiones_serializer = REGIONSerializer(regiones,many = True)
        return Response(regiones_serializer.data)
    else:
        return Response('Metodo no permitido')

@api_view(['GET'])
def region_detail_view(request,pk=None):
    if request.method == 'GET':
        regiones = REGION.objects.filter(id = pk).first()
        regiones_serializer = REGIONSerializer(regiones)
        return Response(regiones_serializer.data)
    else:
        return Response('Metodo no permitido')
    
# ------------------------------------------------------------------------
@api_view(['GET'])
def provincia_api_view(request):
    if request.method == 'GET':
        provincias = PROVINCIA.objects.all()
        provincias_serializer = REGIONSerializer(provincias,many = True)
        return Response(provincias_serializer.data)
    else:
        return Response('Metodo no permitido')

@api_view(['GET'])
def provincia_detail_view(request,pk=None):
    if request.method == 'GET':
        provincias = PROVINCIA.objects.filter(id = pk).first()
        provincias_serializer = REGIONSerializer(provincias)
        return Response(provincias_serializer.data)
    else:
        return Response('Metodo no permitido')
    
# ------------------------------------------------------------------------
@api_view(['GET'])
def comuna_api_view(request):
    if request.method == 'GET':
        comunas = COMUNA.objects.all()
        comunas_serializer = COMUNASerializer(comunas,many = True)
        return Response(comunas_serializer.data)
    else:
        return Response('Metodo no permitido')
@api_view(['GET'])
def comuna_detail_view(request,pk=None):
    if request.method == 'GET':
        comunas = COMUNA.objects.filter(id = pk).first()
        comunas_serializer = COMUNASerializer(comunas)
        return Response(comunas_serializer.data)
    else:
        return Response('Metodo no permitido')

# ------------------------------------------------------------------------
@api_view(['GET','POST'])
def cliente_api_view(request):
    if request.method == 'GET':
        clientes = CLIENTE.objects.all()
        clientes_serializer = CLIENTESerializer(clientes,many = True)
        return Response(clientes_serializer.data)
    elif request.method == 'POST':
        clientes_serializer = CLIENTESerializer(data = request.data)
        if clientes_serializer.is_valid():
            clientes_serializer.save()
            return Response(clientes_serializer.data)
        return Response(clientes_serializer.errors)
    else:
        return Response('Metodo no permitido') 
@api_view(['GET','PUT','DELETE'])
def cliente_detail_view(request,pk=None):
    if request.method == 'GET':
        clientes = CLIENTE.objects.filter(id = pk).first()
        clientes_serializer = CLIENTESerializer(clientes)
        return Response(clientes_serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
            cliente = CLIENTE.objects.filter(id = pk).first()
            cliente_serializar = CLIENTESerializer(cliente,data = request.data)
            if cliente_serializar.is_valid():
                cliente_serializar.save()
                return Response(cliente_serializar.errors)
    elif request.method == 'DELETE':
        cliente = CLIENTE.objects.filter(id = pk).first()
        cliente.delete()
        return Response('Eliminado')
    else:
        return Response('Metodo no permitido')

# ------------------------------------------------------------------------
@api_view(['GET','POST'])
def sucursal_api_view(request):
    if request.method == 'GET':
        sucursales = SUCURSAL.objects.all()
        sucursales_serializer = SUCURSALSerializer(sucursales,many = True)
        return Response(sucursales_serializer.data)
    elif request.method == 'POST':
        sucursales_serializer = SUCURSALSerializer(data = request.data)
        if sucursales_serializer.is_valid():
            sucursales_serializer.save()
            return Response(sucursales_serializer.data)
        return Response(sucursales_serializer.errors)
    else:
        return Response('Metodo no permitido') 
@api_view(['GET','DELETE'])
def sucursal_detail_view(request,pk=None):
    if request.method == 'GET':
        sucursales = SUCURSAL.objects.filter(id = pk).first()
        sucursales_serializer = SUCURSALSerializer(sucursales)
        return Response(sucursales_serializer.data)
    elif request.method == 'DELETE':
        sucursal = SUCURSAL.objects.filter(id = pk).first()
        sucursal.delete()
        return Response('Eliminado')
    else:
        return Response('Metodo no permitido')

# ------------------------------------------------------------------------
@api_view(['GET','POST'])
def categoria_api_view(request):
    if request.method == 'GET':
        categorias = CATEGORIA.objects.all()
        categorias_serializer = CATEGORIASerializer(categorias,many = True)
        return Response(categorias_serializer.data)
    elif request.method == 'POST':
        categorias_serializer = CATEGORIASerializer(data = request.data)
        if categorias_serializer.is_valid():
            categorias_serializer.save()
            return Response(categorias_serializer.data)
        return Response(categorias_serializer.errors)
    else:
        return Response('Metodo no permitido') 
@api_view(['GET','PUT','DELETE'])
def categoria_detail_view(request,pk=None):
    if request.method == 'GET':
        categorias = CATEGORIA.objects.filter(id = pk).first()
        categorias_serializer = CATEGORIASerializer(categorias)
        return Response(categorias_serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
            categoria = CATEGORIA.objects.filter(id = pk).first()
            categoria_serializar = CATEGORIASerializer(categoria,data = request.data)
            if categoria_serializar.is_valid():
                categoria_serializar.save()
                return Response(categoria_serializar.errors)
    elif request.method == 'DELETE':
        categoria = CATEGORIA.objects.filter(id = pk).first()
        categoria.delete()
        return Response('Eliminado')
    else:
        return Response('Metodo no permitido')

# ------------------------------------------------------------------------
@api_view(['GET','POST'])
def proveedor_api_view(request):
    if request.method == 'GET':
        proveedores = PROVEEDOR.objects.all()
        proveedores_serializer = PROVEEDORSerializer(proveedores,many = True)
        return Response(proveedores_serializer.data)
    elif request.method == 'POST':
        proveedores_serializer = PROVEEDORSerializer(data = request.data)
        if proveedores_serializer.is_valid():
            proveedores_serializer.save()
            return Response(proveedores_serializer.data)
        return Response(proveedores_serializer.errors)
    else:
        return Response('Metodo no permitido') 
@api_view(['GET','DELETE'])
def proveedor_detail_view(request,pk=None):
    if request.method == 'GET':
        proveedores = PROVEEDOR.objects.filter(id = pk).first()
        proveedores_serializer = PROVEEDORSerializer(proveedores)
        return Response(proveedores_serializer.data)
    elif request.method == 'DELETE':
        proveedor = PROVEEDOR.objects.filter(id = pk).first()
        proveedor.delete()
        return Response('Eliminado')
    else:
        return Response('Metodo no permitido')

# ------------------------------------------------------------------------
@api_view(['GET','POST'])
def producto_api_view(request):
    if request.method == 'GET':
        productos = PRODUCTO.objects.all()
        productos_serializer = PRODUCTOSerializer(productos,many = True)
        return Response(productos_serializer.data)
    elif request.method == 'POST':
        productos_serializer = PRODUCTOSerializer(data = request.data)
        if productos_serializer.is_valid():
            productos_serializer.save()
            return Response(productos_serializer.data)
        return Response(productos_serializer.errors)
    else:
        return Response('Metodo no permitido') 
@api_view(['GET'])
def producto_detail_view(request,pk=None):
    if request.method == 'GET':
        productos = PRODUCTO.objects.filter(id = pk).first()
        productos_serializer = PRODUCTOSerializer(productos)
        return Response(productos_serializer.data)
    else:
        return Response('Metodo no permitido')

# ------------------------------------------------------------------------
@api_view(['GET'])
def tipo_empleado_api_view(request):
    if request.method == 'GET':
        tipo_empleados = TIPO_EMPLEADO.objects.all()
        tipo_empleados_serializer = TIPO_EMPLEADOSerializer(tipo_empleados,many = True)
        return Response(tipo_empleados_serializer.data)
    else:
        return Response('Metodo no permitido') 
@api_view(['GET'])
def tipo_empleado_detail_view(request,pk=None):
    if request.method == 'GET':
        tipo_empleados = TIPO_EMPLEADO.objects.filter(id = pk).first()
        tipo_empleados_serializer = TIPO_EMPLEADOSerializer(tipo_empleados)
        return Response(tipo_empleados_serializer.data)
    else:
        return Response('Metodo no permitido')

# ------------------------------------------------------------------------
@api_view(['GET','POST'])
def empleado_api_view(request):
    if request.method == 'GET':
        empleados = EMPLEADO.objects.all()
        empleados_serializer = EMPLEADOSerializer(empleados,many = True)
        return Response(empleados_serializer.data)
    elif request.method == 'POST':
        empleados_serializer = EMPLEADOSerializer(data = request.data)
        if empleados_serializer.is_valid():
            empleados_serializer.save()
            return Response(empleados_serializer.data)
        return Response(empleados_serializer.errors)
    else:
        return Response('Metodo no permitido') 
@api_view(['GET','DELETE'])
def empleado_detail_view(request,pk=None):
    if request.method == 'GET':
        empleados = EMPLEADO.objects.filter(id = pk).first()
        empleados_serializer = EMPLEADOSerializer(empleados)
        return Response(empleados_serializer.data)
    elif request.method == 'DELETE':
        empleado = EMPLEADO.objects.filter(id = pk).first()
        empleado.delete()
        return Response('Eliminado')
    else:
        return Response('Metodo no permitido')

# ------------------------------------------------------------------------
@api_view(['GET','POST'])
def venta_api_view(request):
    if request.method == 'GET':
        ventas = VENTA.objects.all()
        ventas_serializer = VENTASerializer(ventas,many = True)
        return Response(ventas_serializer.data)
    elif request.method == 'POST':
        ventas_serializer = VENTASerializer(data = request.data)
        if ventas_serializer.is_valid():
            ventas_serializer.save()
            return Response(ventas_serializer.data)
        return Response(ventas_serializer.errors)
    else:
        return Response('Metodo no permitido') 
@api_view(['GET'])
def venta_detail_view(request,pk=None):
    if request.method == 'GET':
        ventas = VENTA.objects.filter(id = pk).first()
        ventas_serializer = VENTASerializer(ventas)
        return Response(ventas_serializer.data)
    else:
        return Response('Metodo no permitido')

# ------------------------------------------------------------------------
@api_view(['GET'])
def tipo_emision_api_view(request):
    if request.method == 'GET':
        tipoemisions = TIPOEMISION.objects.all()
        tipoemisions_serializer = TIPOEMISIONSerializer(tipoemisions,many = True)
        return Response(tipoemisions_serializer.data)
    else:
        return Response('Metodo no permitido') 
@api_view(['GET'])
def tipo_emision_detail_view(request,pk=None):
    if request.method == 'GET':
        tipoemisions = TIPOEMISION.objects.filter(id = pk).first()
        tipoemisions_serializer = TIPOEMISIONSerializer(tipoemisions)
        return Response(tipoemisions_serializer.data)
    else:
        return Response('Metodo no permitido')

# ------------------------------------------------------------------------
@api_view(['GET','POST'])
def venta_detalle_api_view(request):
    if request.method == 'GET':
        venta_detalles = VENTA_DETALLE.objects.all()
        venta_detalles_serializer = VENTA_DETALLESerializer(venta_detalles,many = True)
        return Response(venta_detalles_serializer.data)
    elif request.method == 'POST':
        venta_detalles_serializer = VENTA_DETALLESerializer(data = request.data)
        if venta_detalles_serializer.is_valid():
            venta_detalles_serializer.save()
            return Response(venta_detalles_serializer.data)
        return Response(venta_detalles_serializer.errors)
    else:
        return Response('Metodo no permitido') 
@api_view(['GET'])
def venta_detalle_detail_view(request,pk=None):
    if request.method == 'GET':
        venta_detalles = VENTA_DETALLE.objects.filter(id = pk).first()
        venta_detalles_serializer = VENTA_DETALLESerializer(venta_detalles)
        return Response(venta_detalles_serializer.data)
    else:
        return Response('Metodo no permitido')

# ------------------------------------------------------------------------
@api_view(['GET','POST'])
def courrier_api_view(request):
    if request.method == 'GET':
        courriers = COURRIER.objects.all()
        courriers_serializer = COURRIERSerializer(courriers,many = True)
        return Response(courriers_serializer.data)
    elif request.method == 'POST':
        courriers_serializer = COURRIERSerializer(data = request.data)
        if courriers_serializer.is_valid():
            courriers_serializer.save()
            return Response(courriers_serializer.data)
        return Response(courriers_serializer.errors)
    else:
        return Response('Metodo no permitido') 
@api_view(['GET','DELETE'])
def courrier_detail_view(request,pk=None):
    if request.method == 'GET':
        courriers = COURRIER.objects.filter(id = pk).first()
        courriers_serializer = COURRIERSerializer(courriers)
        return Response(courriers_serializer.data)
    elif request.method == 'DELETE':
        courrier = COURRIER.objects.filter(id = pk).first()
        courrier.delete()
        return Response('Eliminado')
    else:
        return Response('Metodo no permitido')

# ------------------------------------------------------------------------
@api_view(['GET','POST'])
def despacho_api_view(request):
    if request.method == 'GET':
        despachos = DESPACHO.objects.all()
        despachos_serializer = DESPACHOSerializer(despachos,many = True)
        return Response(despachos_serializer.data)
    elif request.method == 'POST':
        despachos_serializer = DESPACHOSerializer(data = request.data)
        if despachos_serializer.is_valid():
            despachos_serializer.save()
            return Response(despachos_serializer.data)
        return Response(despachos_serializer.errors)
    else:
        return Response('Metodo no permitido') 
@api_view(['GET','PUT'])
def despacho_detail_view(request,pk=None):
    if request.method == 'GET':
        despachos= DESPACHO.objects.filter(id = pk).first()
        despachos_serializer = DESPACHOSerializer(despachos)
        return Response(despachos_serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
            despacho = DESPACHO.objects.filter(id = pk).first()
            despacho_serializar = DESPACHOSerializer(despacho,data = request.data)
            if despacho_serializar.is_valid():
                despacho_serializar.save()
                return Response(despacho_serializar.errors)
    else:
        return Response('Metodo no permitido')

# ------------------------------------------------------------------------
@api_view(['GET','POST'])
def bodega_api_view(request):
    if request.method == 'GET':
        bodegas = BODEGA.objects.all()
        bodegas_serializer = BODEGASerializer(bodegas,many = True)
        return Response(bodegas_serializer.data)
    elif request.method == 'POST':
        bodegas_serializer = BODEGASerializer(data = request.data)
        if bodegas_serializer.is_valid():
            bodegas_serializer.save()
            return Response(bodegas_serializer.data)
        return Response(bodegas_serializer.errors)
    else:
        return Response('Metodo no permitido') 
@api_view(['GET'])
def bodega_detail_view(request,pk=None):
    if request.method == 'GET':
        bodegas = BODEGA.objects.filter(id = pk).first()
        bodegas_serializer = BODEGASerializer(bodegas)
        return Response(bodegas_serializer.data)
    else:
        return Response('Metodo no permitido')

# ------------------------------------------------------------------------
@api_view(['GET','POST'])
def espacios_api_view(request):
    if request.method == 'GET':
        espacioss = ESPACIOS.objects.all()
        espacioss_serializer = ESPACIOSSerializer(espacioss,many = True)
        return Response(espacioss_serializer.data)
    elif request.method == 'POST':
        espacioss_serializer = ESPACIOSSerializer(data = request.data)
        if espacioss_serializer.is_valid():
            espacioss_serializer.save()
            return Response(espacioss_serializer.data)
        return Response(espacioss_serializer.errors)
    else:
        return Response('Metodo no permitido') 
@api_view(['GET','DELETE'])
def espacios_detail_view(request,pk=None):
    if request.method == 'GET':
        espacioss = ESPACIOS.objects.filter(id = pk).first()
        espacioss_serializer = ESPACIOSSerializer(espacioss)
        return Response(espacioss_serializer.data)
    elif request.method == 'DELETE':
        espacios = ESPACIOS.objects.filter(id = pk).first()
        espacios.delete()
        return Response('Eliminado')
    else:
        return Response('Metodo no permitido')

# ------------------------------------------------------------------------
@api_view(['GET','POST'])
def bodega_detalle_api_view(request):
    if request.method == 'GET':
        bodega_detalles = BODEGA_DETALLE.objects.all()
        bodega_detalles_serializer = BODEGA_DETALLESerializer(bodega_detalles,many = True)
        return Response(bodega_detalles_serializer.data)
    elif request.method == 'POST':
        bodega_detalles_serializer = BODEGA_DETALLESerializer(data = request.data)
        if bodega_detalles_serializer.is_valid():
            bodega_detalles_serializer.save()
            return Response(bodega_detalles_serializer.data)
        return Response(bodega_detalles_serializer.errors)
    else:
        return Response('Metodo no permitido') 
@api_view(['GET','PUT','DELETE'])
def bodega_detalle_detail_view(request,pk=None):
    if request.method == 'GET':
        bodega_detalles = BODEGA_DETALLE.objects.filter(id = pk).first()
        bodega_detalles_serializer = BODEGA_DETALLESerializer(bodega_detalles)
        return Response(bodega_detalles_serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
            bodega_detalle = BODEGA_DETALLE.objects.filter(id = pk).first()
            bodega_detalle_serializar = BODEGA_DETALLESerializer(bodega_detalle,data = request.data)
            if bodega_detalle_serializar.is_valid():
                bodega_detalle_serializar.save()
                return Response(bodega_detalle_serializar.errors)
    elif request.method == 'DELETE':
        bodega_detalle = BODEGA_DETALLE.objects.filter(id = pk).first()
        bodega_detalle.delete()
        return Response('Eliminado')
    else:
        return Response('Metodo no permitido')

# ------------------------------------------------------------------------
@api_view(['GET','POST'])
def guia_despacho_api_view(request):
    if request.method == 'GET':
        guia_despachos = GUIA_DESPACHO.objects.all()
        guia_despachos_serializer = GUIA_DESPACHOSerializer(guia_despachos,many = True)
        return Response(guia_despachos_serializer.data)
    elif request.method == 'POST':
        guia_despachos_serializer = GUIA_DESPACHOSerializer(data = request.data)
        if guia_despachos_serializer.is_valid():
            guia_despachos_serializer.save()
            return Response(guia_despachos_serializer.data)
        return Response(guia_despachos_serializer.errors)
    else:
        return Response('Metodo no permitido') 
@api_view(['GET'])
def guia_despacho_detail_view(request,pk=None):
    if request.method == 'GET':
        guia_despachos = GUIA_DESPACHO.objects.filter(id = pk).first()
        guia_despachos_serializer = GUIA_DESPACHOSerializer(guia_despachos)
        return Response(guia_despachos_serializer.data)
    else:
        return Response('Metodo no permitido')

# ------------------------------------------------------------------------
@api_view(['GET','POST'])
def compra_api_view(request):
    if request.method == 'GET':
        compras = COMPRA.objects.all()
        compras_serializer = COMPRASerializer(compras,many = True)
        return Response(compras_serializer.data)
    elif request.method == 'POST':
        compras_serializer = COMPRASerializer(data = request.data)
        if compras_serializer.is_valid():
            compras_serializer.save()
            return Response(compras_serializer.data)
        return Response(compras_serializer.errors)
    else:
        return Response('Metodo no permitido') 
@api_view(['GET','PUT'])
def compra_detail_view(request,pk=None):
    if request.method == 'GET':
        compras = COMPRA.objects.filter(id = pk).first()
        compras_serializer = COMPRASerializer(compras)
        return Response(compras_serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
            compra = COMPRA.objects.filter(id = pk).first()
            compra_serializar = COMPRASerializer(compra,data = request.data)
            if compra_serializar.is_valid():
                compra_serializar.save()
                return Response(compra_serializar.errors)
    else:
        return Response('Metodo no permitido')

# ------------------------------------------------------------------------
@api_view(['GET','POST'])
def compra_detalle_api_view(request):
    if request.method == 'GET':
        compra_detalles = COMPRA_DETALLE.objects.all()
        compra_detales_serializer = COMPRA_DETALLESerializer(compra_detalles,many = True)
        return Response(compra_detales_serializer.data)
    elif request.method == 'POST':
        compra_detalles_serializer = COMPRA_DETALLESerializer(data = request.data)
        if compra_detalles_serializer.is_valid():
            compra_detalles_serializer.save()
            return Response(compra_detalles_serializer.data)
        return Response(compra_detalles_serializer.errors)
    else:
        return Response('Metodo no permitido') 
@api_view(['GET','PUT','DELETE'])
def compra_detalle_detail_view(request,pk=None):
    if request.method == 'GET':
        compra_detalles = COMPRA_DETALLE.objects.filter(id = pk).first()
        compra_detalles_serializer = COMPRA_DETALLESerializer(compra_detalles)
        return Response(compra_detalles_serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
            compra_detalle = COMPRA_DETALLE.objects.filter(id = pk).first()
            compra_detalle_serializar = COMPRA_DETALLESerializer(compra_detalles,data = request.data)
            if compra_detalle_serializar.is_valid():
                compra_detalle_serializar.save()
                return Response(compra_detalle_serializar.errors)
    elif request.method == 'DELETE':
        compra_detalle = COMPRA_DETALLE.objects.filter(id = pk).first()
        compra_detalle.delete()
        return Response('Eliminado')
    else:
        return Response('Metodo no permitido')

# ------------------------------------------------------------------------

# from rest_framework.viewsets import ModelViewSet

# class USUARIOApiViewSet(ModelViewSet):
#     serializer_class=USUARIOSerializer
#     queryset=USUARIO.objects.all()

# class REGIONViewSet(ModelViewSet):
#     serializer_class=REGIONSerializer
#     queryset=REGION.objects.all()
    
# class PROVINCIAViewSet(ModelViewSet):
#     serializer_class=PROVINCIASerializer
#     queryset=PROVINCIA.objects.all()
    
# class COMUNAViewSet(ModelViewSet):
#     serializer_class=COMUNASerializer
#     queryset=COMUNA.objects.all()
    
# class CLIENTEViewSet(ModelViewSet):
#     serializer_class=CLIENTESerializer
#     queryset=CLIENTE.objects.all()
    
# class SUCURSALViewSet(ModelViewSet):
#     serializer_class=SUCURSALSerializer
#     queryset=SUCURSAL.objects.all()
    
# class CATEGORIAViewSet(ModelViewSet):
#     serializer_class=CATEGORIASerializer
#     queryset=CATEGORIA.objects.all()
    
# class PROVEEDORViewSet(ModelViewSet):
#     serializer_class=PROVEEDORSerializer
#     queryset=PROVEEDOR.objects.all()
    
# class PRODUCTOViewSet(ModelViewSet):
#     serializer_class=PRODUCTOSerializer
#     queryset=PRODUCTO.objects.all()
    
# class TIPO_EMPLEADOViewSet(ModelViewSet):
#     serializer_class=TIPO_EMPLEADOSerializer
#     queryset=TIPO_EMPLEADO.objects.all()
    
# class EMPLEADOViewSet(ModelViewSet):
#     serializer_class=EMPLEADOSerializer
#     queryset=EMPLEADO.objects.all()
    
# class VENTAViewSet(ModelViewSet):
#     serializer_class=VENTASerializer
#     queryset=VENTA.objects.all()

# class TIPOEMISIONViewSet(ModelViewSet):
#     serializer_class=TIPOEMISIONSerializer
#     queryset=TIPOEMISION.objects.all()
    
# class VENTA_DETALLEViewSet(ModelViewSet):
#     serializer_class=VENTA_DETALLESerializer
#     queryset=VENTA_DETALLE.objects.all()
    
# class COURRIERViewSet(ModelViewSet):
#     serializer_class=COURRIERSerializer
#     queryset=COURRIER.objects.all()
    
# class DESPACHOViewSet(ModelViewSet):
#     serializer_class=DESPACHOSerializer
#     queryset=DESPACHO.objects.all()
    
# class BODEGAViewSet(ModelViewSet):
#     serializer_class=BODEGASerializer
#     queryset=BODEGA.objects.all()
    
# class ESPACIOSViewSet(ModelViewSet):
#     serializer_class=ESPACIOSSerializer
#     queryset=ESPACIOS.objects.all()
    
# class BODEGA_DETALLEViewSet(ModelViewSet):
#     serializer_class=BODEGA_DETALLESerializer
#     queryset=BODEGA_DETALLE.objects.all()
    
# class GUIA_DESPACHOViewSet(ModelViewSet):
#     serializer_class=GUIA_DESPACHOSerializer
#     queryset=GUIA_DESPACHO.objects.all()
    
# class COMPRAViewSet(ModelViewSet):
#     serializer_class=COMPRASerializer
#     queryset=COMPRA.objects.all()
    
# class COMPRA_DETALLEViewSet(ModelViewSet):
#     serializer_class=COMPRA_DETALLESerializer
#     queryset=COMPRA_DETALLE.objects.all()