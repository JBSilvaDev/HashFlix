from django.contrib import admin
from .models import Filme

# Register your models here.
class ExibicaoAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "categoria", "data_criacao" )
    list_display_links = ("id", "titulo")

admin.site.register(Filme, ExibicaoAdmin)
