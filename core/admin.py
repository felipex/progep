from django.contrib import admin
from .models import Setor, Setor2, Servidor, Servidor2

admin.site.site_header = 'PROGEP Admin'
admin.site.site_title = 'PROGEP Admin Portal'


class SetorAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'caminho', 'caminho_sigla',
                    'unidade_sigla', 'unidade_nome')
    search_fields = ('codigo', 'nome', 'caminho', 'caminho_sigla',
                     'unidade_sigla', 'unidade_nome')
    list_filter = ('unidade_sigla', )
    list_per_page = 25


class EscolaridadeFilter(admin.SimpleListFilter):
    title = 'Escolaridade'
    parameter_name = 'escolaridade'
    default_value = None

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        if self.value() == 'GRADUAÇÃO':
            return queryset.filter(escolaridade='GRADUAÇÃO')
        if self.value() == 'ESPECIALIZAÇÃO':
            return queryset.filter(escolaridade='ESPECIALIZAÇÃO')
        if self.value() == 'MESTRADO':
            return queryset.filter(escolaridade='MESTRADO')
        if self.value() == 'DOUTORADO':
            return queryset.filter(escolaridade='DOUTORADO')

    def lookups(self, request, model_admin):
        return (
            ('GRADUAÇÃO', 'Graduação'),
            ('ESPECIALIZAÇÃO', 'Especialização'),
            ('MESTRADO', 'Mestrado'),
            ('DOUTORADO', 'Doutorado'),
        )


class ServidorAdmin(admin.ModelAdmin):
    lista1 = 0

    list_display = (
        'nome',
        'siape',
        'caminho',
        'nome_uorg',
        'unidade_sigla',
        'nivel_funcao',
        'carreira',
        'escolaridade',
        'situacao_vinculo',
        'cargo',
    )
    search_fields = (
        'nome',
        'siape',
        'carreira',
        'escolaridade',
        'cargo',
        'caminho',
    )
    list_filter = (
        'nivel_funcao',
        'escolaridade',
        'carreira',
        'situacao_vinculo',
        'unidade_sigla',
    )
    list_per_page = 25
    actions = ['nada']

    @admin.action(description='Nada')
    def nada(self, request, queryset):
        self.lista1 = 1

    def get_list_display(self, request):
        if self.lista1 == 0:
            return (
                'nome',
                'siape',
                'caminho',
                'nome_uorg',
                'unidade_sigla',
                'nivel_funcao',
                'carreira',
                'escolaridade',
                'situacao_vinculo',
                'cargo',
            )

        return (
            'nome',
            'sexo',
            'idade',
            'siape',
            'caminho',
            'nome_uorg',
            'unidade_sigla',
            'nivel_funcao',
            'carreira',
            'escolaridade',
            'situacao_vinculo',
            'cargo',
        )


class Servidor2Admin(admin.TabularInline):
    model = Servidor2


class SetorAdmin2(admin.ModelAdmin):
    inlines = [Servidor2Admin]


admin.site.register(Servidor, ServidorAdmin)
admin.site.register(Setor, SetorAdmin)
admin.site.register(Setor2, SetorAdmin2)
