from django.db import models
from django.db.models.enums import Choices
from pandas.core.algorithms import unique


class Setor(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=100)
    caminho = models.CharField(max_length=100)
    caminho_sigla = models.CharField(max_length=100)
    unidade_sigla = models.CharField(max_length=10)
    unidade_nome = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'


class Servidor(models.Model):

    ESCOLARIDADE_CHOICES = (
        ('ENSINO FUNDAMENTAL', 'Ensino Fundamental'),
        ('ENSINO MÉDIO', 'Ensino Médio'),
        ('ENSINO SUPERIOR', 'Ensino Superior'),
        ('PÓS-GRADUAÇÃO', 'Pós-graduação'),
        ('PÓS-GRADUAÇÃO', 'Pós-graduação'),
        ('GRADUAÇÃO', 'Graduação'),
        ('ESPECIALIZAÇÃO', 'Especialização'),
        ('MESTRADO', 'Mestrado'),
        ('DOUTORADO', 'Doutorado'),
    )

    nome = models.CharField(db_column='NOME',
                            blank=True,
                            max_length=100,
                            null=True)  # Field name made lowercase.

    nome_servidor = models.CharField(db_column='NOME_SERVIDOR',
                                     max_length=100,
                                     blank=True,
                                     null=True)  # Field name made lowercase.
    mes = models.CharField(db_column='MES',
                           blank=True,
                           max_length=100,
                           null=True)  # Field name made lowercase.
    vinculo_servidor = models.CharField(
        db_column='VINCULO_SERVIDOR', blank=True, max_length=100,
        null=True)  # Field name made lowercase.
    situacao_funcional = models.CharField(
        db_column='SITUACAO_FUNCIONAL', blank=True, max_length=100,
        null=True)  # Field name made lowercase.
    situacao_vinculo = models.CharField(
        db_column='SITUACAO_VINCULO', blank=True, max_length=100,
        null=True)  # Field name made lowercase.
    cod_uorg = models.CharField(db_column='COD_UORG',
                                blank=True,
                                max_length=100,
                                null=True)  # Field name made lowercase.
    uorg = models.CharField(db_column='UORG',
                            blank=True,
                            max_length=100,
                            null=True)  # Field name made lowercase.
    grupo_uorg = models.CharField(db_column='GRUPO_UORG',
                                  max_length=100,
                                  blank=True,
                                  null=True)  # Field name made lowercase.
    nivel_funcao = models.CharField(db_column='NIVEL_FUNCAO',
                                    max_length=100,
                                    blank=True,
                                    null=True)  # Field name made lowercase.
    jornada_trabalho = models.CharField(
        db_column='JORNADA_TRABALHO', blank=True, max_length=100,
        null=True)  # Field name made lowercase.
    cargo = models.CharField(db_column='CARGO',
                             blank=True,
                             max_length=100,
                             null=True)  # Field name made lowercase.
    data_ingresso_cargo = models.CharField(
        db_column='DATA_INGRESSO_CARGO', blank=True, max_length=100,
        null=True)  # Field name made lowercase.
    sistematica_cargo = models.CharField(
        db_column='SISTEMATICA_CARGO', blank=True, max_length=100,
        null=True)  # Field name made lowercase.
    nivel_cargo = models.CharField(db_column='NIVEL_CARGO',
                                   max_length=100,
                                   blank=True,
                                   null=True)  # Field name made lowercase.
    gr_niv_cargo = models.CharField(db_column='GR_NIV_CARGO',
                                    max_length=100,
                                    blank=True,
                                    null=True)  # Field name made lowercase.
    cod_cargo = models.CharField(db_column='COD_CARGO',
                                 blank=True,
                                 max_length=100,
                                 null=True)  # Field name made lowercase.
    classe_cargo = models.CharField(db_column='CLASSE_CARGO',
                                    max_length=100,
                                    blank=True,
                                    null=True)  # Field name made lowercase.
    sexo = models.CharField(db_column='SEXO',
                            blank=True,
                            max_length=100,
                            null=True)  # Field name made lowercase.
    cod_orgao = models.IntegerField(db_column='COD_ORGAO',
                                    blank=True,
                                    null=True)  # Field name made lowercase.
    nome_uorg = models.CharField(db_column='NOME_UORG',
                                 blank=True,
                                 max_length=100,
                                 null=True)  # Field name made lowercase.
    cod_siorg_orgao = models.IntegerField(
        db_column='COD_SIORG_ORGAO', blank=True,
        null=True)  # Field name made lowercase.
    cod_siorg_uorg = models.IntegerField(
        db_column='COD_SIORG_UORG', blank=True,
        null=True)  # Field name made lowercase.
    cod_vaga = models.IntegerField(db_column='COD_VAGA', blank=True,
                                   null=True)  # Field name made lowercase.
    data_nascimento_servidor = models.CharField(
        db_column='DATA_NASCIMENTO_SERVIDOR',
        blank=True,
        max_length=100,
        null=True)  # Field name made lowercase.
    deficiencia_fisica = models.CharField(
        db_column='DEFICIENCIA_FISICA', blank=True, max_length=100,
        null=True)  # Field name made lowercase.
    escolaridade = models.CharField(db_column='ESCOLARIDADE',
                                    #choices=ESCOLARIDADE_CHOICES,
                                    blank=True,
                                    max_length=100,
                                    null=True)  # Field name made lowercase.
    grupo_escolaridade = models.CharField(
        db_column='GRUPO_ESCOLARIDADE', blank=True, max_length=100,
        null=True)  # Field name made lowercase.
    cor_origem_etnica = models.CharField(
        db_column='COR_ORIGEM_ETNICA', blank=True, max_length=100,
        null=True)  # Field name made lowercase.
    grupo_situacao_vinculo = models.CharField(
        db_column='GRUPO_SITUACAO_VINCULO',
        blank=True,
        max_length=100,
        null=True)  # Field name made lowercase.
    ano_ing_spub = models.CharField(db_column='ANO_ING_SPUB',
                                    blank=True,
                                    max_length=100,
                                    null=True)  # Field name made lowercase.
    exclusao = models.CharField(db_column='EXCLUSAO',
                                blank=True,
                                max_length=100,
                                null=True)  # Field name made lowercase.
    dia_nomeacao = models.CharField(db_column='DIA_NOMEACAO',
                                    max_length=100,
                                    blank=True,
                                    null=True)  # Field name made lowercase.
    dia_ocor_ingr_orgao_ev = models.CharField(
        db_column='DIA_OCOR_INGR_ORGAO_EV',
        blank=True,
        max_length=100,
        null=True)  # Field name made lowercase.
    dia_ocor_excl_serv_ev = models.CharField(
        db_column='DIA_OCOR_EXCL_SERV_EV',
        blank=True,
        max_length=100,
        null=True)  # Field name made lowercase.
    atividade_funcao = models.CharField(
        db_column='ATIVIDADE_FUNCAO', blank=True, max_length=100,
        null=True)  # Field name made lowercase.
    qtde_vinc_serv = models.IntegerField(
        db_column='QTDE_VINC_SERV', blank=True,
        null=True)  # Field name made lowercase.
    qtde_afastamento = models.FloatField(
        db_column='QTDE_AFASTAMENTO', blank=True,
        null=True)  # Field name made lowercase.
    mes_ansi = models.CharField(db_column='MES_ANSI',
                                blank=True,
                                max_length=100,
                                null=True)  # Field name made lowercase.
    siape = models.CharField(db_column='SIAPE',
                             blank=True,
                             max_length=100,
                             null=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=100,
                          primary_key=True)  # Field name made lowercase.
    carreira = models.CharField(db_column='CARREIRA',
                                blank=True,
                                max_length=100,
                                null=True)  # Field name made lowercase.
    escolaridade2 = models.CharField(db_column='ESCOLARIDADE2',
                                     max_length=100,
                                     blank=True,
                                     null=True)  # Field name made lowercase.
    idade = models.IntegerField(db_column='IDADE', blank=True,
                                null=True)  # Field name made lowercase.
    faixa_etaria = models.CharField(db_column='FAIXA_ETARIA',
                                    max_length=100,
                                    blank=True,
                                    null=True)  # Field name made lowercase.

    caminho = models.CharField(max_length=100)
    unidade_sigla = models.CharField(max_length=10)
    unidade_nome = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'core_servidor'


