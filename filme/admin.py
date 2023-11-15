from django.contrib import admin
from .models import Episodio, Filme


# Register your models here.
class ExibicaoAdminFilme(admin.ModelAdmin):
    list_display = (
        "id",
        "titulo",
        "categoria",
        "data_criacao",
    )
    list_display_links = (
        "id",
        "titulo",
    )


class ExibicaoAdminEps(admin.ModelAdmin):
    list_display = (
        "titulo",
        "filme",
    )
    list_filter = ("filme",)


admin.site.register(Filme, ExibicaoAdminFilme)
admin.site.register(Episodio, ExibicaoAdminEps)
