# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CoreSetor(models.Model):
    codigo = models.CharField(max_length=10)
    nome = models.CharField(max_length=100)
    caminho = models.CharField(max_length=100)
    unidade_sigla = models.CharField(max_length=10)
    unidade_nome = models.CharField(max_length=100)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'core_setor'


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Servidor(models.Model):
    nome_servidor = models.TextField(db_column='NOME_SERVIDOR', blank=True, null=True)  # Field name made lowercase.
    nome_social_servidor = models.TextField(db_column='NOME_SOCIAL_SERVIDOR', blank=True, null=True)  # Field name made lowercase.
    cargo_origem = models.TextField(db_column='CARGO_ORIGEM', blank=True, null=True)  # Field name made lowercase.
    orgao_origem = models.TextField(db_column='ORGAO_ORIGEM', blank=True, null=True)  # Field name made lowercase.
    unnamed_4 = models.TextField(db_column='Unnamed:_4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    orgao_destino = models.TextField(db_column='ORGAO_DESTINO', blank=True, null=True)  # Field name made lowercase.
    unnamed_6 = models.TextField(db_column='Unnamed:_6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    plano_cargo_origem = models.TextField(db_column='PLANO_CARGO_ORIGEM', blank=True, null=True)  # Field name made lowercase.
    funcao_destino = models.TextField(db_column='FUNCAO_DESTINO', blank=True, null=True)  # Field name made lowercase.
    nivel_funcao_destino = models.TextField(db_column='NIVEL_FUNCAO_DESTINO', blank=True, null=True)  # Field name made lowercase.
    id_servidor = models.TextField(db_column='ID_SERVIDOR', blank=True, null=True)  # Field name made lowercase.
    mes = models.TextField(db_column='MES', blank=True, null=True)  # Field name made lowercase.
    vinculo_servidor = models.TextField(db_column='VINCULO_SERVIDOR', blank=True, null=True)  # Field name made lowercase.
    situacao_funcional = models.TextField(db_column='SITUACAO_FUNCIONAL', blank=True, null=True)  # Field name made lowercase.
    situacao_vinculo = models.TextField(db_column='SITUACAO_VINCULO', blank=True, null=True)  # Field name made lowercase.
    cod_uorg = models.TextField(db_column='COD_UORG', blank=True, null=True)  # Field name made lowercase.
    uorg = models.TextField(db_column='UORG', blank=True, null=True)  # Field name made lowercase.
    grupo_uorg = models.TextField(db_column='GRUPO_UORG', blank=True, null=True)  # Field name made lowercase.
    nivel_funcao = models.TextField(db_column='NIVEL_FUNCAO', blank=True, null=True)  # Field name made lowercase.
    jornada_trabalho = models.TextField(db_column='JORNADA_TRABALHO', blank=True, null=True)  # Field name made lowercase.
    cargo = models.TextField(db_column='CARGO', blank=True, null=True)  # Field name made lowercase.
    data_ingresso_cargo = models.TextField(db_column='DATA_INGRESSO_CARGO', blank=True, null=True)  # Field name made lowercase.
    sistematica_cargo = models.TextField(db_column='SISTEMATICA_CARGO', blank=True, null=True)  # Field name made lowercase.
    nivel_cargo = models.TextField(db_column='NIVEL_CARGO', blank=True, null=True)  # Field name made lowercase.
    gr_niv_cargo = models.TextField(db_column='GR_NIV_CARGO', blank=True, null=True)  # Field name made lowercase.
    cod_cargo = models.TextField(db_column='COD_CARGO', blank=True, null=True)  # Field name made lowercase.
    classe_cargo = models.TextField(db_column='CLASSE_CARGO', blank=True, null=True)  # Field name made lowercase.
    sexo = models.TextField(db_column='SEXO', blank=True, null=True)  # Field name made lowercase.
    cod_orgao = models.IntegerField(db_column='COD_ORGAO', blank=True, null=True)  # Field name made lowercase.
    nome_uorg = models.TextField(db_column='NOME_UORG', blank=True, null=True)  # Field name made lowercase.
    cod_siorg_orgao = models.IntegerField(db_column='COD_SIORG_ORGAO', blank=True, null=True)  # Field name made lowercase.
    cod_siorg_uorg = models.IntegerField(db_column='COD_SIORG_UORG', blank=True, null=True)  # Field name made lowercase.
    cod_vaga = models.IntegerField(db_column='COD_VAGA', blank=True, null=True)  # Field name made lowercase.
    data_nascimento_servidor = models.TextField(db_column='DATA_NASCIMENTO_SERVIDOR', blank=True, null=True)  # Field name made lowercase.
    deficiencia_fisica = models.TextField(db_column='DEFICIENCIA_FISICA', blank=True, null=True)  # Field name made lowercase.
    escolaridade = models.TextField(db_column='ESCOLARIDADE', blank=True, null=True)  # Field name made lowercase.
    grupo_escolaridade = models.TextField(db_column='GRUPO_ESCOLARIDADE', blank=True, null=True)  # Field name made lowercase.
    cor_origem_etnica = models.TextField(db_column='COR_ORIGEM_ETNICA', blank=True, null=True)  # Field name made lowercase.
    grupo_situacao_vinculo = models.TextField(db_column='GRUPO_SITUACAO_VINCULO', blank=True, null=True)  # Field name made lowercase.
    ano_ing_spub = models.TextField(db_column='ANO_ING_SPUB', blank=True, null=True)  # Field name made lowercase.
    exclusao = models.TextField(db_column='EXCLUSAO', blank=True, null=True)  # Field name made lowercase.
    dia_nomeacao = models.TextField(db_column='DIA_NOMEACAO', blank=True, null=True)  # Field name made lowercase.
    dia_ocor_ingr_orgao_ev = models.TextField(db_column='DIA_OCOR_INGR_ORGAO_EV', blank=True, null=True)  # Field name made lowercase.
    dia_ocor_excl_serv_ev = models.TextField(db_column='DIA_OCOR_EXCL_SERV_EV', blank=True, null=True)  # Field name made lowercase.
    atividade_funcao = models.TextField(db_column='ATIVIDADE_FUNCAO', blank=True, null=True)  # Field name made lowercase.
    qtde_vinc_serv = models.IntegerField(db_column='QTDE_VINC_SERV', blank=True, null=True)  # Field name made lowercase.
    qtde_afastamento = models.FloatField(db_column='QTDE_AFASTAMENTO', blank=True, null=True)  # Field name made lowercase.
    nome = models.TextField(db_column='NOME', blank=True, null=True)  # Field name made lowercase.
    mes_ansi = models.TextField(db_column='MES_ANSI', blank=True, null=True)  # Field name made lowercase.
    siape = models.TextField(db_column='SIAPE', blank=True, null=True)  # Field name made lowercase.
    id = models.TextField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    carreira = models.TextField(db_column='CARREIRA', blank=True, null=True)  # Field name made lowercase.
    escolaridade2 = models.TextField(db_column='ESCOLARIDADE2', blank=True, null=True)  # Field name made lowercase.
    idade = models.IntegerField(db_column='IDADE', blank=True, null=True)  # Field name made lowercase.
    faixa_etaria = models.TextField(db_column='FAIXA_ETARIA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'servidor'
