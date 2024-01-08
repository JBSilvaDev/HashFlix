from django.contrib import admin
from .models import Episodio, Filme, Usuario
from django.contrib.auth.admin import UserAdmin


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


# Incluindo campo na exibição da classe usuario na area ADM
camposADM = list(UserAdmin.fieldsets)
camposADM.append(
    (
        "Campos Extras",
        {
            "fields": ("filmes_vistos",),
        },
    )
)

UserAdmin.fieldsets = tuple(camposADM)

admin.site.register(Filme, ExibicaoAdminFilme)
admin.site.register(Episodio, ExibicaoAdminEps)
admin.site.register(
    Usuario, UserAdmin
)  # UserAdmin é a exibição padrao dos usuarios na area adm
