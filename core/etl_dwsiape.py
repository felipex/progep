from datetime import date, datetime
import pandas as pd


def open_file(filename, encoding='utf-8', skiproww=2, sep=';'):
  df = pd.read_csv(filename, sep=';', encoding=encoding, skiprows=2)
  return df


def change_column_name(old_name):
  letter_with_accent = 'ÁÀÃÂÉÊÍÓÔÕÚÇ '
  letter_without_accent = 'AAAAEEIOOOUC_'
  name = old_name
  for i in range(len(letter_with_accent)):
    name = name.replace(letter_with_accent[i], letter_without_accent[i])

  return name


def change_columns_name(df):
  columns = {}
  for c in df.columns:
    columns[c] = change_column_name(c)

  df.rename(columns=columns, inplace=True)


# MMM YYYY to YYYYMM
def change_month(month):
  months = {
      'Jan': '01',
      'Fef': '02',
      'Mar': '03',
      'Abr': '04',
      'Mai': '05',
      'Jun': '06',
      'Jul': '07',
      'Ago': '08',
      'Set': '09',
      'Out': '10',
      'Nov': '11',
      'Dez': '12'
  }
  nmonth, year = month.split(' ')
  return f'{year}{months[nmonth]}'


def strtodate(date_str):
  try:
    return pd.to_datetime(date_str, format='%d/%m/%Y', errors='coerce')
  except ValueError:
    try:
      return pd.to_datetime(date_str, format='%Y-%m-%d', errors='coerce')
    except ValueError:
      return pd.NaT


def idade(data_nascimento, data_atual=date.today()):
  anos = data_atual.year - data_nascimento.year
  meses = data_atual.month - data_nascimento.month
  dias = data_atual.day - data_nascimento.day

  if meses < 0 or (meses == 0 and dias < 0):
    anos -= 1

  return anos


def faixa_etaria(idade):
  if idade <= 20:
    return '0 - 20'
  if idade <= 30:
    return '21 - 30'
  if idade <= 40:
    return '31 - 40'
  if idade <= 50:
    return '41 - 50'
  if idade <= 60:
    return '51 - 60'
  if idade <= 70:
    return '61 - 70'
  if idade <= 80:
    return '71 - 80'
  return '80 -'


def transform_idade(df):
  df['IDADE'] = df.apply(
      lambda row: idade(strtodate(row['DATA_NASCIMENTO_SERVIDOR'])), axis=1)
  df['FAIXA_ETARIA'] = df.apply(lambda row: faixa_etaria(row['IDADE']), axis=1)


def transform_escolaridade(df):
  df['ESCOLARIDADE'] = df['ESCOLARIDADE'].str.strip()
  df['ESCOLARIDADE2'] = df['ESCOLARIDADE']
  df['ESCOLARIDADE'] = df.apply(
      lambda row: 'DOUTORADO'
      if row['ESCOLARIDADE2'].startswith('DOUTORADO') else row['ESCOLARIDADE'],
      axis=1)
  df['ESCOLARIDADE'] = df.apply(
      lambda row: 'MESTRADO'
      if row['ESCOLARIDADE2'].startswith('MESTRADO') else row['ESCOLARIDADE'],
      axis=1)
  df['ESCOLARIDADE'] = df.apply(lambda row: 'ESPECIALIZAÇÃO' if row[
      'ESCOLARIDADE2'].startswith('ESPECIALIZACAO') else row['ESCOLARIDADE'],
                                axis=1)
  df['ESCOLARIDADE'] = df.apply(lambda row: 'GRADUAÇÃO' if row[
      'ESCOLARIDADE2'].startswith('ENSINO SUPERIOR') else row['ESCOLARIDADE'],
                                axis=1)
  df['ESCOLARIDADE'] = df.apply(
      lambda row: 'GRADUAÇÃO'
      if row['ESCOLARIDADE2'].startswith('GRADUACAO') else row['ESCOLARIDADE'],
      axis=1)


