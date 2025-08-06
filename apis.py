import requests
import sqlite3
import time
import datetime
'''
https://api.portaldatransparencia.gov.br/api-de-dados/servidores?tipoServidor=1&situacaoServidor=1&cpf=38558610304&nome=FELIPE%20CAVALCANTE%20DA%20ROCHA&pagina=1

[{"key":"chave-api-dados","value":"28aa42b6d7c653294de1b8657aa84f46"}]
'''


def get_servidores(nome, orgao):
    url = f"https://api.portaldatransparencia.gov.br/api-de-dados/servidores?tipoServidor=1&situacaoServidor=1&nome={nome}&orgaoServidorExercicio={orgao}&pagina=1"
    headers = {
        "chave-api-dados": "28aa42b6d7c653294de1b8657aa84f46",
        "Content-Type": "application/json",
    }
    response = requests.get(url, headers=headers)
    return response.json()


def grava_servidor(f, servidor):
    if len(servidor) == 0:
        f.write("Servidor não encontrado\n")
        return

    id = servidor[0]['servidor']['id']
    nome = servidor[0]['servidor']['pessoa']['nome']
    funcao = ""
    atividade = ""
    uorgExercicio = ""
    uorgLotacao = ""
    if len(servidor[0]['fichasCargoEfetivo']) > 0:
        uorgLotacao = servidor[0]['fichasCargoEfetivo'][0]['uorgLotacao']

    if len(servidor[0]['fichasFuncao']) > 0:
        funcao = servidor[0]['fichasFuncao'][0]['funcao']
        atividade = servidor[0]['fichasFuncao'][0]['atividade']
        uorgExercicio = servidor[0]['fichasFuncao'][0]['uorgExercicio']

    f.write(
        f"{id}, {nome}, {funcao}, {atividade}, {uorgExercicio}, {uorgLotacao}\n"
    )


def mostra_servidores(orgao):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT nome_servidor FROM servidor ORDER BY nome_servidor limit 300 offset 500;"
    )
    nomes = cursor.fetchall()
    cursor.close()
    conn.close()

    f = open('servidores_ufca.csv', 'w')
    index = 1
    for nome in nomes:
        print('-----> ', datetime.datetime.now(), index, nome[0])
        index += 1
        servidor = get_servidores(nome[0], orgao)
        #print(servidor)
        grava_servidor(f, servidor)
        time.sleep(2)

    f.close()


if __name__ == "__main__":
    orgao = "26449"
    mostra_servidores(orgao)
    print("Fim")
    '''
https://dadosabertosapi.ufca.edu.br/service/recurso/servidor_por_siape.json?siape=2656876

    
    nome = "THIAGO MIELLE BRITO FERREIRA OLIVEIRA"
    url = f"https://api.portaldatransparencia.gov.br/api-de-dados/servidores?tipoServidor=1&situacaoServidor=1&nome={nome}&orgaoServidorExercicio={orgao}&pagina=1"
    headers = {
        "chave-api-dados": "28aa42b6d7c653294de1b8657aa84f46",
        "Content-Type": "application/json",
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    print("\n\n")
    print(data[0]['fichasCargoEfetivo'])
    print(20*"-")
    print(data[0]['fichasFuncao'])
    '''