class Setor2(Setor):

    class Meta:
        proxy = True


class Servidor2(models.Model):
    nome = models.CharField(db_column='NOME', max_length=100)
    siape = models.CharField(db_column='SIAPE', max_length=100)
    setor = models.ForeignKey(Setor2,
                              on_delete=models.CASCADE,
                              db_column='COD_SIORG_UORG',
                              to_field='codigo')

    class Meta:
        managed = False
        db_table = 'servidor'


'''
https://dadosabertosapi.ufca.edu.br/service/recurso/servidor_por_siape.json?siape=2656876

'''
'''
CREATE VIEW core_servidor AS 
SELECT * FROM servidor s, core_setor c where c.codigo = s.cod_siorg_uorg;
 core_servidor(NOME_SERVIDOR,NOME_SOCIAL_SERVIDOR,CARGO_ORIGEM,ORGAO_ORIGEM,"Unnamed:_4",ORGAO_DESTINO,"Unnamed:_6",PLANO_CARGO_ORIGEM,FUNCAO_DESTINO,NIVEL_FUNCAO_DESTINO,ID_SERVIDOR,MES,VINCULO_SERVIDOR,SITUACAO_FUNCIONAL,SITUACAO_VINCULO,COD_UORG,UORG,GRUPO_UORG,NIVEL_FUNCAO,JORNADA_TRABALHO,CARGO,DATA_INGRESSO_CARGO,SISTEMATICA_CARGO,NIVEL_CARGO,GR_NIV_CARGO,COD_CARGO,CLASSE_CARGO,SEXO,COD_ORGAO,NOME_UORG,COD_SIORG_ORGAO,COD_SIORG_UORG,COD_VAGA,DATA_NASCIMENTO_SERVIDOR,DEFICIENCIA_FISICA,ESCOLARIDADE,GRUPO_ESCOLARIDADE,COR_ORIGEM_ETNICA,GRUPO_SITUACAO_VINCULO,ANO_ING_SPUB,EXCLUSAO,DIA_NOMEACAO,DIA_OCOR_INGR_ORGAO_EV,DIA_OCOR_EXCL_SERV_EV,ATIVIDADE_FUNCAO,QTDE_VINC_SERV,QTDE_AFASTAMENTO,NOME,MES_ANSI,SIAPE,ID,CARREIRA,ESCOLARIDADE2,IDADE,FAIXA_ETARIA,"id:1",codigo,"nome:1",caminho,caminho_sigla,unidade_sigla,unidade_nome,updated_at);
'''