def transform_nome_social(df):
  df['NOME'] = df['NOME_SERVIDOR']
  df['NOME'] = df.apply(
      lambda row: row['NOME_SOCIAL_SERVIDOR']
      if row['NOME_SOCIAL_SERVIDOR'] != '0' else row['NOME_SERVIDOR'],
      axis=1)
  #df['NOME'] = df['NOME_SOCIAL_SERVIDOR'] if df['NOME_SOCIAL_SERVIDOR'] != '0' else df['NOME_SERVIDOR']


def transform_mes(df):
  df['MES_ANSI'] = df.apply(lambda row: change_month(row['MES']), axis=1)


def transform_siape(df):
  df['SIAPE'] = df.apply(lambda row: row['VINCULO_SERVIDOR'].split('-')[1],
                         axis=1)


def transform_id(df):
  df['ID'] = df['MES_ANSI'] + df['SIAPE']


def transform_carreira(df):
  df['CARREIRA'] = df.apply(lambda row: 'DOCENTE'
                            if row['NIVEL_CARGO'][0:3] == '705' else 'TAE'
                            if row['NIVEL_CARGO'][0:3] == '701' else 'OUTROS',
                            axis=1)


def unidade_tipo(codigo):
  if codigo in pro_reitorias:
    return 'PRÓ-REITORIA'
  if codigo in unidades_academicas:
    return 'UNIDADE ACADÊMICA'
  if codigo in diretorias:
    return 'DIRETORIA'

  return 'OUTROS'


def transform_unidade(df):
  pro_reitorias = [
      228380,  # PRPI
      228396,  # PROPLAN
      228414,  # PRAE
      228425,  # PROGEP
      228448,  # PROAD
      228497,  # PROEX
      228506  # PROCULT
  ]
  unidades_academicas = [
      228540,  # FAMED
      228533,  # CCT
      228492,  # IISCA
      228527,  # CCAB
      228476,  # CCSA
      228485,  # IFE
  ]
  diretorias = [
      228371,  # DCOM
      228603,  # DINFRA
      228598,  # DIARI
      228377,  # DLA
      228583,  # DTI
      228519,  # SIBI
  ]

  df['UNIDADE_TIPO'] = df.apply(
      lambda row: unidade_tipo(row['COD_SIORG_UORG']), axis=1)


def clean_data(df):
  df = df.dropna()
  transform_nome_social(df)
  transform_mes(df)
  transform_siape(df)
  transform_id(df)
  transform_carreira(df)
  #transform_unidade(df)
  transform_escolaridade(df)
  transform_idade(df)

  return df


def extract_data(old_df):
  """df = old_df[[
      'ID', 'SIAPE', 'NOME', 'NOME_SERVIDOR', 'NOME_SOCIAL_SERVIDOR',
      'ID_SERVIDOR', 'MES', 'MES_ANSI', 'SITUACAO_FUNCIONAL',
      'SITUACAO_VINCULO', 'COD_UORG', 'UORG', 'NOME_UORG', 'COD_SIORG_ORGAO',
      'COD_SIORG_UORG', 'NIVEL_FUNCAO', 'JORNADA_TRABALHO', 'CARGO',
      'ESCOLARIDADE', 'IDADE', 'FAIXA_ETARIA', 'DATA_NASCIMENTO_SERVIDOR',
      'CARREIRA', 'DATA INGRESSO CARGO', 'NIVEL_CARGO', 'GR_NIV_CARGO',
      'COD_CARGO', 'CLASSE CARGO'
  ]]
  """
  df = old_df
  return df


def etl_dwsiape(connection,
                filename='',
                encoding='utf-8',
                skiproww=2,
                sep=';'):
  df = open_file(filename, encoding, skiproww, sep)
  change_columns_name(df)
  df = clean_data(df)
  df = extract_data(df)

  hh = df.columns
  print(hh)
  print(df[[
      'ID',
      'MES_ANSI',
      'SIAPE',
      'NOME',
      #'UNIDADE_TIPO',
  ]])
  df.to_sql('servidor', connection, if_exists='append', index=False)


'''
import os

database = os.getenv('DATABASE_CONNECTION')
filename = './temp/servidores.csv'
etl_dwsiape(database, filename=filename, encoding='utf-16le')
'''
