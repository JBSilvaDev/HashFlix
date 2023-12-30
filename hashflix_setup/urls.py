from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# namespace='filme' é opcional, caso não use remover tambem do arquivo url filho e da pagina html que possui filme:ArquivoHTMnome
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("filme.urls", namespace='filme')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
