from django.contrib import admin

from blog.models import Post

# admin.site.register(Post)
# Importación del decorador 'register' del módulo 'admin' de Django
from django.contrib import admin

# Decorador que registra el modelo 'Post' con el panel de administración de Django
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Lista de campos a mostrar en la lista de objetos en el panel de administración
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    # Lista de campos por los que se puede filtrar la lista de objetos en el panel de administración
    list_filter = ['status', 'created', 'publish', 'author']
    # Lista de campos que se pueden buscar en la lista de objetos en el panel de administración
    search_fields = ['title', 'body']
    # Diccionario que especifica campos prepopulados en el formulario de creación/editación basados en otros campos
    prepopulated_fields = {'slug': ('title',)}
    # Lista de campos que se mostrarán como enlaces a objetos en el formulario de creación/editación
    raw_id_fields = ['author']
    # Nombre del campo que se utilizará como jerarquía de fechas en el panel de administración
    date_hierarchy = 'publish'
    # Lista de campos utilizados para ordenar la lista de objetos en el panel de administración
    ordering = ['status', 'publish']
