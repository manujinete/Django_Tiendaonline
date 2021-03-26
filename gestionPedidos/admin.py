from django.contrib import admin

from gestionPedidos.models import Clientes, Articulos, Pedidos

# Register your models here.

#Permite hacer modificaciones de visualización desde el Panel en Clientes.

class ClientesAdmin(admin.ModelAdmin):
    list_display=('nombre', 'direccion', 'email', 'telefono')
    search_fields=('nombre', 'telefono')

#Crear para los Articulos un Filtro de Campos.

class ArticulosAdmin(admin.ModelAdmin):
    list_filter=('seccion',)

#crear Filtro para Pedidos por el campo Fecha.

class PedidosAdmin(admin.ModelAdmin):
    list_display=('numero', 'fecha') #esto es lo que muestra en la consulta.
    list_filter=('fecha',)
#crea un filtro superior llamado -migas de pan- busquedas por fechas.
    date_hierarchy='fecha'

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)



