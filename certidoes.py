import os
import shutil
import os.path
from datetime import datetime
from datetime import date
from time import sleep 

### FUNÇÃO QUE IMPRIME O RESULTADO DO PROCESSO
def processo_terminado(x):
    print('\n' * 30)
    print('=' * 120)
    barra_esquerda = "|"
    barra_direita = "|"
    print("{:^110}".format(" \\|||||/"))
    print("{:^110}".format(" ( O O )"))   
    print("{:^110}".format("|------ooO-----(_)-------------|"))
    print("{:^110}".format("|                              |"))
    print("{:^110}".format("|          Resultado:          |"))
    print("{:^110}".format("|                              |"))
    print(barra_esquerda.rjust(40), end=' ')
    print(x.center(24), end='  ')
    print(barra_direita.ljust(35))
    print("{:^110}".format("|                              |"))
    print("{:^110}".format("|                              |"))
    print("{:^110}".format("|----------------------Ooo-----|"))
    print("{:^110}".format("          |__||__|        "))
    print("{:^110}".format("           ||  ||         "))
    print("{:^110}".format("          ooO  Ooo        "))
    print('=' * 120)
    print('\n' * 2)
    


#CRIA AS PASTAS
data = datetime.today()
dia = str(data.day)
mes = data.month - 1
ano = str(data.year)
mes_ext = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
mes_cor = mes_ext[mes]
lista = list()
lista = os.listdir('C:/' + ano + '/' + mes_cor + '/' + dia)
destino = ('C:/' + ano + '/' + mes_cor + '/' + dia + '/')
pastas = list()
resultado = ""
try:
    for i in lista:
        arqemint = int(i[0:7])
        if arqemint not in pastas:
            pastas.append(arqemint)
        else:
            pass
    for past in pastas:
        past = str(past)
        os.mkdir(destino + past)
        print(f"Pasta {past} criada com sucesso...")
    #COLOCA OS ARQUIVOS DENTRO DAS PASTAS
    lista_pasta = os.listdir('C:/' + ano + '/' + mes_cor + '/' + dia)
    for certidao in lista_pasta:
        if ".pdf" in certidao:
            cert_fat = int(certidao[0:7])
            cert_str = certidao
            for past_arq in pastas:
                if cert_fat == past_arq:
                    cert_emt = ('C:/' + ano + '/' + mes_cor + '/' + dia + '/' + certidao)
                    destino = ('C:/' + ano + '/' + mes_cor + '/' + dia + '/' + str(past_arq))
                    shutil.move(cert_emt, destino)
                    print(f"Arquivando a certidão {certidao} na pasta {past_arq}")
    sucesso = "SUCESSO! Fim do programa  "
    processo_terminado(sucesso)
    sleep(10)
    os.system('pause')
except FileExistsError:
    erro = "  ERRO! Pasta já existe... "
    processo_terminado(erro)
    sleep(10)
    os.system('pause')









