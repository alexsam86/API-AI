from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    
    path('USUARIO/',usuario_api_view, name= 'usuario api'),
    path('USUARIO/<int:pk>/',usuario_detail_view, name = 'usuario api detalle' ),
    path('USUARIOC/<int:pk>/<str:contrasena>/', usuarioc, name='usuario_contrasena'),

    path('REGION/',region_api_view, name= 'region api'),
    path('REGION/<int:pk>/',region_detail_view, name = 'region api detalle' ),
    
    path('PROVINCIA/',provincia_api_view, name= 'provincia api'),
    path('PROVINCIA/<int:pk>/',provincia_detail_view, name = 'provincia api detalle' ),
    
    path('COMUNA/',comuna_api_view, name= 'comuna api'),
    path('COMUNA/<int:pk>/',comuna_detail_view, name = 'comuna api detalle' ),
    
    path('CLIENTE/',cliente_api_view, name= 'cliente api'),
    path('CLIENTE/<int:pk>/',cliente_detail_view, name = 'cliente api detalle' ),
    
    path('SUCURSAL/',sucursal_api_view, name= 'sucursal api'),
    path('SUCURSAL/<int:pk>/',sucursal_detail_view, name = 'sucursal api detalle' ),
    
    path('CATEGORIA/',categoria_api_view, name= 'categoria api'),
    path('CATEGORIA/<int:pk>/',categoria_detail_view, name = 'categoria api detalle' ),
    
    path('PROVEEDOR/',proveedor_api_view, name= 'proveedor api'),
    path('PROVEEDOR/<int:pk>/',proveedor_detail_view, name = 'proveedor api detalle' ),
    
    path('PRODUCTO/',producto_api_view, name= 'producto api'),
    path('PRODUCTO/<int:pk>/',producto_detail_view, name = 'producto api detalle' ),
    
    path('TIPO_EMPLEADO/',tipo_empleado_api_view, name= 'tipo empleado api'),
    path('TIPO_EMPLEADO/<int:pk>/',tipo_empleado_detail_view, name = 'tipo empleado api detalle' ),
    
    path('EMPLEADO/',empleado_api_view, name= 'empleado api'),
    path('EMPLEADO/<int:pk>/',empleado_detail_view, name = 'empleado api detalle' ),
    
    path('VENTA/',venta_api_view, name= 'venta api'),
    path('VENTA/<int:pk>/',venta_detail_view, name = 'venta api detalle' ),
    
    path('TIPO_EMISION/',tipo_emision_api_view, name= 'tipo emision api'),
    path('TIPO_EMISION/<int:pk>/',tipo_emision_detail_view, name = 'tipo emision api detalle' ),
    
    path('VENTA_DETALLE/',venta_detalle_api_view, name= 'venta detalle api'),
    path('VENTA_DETALLE/<int:pk>/',venta_detalle_detail_view, name = 'venta detalle api detalle' ),
    
    path('COURRIER/',courrier_api_view, name= 'courrier api'),
    path('COURRIER/<int:pk>/',courrier_detail_view, name = 'courrier api detalle' ),
    
    path('DESPACHO/',despacho_api_view, name= 'despacho api'),
    path('DESPACHO/<int:pk>/',despacho_detail_view, name = 'despacho api detalle' ),
    
    path('BODEGA/',bodega_api_view, name= 'bodega api'),
    path('BODEGA/<int:pk>/',bodega_detail_view, name = 'bodega api detalle' ),
    
    path('ESPACIOS/',espacios_api_view, name= 'espacios api'),
    path('ESPACIOS/<int:pk>/',espacios_detail_view, name = 'espacios api detalle' ),
    
    path('BODEGA_DETALLE/',bodega_detalle_api_view, name= 'bodega detalle api'),
    path('BODEGA_DETALLE/<int:pk>/',bodega_detalle_detail_view, name = 'bodega detalle api detalle' ),
    
    path('GUIA_DESPACHO/',guia_despacho_api_view, name= 'guia despacho api'),
    path('GUIA_DESPACHO/<int:pk>/',guia_despacho_detail_view, name = 'guia despacho api detalle' ),
    
    path('COMPRA/',compra_api_view, name= 'compra api'),
    path('COMPRA/<int:pk>/',compra_detail_view, name = 'compra api detalle' ),
    
    path('COMPRA_DETALLE/',compra_detalle_api_view, name= 'compra detalle api'),
    path('COMPRA_DETALLE/<int:pk>/',compra_detalle_detail_view, name = 'compra detalle api detalle' ), 
]


# from rest_framework.routers import DefaultRouter

# router_posts = DefaultRouter()

# router_posts.register(prefix='USUARIO',basename='USUARIO',viewset=USUARIOApiViewSet)
# router_posts.register(prefix='REGION',basename='REGION',viewset=REGIONViewSet)
# router_posts.register(prefix='PROVINCIA',basename='PROVINCIA',viewset=PROVINCIAViewSet)
# router_posts.register(prefix='COMUNA',basename='COMUNA',viewset=COMUNAViewSet)
# router_posts.register(prefix='CLIENTE',basename='CLIENTE',viewset=CLIENTEViewSet)
# router_posts.register(prefix='SUCURSAL',basename='SUCURSAL',viewset=SUCURSALViewSet)
# router_posts.register(prefix='CATEGORIA',basename='CATEGORIA',viewset=CATEGORIAViewSet)
# router_posts.register(prefix='PROVEEDOR',basename='PROVEEDOR',viewset=PROVEEDORViewSet)
# router_posts.register(prefix='PRODUCTO',basename='PRODUCTO',viewset=PRODUCTOViewSet)
# router_posts.register(prefix='TIPO_EMPLEADO',basename='TIPO_EMPLEADO',viewset=TIPO_EMPLEADOViewSet)
# router_posts.register(prefix='EMPLEADO',basename='EMPLEADO',viewset=EMPLEADOViewSet)
# router_posts.register(prefix='VENTA',basename='VENTA',viewset=VENTAViewSet)
# router_posts.register(prefix='TIPOEMISION',basename='TIPOEMISION',viewset=TIPOEMISIONViewSet)
# router_posts.register(prefix='VENTA_DETALLE',basename='VENTA_DETALLE',viewset=VENTA_DETALLEViewSet)
# router_posts.register(prefix='COURRIER',basename='COURRIER',viewset=COURRIERViewSet)
# router_posts.register(prefix='DESPACHO',basename='DESPACHO',viewset=DESPACHOViewSet)
# router_posts.register(prefix='BODEGA',basename='BODEGA',viewset=BODEGAViewSet)
# router_posts.register(prefix='ESPACIOS',basename='ESPACIOS',viewset=ESPACIOSViewSet)
# router_posts.register(prefix='BODEGA_DETALLE',basename='BODEGA_DETALLE',viewset=BODEGA_DETALLEViewSet)
# router_posts.register(prefix='GUIA_DESPACHO',basename='GUIA_DESPACHO',viewset=GUIA_DESPACHOViewSet)
# router_posts.register(prefix='COMPRA',basename='COMPRA',viewset=COMPRAViewSet)
# router_posts.register(prefix='COMPRA_DETALLE',basename='COMPRA_DETALLE',viewset=COMPRA_DETALLEViewSet)