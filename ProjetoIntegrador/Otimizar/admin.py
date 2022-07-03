from django.contrib import admin
from Otimizar.models import Peca, Sobra, Aproveita

class Pecas (admin.ModelAdmin):
        list_display = ('id', 'comprimento', 'largura', 'material')
        list_display_links = ('id', 'material')
        search_fields = ('material',)
        list_per_page = 20


admin.site.register(Peca, Pecas)

class Sobras (admin.ModelAdmin):
        list_display = ('id', 'comprimento', 'largura', 'material')
        list_display_links = ('id', 'material')
        search_fields = ('material',)
        list_per_page = 20


admin.site.register(Sobra, Sobras)

class Aproveitam (admin.ModelAdmin):
        list_display = ('id', 'sobra', 'peca')
        list_display_links = ('id',)


admin.site.register(Aproveita, Aproveitam)
