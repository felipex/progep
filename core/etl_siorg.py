from datetime import datetime
import logging
import requests
import pandas as pd


def estrutura_da_unidade_api(unidade: str):
  """
    Acessa a API do SIORG para obter a informação da unidade organizacional 
    correspondente ao identificador fornecido. Retorna os dados da estrutura dessa unidade.

    Parâmetros:
    unidade (str): Código da unidade organizacional.

    Retorna:
    dict: A estrutura da unidade organizacional em formato JSON.
    """

  estrutura = requests.get(
      f"http://estruturaorganizacional.dados.gov.br/doc/unidade-organizacional/{unidade}/estrutura"
  )

  return estrutura.json()


def lista_de_unidades_api(unidade: str):
  resposta = requests.get(
      f'https://estruturaorganizacional.dados.gov.br/doc/estrutura-organizacional/resumida?codigoPoder=1&codigoEsfera=1&codigoUnidade={unidade}'
  ).json()
  return resposta


def lista_de_unidades(unidades_api: pd.DataFrame) -> pd.DataFrame:
  df_unidades = pd.DataFrame(columns=['SETOR_CODIGO', 'SETOR_NOME', 'SIGLA'])
  for u in unidades_api['unidades']:
    df_unidades.loc[len(df_unidades)] = [
        u['codigoUnidade'].split('/')[-1:][0], u['nome'], u['sigla']
    ]

  return df_unidades


def orgao(codigo: str, df_unidades: pd.DataFrame):
  u = df_unidades[df_unidades['SETOR_CODIGO'] == codigo]
  return u.to_dict('records')[0]


def adiciona_setor(df: pd.DataFrame, codigo: str, nome: str, path: str,
                   path_sigla: str, codigo_superior: str, nome_superior: str):
  df.loc[len(df)] = [
      codigo, nome, path, path_sigla, codigo_superior, nome_superior
  ]


def adiciona_setores(df, organograma, df_unidades):
  unidade = "122391"
  for e in organograma['estrutura']['estrutura']:
    o = orgao(str(e['codigoUnidade']), df_unidades)
    adiciona_setor(df, o['SETOR_CODIGO'], o['SETOR_NOME'],
                   f"{o['SIGLA']}/UFCA", f"{o['SETOR_CODIGO']}/{unidade}",
                   o['SIGLA'], o['SETOR_NOME'])

    if e['estrutura']:
      for ee in e['estrutura']:
        oo = orgao(str(ee['codigoUnidade']), df_unidades)
        adiciona_setor(df, oo['SETOR_CODIGO'], oo['SETOR_NOME'],
                       f"{oo['SIGLA']}/{o['SIGLA']}/UFCA",
                       f"{oo['SETOR_CODIGO']}/{o['SETOR_CODIGO']}/{unidade}",
                       o['SIGLA'], o['SETOR_NOME'])

        if ee['estrutura']:
          for eee in ee['estrutura']:
            ooo = orgao(str(eee['codigoUnidade']), df_unidades)
            adiciona_setor(
                df, ooo['SETOR_CODIGO'], ooo['SETOR_NOME'],
                f"{ooo['SIGLA']}/{oo['SIGLA']}/{o['SIGLA']}/UFCA",
                f"{ooo['SETOR_CODIGO']}/{oo['SETOR_CODIGO']}/{o['SETOR_CODIGO']}/{unidade}",
                o['SIGLA'], o['SETOR_NOME'])

            if eee['estrutura']:
              for eeee in eee['estrutura']:
                oooo = orgao(str(eeee['codigoUnidade']), df_unidades)
                adiciona_setor(
                    df, oooo['SETOR_CODIGO'], oooo['SETOR_NOME'],
                    f"{oooo['SIGLA']}/{ooo['SIGLA']}/{oo['SIGLA']}/{o['SIGLA']}/UFCA",
                    f"{oooo['SETOR_CODIGO']}/{ooo['SETOR_CODIGO']}/{oo['SETOR_CODIGO']}/{o['SETOR_CODIGO']}/{unidade}",
                    o['SIGLA'], o['SETOR_NOME'])


#def to_sql(df: pd.DataFrame, conexao: sqlite3.Connection, table: str):
def to_sql(df, conexao, table: str):
  for index, row in df.iterrows():
    values = ''
    for v in row.values:
      values += f"'{v}', "

    values += f"'{datetime.now()}' "
    #values = values[:-2]

    insert_query = f"""INSERT INTO {table} ({', '.join(df.columns)}, updated_at) VALUES ({values})"""
    print(insert_query)
    conexao.execute(insert_query)
    conexao.commit()
  #df.to_sql(table, conexao, if_exists='replace', index=False)


def etl_siorg(unidade, conexao):
  logging.info('Buscando organograma no SIORG...')
  organograma = estrutura_da_unidade_api(unidade)
  unidades_api = lista_de_unidades_api(unidade)
  df_unidades = lista_de_unidades(unidades_api)

  df_setor = pd.DataFrame(columns=[
      'SETOR_CODIGO', 'SETOR_NOME', 'CAMINHO', 'CAMINHO_SIGLA',
      'UNIDADE_SIGLA', 'UNIDADE_NOME'
  ])
  adiciona_setores(df_setor, organograma, df_unidades)
  df_setor.rename(columns={
      'SETOR_CODIGO': 'codigo',
      'SETOR_NOME': 'nome',
      'CAMINHO': 'caminho',
      'CAMINHO_SIGLA': 'caminho_sigla',
      'UNIDADE_SIGLA': 'unidade_sigla',
      'UNIDADE_NOME': 'unidade_nome'
  },
                  inplace=True)
  df_setor.reset_index(drop=True, inplace=True)
  df_setor.index = df_setor.index + 1
  logging.info('Gravando organograma no banco de dados...')
  to_sql(df_setor, conexao, 'core_setor')
  #df_setor.to_sql('core_setor', conexao, if_exists='replace', index=False)


'''
CREATE TABLE IF NOT EXISTS "core_setor" (
  id integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  codigo varchar(10) NOT NULL, 
  nome varchar(100) NOT NULL, 
  caminho varchar(100) NOT NULL, 
  caminho_sigla varchar(100) NULL,
  unidade_sigla varchar(10) NOT NULL, 
  unidade_nome varchar(100) NOT NULL, 
  updated_at datetime NOT NULL);
'''
