from django.contrib import admin
from .models import Setor, Setor2, Servidor, Servidor2, Servidorx
from django_admin_multi_select_filter.filters import MultiSelectFieldListFilter

from unfold.admin import ModelAdmin

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


class MyMultiChoiceFilter(admin.SimpleListFilter):
    title = 'My Multi-Select Filter'
    parameter_name = 'mes_ansi'

    def lookups(self, request, model_admin):
        # Return a list of tuples (value, human-readable name)
        # These will be the options in your filter
        return [
            ('202501', 'Jan'),
            ('202502', 'Fev'),
            ('202503', 'Mar'),
            ('202504', 'Abr'),
            ('202505', 'Mai'),
            ('202506', 'Jun'),
            ('202507', 'Jul'),
            ('202508', 'Ago'),
            ('202509', 'Set'),
            ('202510', 'Out'),
            ('202511', 'Nov'),
            ('202512', 'Dez'),
        ]

    def queryset(self, request, queryset):
        if self.value():
            # Get selected values (they will be comma-separated if multiple selected)
            selected_values = self.value().split(',')
            # Apply your filtering logic based on selected_values
            return queryset.filter(mes_ansi__in=selected_values)
        return queryset


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
        'mes_ansi',
        'nome_uorg',
    )
    list_filter = (
        ('mes_ansi', MultiSelectFieldListFilter),
        'nivel_cargo',
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
                'nivel_cargo',
                'mes_ansi',
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
            'mes_ansi',
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

    def get_search_results(self, request, queryset, search_term):
        return super().get_search_results(request, queryset, search_term)


class Servidor2Admin(admin.TabularInline):
    model = Servidor2


class SetorAdmin2(admin.ModelAdmin):
    inlines = [Servidor2Admin]


class ServidorxAdmin(admin.ModelAdmin):

    list_display = ('nome', 'siape')
    search_fields = ('nome', 'siape')
    list_per_page = 25


admin.site.register(Servidor, ServidorAdmin)
admin.site.register(Setor, SetorAdmin)
admin.site.register(Setor2, SetorAdmin2)

admin.site.register(Servidorx, ServidorxAdmin)
