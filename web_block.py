import time
from datetime import datetime as dt

#Creditos Alameda

hostsPath="hosts"
"""
Eh com esse arquivo que iremos usar para bloquear os site
mude local se voce usa o sistema windows.
Estou usando o sistema linux por isso coloquei o local do arquivo

C:\windows\system32\drivers\etc\hosts

"""
# hostsPath=r"/etc/hosts"


# # Vai recebe localhost da sua rede
redirect="127.0.0.1"

# # Aqui criamos uma lista para recebe os site que estamos querendo bloquear
websites=["facebook.com","www.facebook.com"]

"""

Vou criar um loop infinito para ele roda pra sempre ate o usuario cancelar automaticamente o loop
"""
while True:
    
    """
    aqui nois verifica. " ano, mes e dia 8 eh menor do que ano,mes do dia 22"
    aqui vai da False por que o ano,mes e dia 8 eh menor do que, ano,mes e dia 22, entao irar da falso
    entao ele imprime "jornada de trabalho"
    """
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,22):
        print("Jornada de trabalho...")
        # Aqui uso o with para fechar o arquivo automaticamente no final do codigo 
        # "usamos essa metodo 'with' quando queremos fechar arquivo de forma mais facil, ele fecha automaticamente sem precisa usa 'arquivo.close()'"
        with open(hostsPath,'r+') as file:
            
            # faco leitura do file

            content=file.read()
            
            #Faco um for para ele analisar cada linha do arquivo 
            #Faco um if que vai ter o PASS 'mesma coisa que "NULL" um parametro nulo'
            #Entao ele vai escrever redirecionamento e site que quer bloquear
            for site in websites:
                if site in content:
                    pass
                else:
                    file.write(redirect+" "+site+"\n")
  
    # else:
    #     with open(hostsPath,'r+') as file:
    #         content=file.readlines()
    #         file.seek(0) # redefine o ponteiro para o topo do arquivo de texto
    #         for line in content:
    #              # aqui vem a linha complicada, basicamente nós sobrescrevemos todo o arquivo
    #             if not any(site in line for site in websites):
    #                 file.write(line)
    #         file.truncate() # esta linha é usada para excluir as linhas finais (que contêm DNS)
    #     print ("Horas divertidas...")
    # time.sleep(5)
    #Aqui crio outro loop infinito para eu informa o usuario oque ele deve fazer
    """caso ele informe um valor diferente de 1 ou 0 entao irar imprimir ERROR,
    Se ele informa 1, vai cancelar o segundo loop e vai continuar o script
    Se ele informa 0 irar finalizar o primeiro e o segundo loop, Assim vai finalizar o script
    """

    while True:
        deseja = int(input("Deseja Continuar? [0 Interrompa/1 Continue]: "))
        if deseja == 0 or deseja == 1:
            break
        print("ERROR! Por, Favor digite '0' para sair ou '1' para continuar")
    if deseja == 0:
        break
