import math
import random
import banco_de_dados
import fun 
import colorama
from colorama import Fore,Style

dic = banco_de_dados.DADOS
paises = banco_de_dados.paises
EARTH_RADIUS = 6371

# PAIS ESCOLHIDO
continentes = list(dic.keys())
continente_escolhido = random.choice(continentes)
pais_escolhido = fun.sorteia_pais(dic[continente_escolhido])

# INFO do pais
info_pais= dic[continente_escolhido][pais_escolhido]
area = info_pais['area']
populacao = info_pais['populacao']
capital = info_pais['capital']
bandeira = info_pais['bandeira']
longitude_escolida = info_pais['geo']['longitude']
latitude_escolida = info_pais['geo']['latitude'] 

# LETRA(CAPITAL) PARA DICA
letras_possiveis = []
letras_capital = list(capital)
for letra in capital:
    if letra != ' ' and letra != "'":
        letras_possiveis.append(letra)

# CORES PARA DICA
cores_presentes = []
cores = list(bandeira.keys())
# print(cores)
for cor in cores:
    if cor != 'outras':
        if bandeira[cor] != 0:
            cores_presentes.append(cor)

# para as dicas, pegar os valores (area, populacao,letras_possiveis,cores_presentes)
print('\n')

# info para developer, VERSAO FINAL TEM Q TER ISSO COMENTADO OU REMOVIDO
print('pais_escolhido: ', pais_escolhido)
# print('letras_possiveis: ', letras_possiveis)
# print('cores_presentes: ', cores_presentes)



tentativas = 20
lista_cor = []
lista_letras = []
area_lista = []
populacao_lista = []
continente_lista = []
verifica_area = 0
verifica_população = 0
verifica_continente = 0
distancia_lista = []
chutes = []


while tentativas > 0:
    print(fun.menu(tentativas))
    continuar_jogando = True
    # CONTINUAR JOGANDO
    while continuar_jogando:

        comando = input('Qual seu palpite? ' )

        # ACERTOU O CHUTE
        if comando == pais_escolhido:
            print('\033[1;36m *** Parabéns! Você acertou após {0} tentativas!'.format(20 - tentativas+1))
            print('\033[0;0m')
            # arrumar o jogar outra rodada do desisto e copiar o codigo aqui
            # isso eh como ta atualmente(incompleto) o "jogar novamente?"
            outra_rodada = input('Jogar novamente? [s|n] ' )
            if outra_rodada == 's':

                # OUTRO PAIS
                # PAIS ESCOLHIDO
                continentes = list(dic.keys())
                continente_escolhido = random.choice(continentes)
                pais_escolhido = fun.sorteia_pais(dic[continente_escolhido])

                # INFO do pais
                info_pais= dic[continente_escolhido][pais_escolhido]
                area = info_pais['area']
                populacao = info_pais['populacao']
                capital = info_pais['capital']
                bandeira = info_pais['bandeira']
                longitude_escolida = info_pais['geo']['longitude']
                latitude_escolida = info_pais['geo']['latitude'] 

                # LETRA(CAPITAL) PARA DICA
                letras_possiveis = []
                letras_capital = list(capital)
                for letra in capital:
                    if letra != ' ' and letra != "'":
                        letras_possiveis.append(letra)

                # CORES PARA DICA
                cores_presentes = []
                cores = list(bandeira.keys())
                for cor in cores:
                    if cor != 'outras':
                        if bandeira[cor] != 0:
                            cores_presentes.append(cor)

                print('\n')

                # info para developer, VERSAO FINAL TEM Q TER ISSO COMENTADO OU REMOVIDO
                # print('pais_escolhido: ', pais_escolhido)
                # print('letras_possiveis: ', letras_possiveis)
                # print('cores_presentes: ', cores_presentes)




                tentativas = 20
                lista_cor = []
                lista_letras = []
                area_lista = []
                populacao_lista = []
                continente_lista = []
                verifica_area = 0
                verifica_população = 0
                verifica_continente = 0
                distancia_lista = []
                chutes = []

                print(fun.menu(tentativas))
                print('\n \n')

                comando = input('Qual seu palpite? ' )

            elif outra_rodada != 's':       # nao jogar denovo
                print('\n \n Obrigado por jogar, volte sempre! \n \n')

                continuar_jogando == False
                exit()

        # ERROU O CHUTE 
        if comando != pais_escolhido and comando != 'desisto' and comando != 'inventario' and comando != 'dica':
            if comando in paises:
                tentativas -= 1
                # definir info pra distancia
                for continente in continentes:
                    if comando in dic[continente]:
                        continente_chute = continente
                info_chute = dic[continente_chute][comando]
                latitude_chute = info_chute['geo']['latitude'] 
                longitude_chute = info_chute['geo']['longitude']
                # definir distancia 
                distancia = fun.haversine(EARTH_RADIUS,latitude_chute,longitude_chute,latitude_escolida,longitude_escolida)
                # printar lista de distancias
                if comando not in chutes:
                    chutes.append(comando)
                    distancia_lista = fun.adiciona_em_ordem(comando,distancia,distancia_lista)
                    print(fun.distancias(distancia_lista))
                    print('\033[0;0m')
                    print('Você tem \033[1;36m {0} \033[0;0m tentativas'.format(tentativas))
                    print('\033[0;0m')
                else:
                    print("\n \n \033[1;36m Voce ja tentou esse pais e viu que nao deu certo, ta tentando ele denovo porque? \033[0;0m \n \n ")
                    print('\033[0;0m')
                    print(fun.distancias(distancia_lista))
                    print('\033[0;0m')
            else:
                print('Pais Desconhecido')

        # DESISTO NAO FEITO(RE-ESCOLHER O PAIS DEPOIS DE COMECAR UMA RODADA NOVA,[so copiar e colar o codigo usado no comeco???])!!!
        if comando == 'desisto':
            garantia = input('Tem certeza que deseja desistir da rodada? [s|n] ' )
            if garantia == 'n':
                print('Você tem {0} tentativas'.format(tentativas))
                comando = 0
                
            elif garantia == 's':
                print('Que pena, boa sorte na proxima vez.... PERDEDOR')
                outra_rodada = input('Jogar novamente? [s|n] ' )
                if outra_rodada == 's':
                    # OUTRO PAIS
                    # PAIS ESCOLHIDO
                    continentes = list(dic.keys())
                    continente_escolhido = random.choice(continentes)
                    pais_escolhido = fun.sorteia_pais(dic[continente_escolhido])
                    # INFO do pais
                    info_pais= dic[continente_escolhido][pais_escolhido]
                    area = info_pais['area']
                    populacao = info_pais['populacao']
                    capital = info_pais['capital']
                    bandeira = info_pais['bandeira']
                    longitude_escolida = info_pais['geo']['longitude']
                    latitude_escolida = info_pais['geo']['latitude'] 
                    # LETRA(CAPITAL) PARA DICA
                    letras_possiveis = []
                    letras_capital = list(capital)
                    for letra in capital:
                        if letra != ' ' and letra != "'":
                            letras_possiveis.append(letra)
                    # CORES PARA DICA
                    cores_presentes = []
                    cores = list(bandeira.keys())
                    for cor in cores:
                        if cor != 'outras':
                            if bandeira[cor] != 0:
                                cores_presentes.append(cor)
                    print('\n')
                    # info para developer, VERSAO FINAL TEM Q TER ISSO COMENTADO OU REMOVIDO
                    # print('pais_escolhido: ', pais_escolhido)
                    # print('letras_possiveis: ', letras_possiveis)
                    # print('cores_presentes: ', cores_presentes)
                    tentativas = 20
                    lista_cor = []
                    lista_letras = []
                    area_lista = []
                    populacao_lista = []
                    continente_lista = []
                    verifica_area = 0
                    verifica_população = 0
                    verifica_continente = 0
                    distancia_lista = []
                    chutes = []
                    print(fun.menu(tentativas))
                    print('\n \n')
                    comando = input('Qual seu palpite? ' )

                elif outra_rodada != 's':       # nao jogar denovo
                    print('\n \n Obrigado por jogar, volte sempre! \n \n')
                    continuar_jogando == False
                    exit()

        # INVENTARIO (FALTA ESPINA, FALAR COM BETO)
        if comando == 'inventario':
            print(fun.dica_menu(lista_cor,lista_letras,area_lista,populacao_lista,continente_lista))
            print(fun.distancias(distancia_lista))

        if comando == "dica":
            print(fun.mercado(verifica_area,verifica_população,verifica_continente))
        
        # DICA (FALTA ESPINA, FALAR COM BETO)
        while comando == 'dica':
        
            opc = int(input('Escolha sua opção: {} '.format(str(fun.opc_menu(verifica_area,verifica_população,verifica_continente)))))
            
            #Cor da bandeira
            if opc == 1:
                
                if tentativas > 4:
          
                    cor_escohida = str((random.choice(cores_presentes)))
                    cores_presentes.remove(cor_escohida)
                    lista_cor.append(cor_escohida)
                    
                    print(fun.dica_menu(lista_cor,lista_letras,area_lista,populacao_lista,continente_lista))
                
                    tentativas = tentativas - 4
                else:
                    print("Você não tem tentativas suficientes")
                
                break
            
            if opc == 2:
                
                if tentativas > 3:
                
                    letra_escolhida = str((random.choice(letras_possiveis)))
                    letras_possiveis.remove(letra_escolhida)
                    lista_letras.append(letra_escolhida)
                    
                    print(fun.dica_menu(lista_cor,lista_letras,area_lista,populacao_lista,continente_lista))

                    tentativas = tentativas - 3
                else:
                    print("Você não tem tentativas suficientes")
                    
                break
                
            if opc == 3:
                
                if verifica_area == 0:
                    
                    if tentativas > 6:
                        area_lista.append(str(area))
                        print(fun.dica_menu(lista_cor,lista_letras,area_lista,populacao_lista,continente_lista))
                    
                        verifica_area = verifica_area + 1
                        
                        tentativas = tentativas - 6
                        
                    else:
                        print("Você não tem tentativas suficientes")
                        
                    break
                else:
                    print("Opção invalida")
                
        
            if opc == 4:
                
                if verifica_população == 0:
                    
                    if tentativas > 5:
                    
                        populacao_lista.append(str(populacao))
                        print(fun.dica_menu(lista_cor,lista_letras,area_lista,populacao_lista,continente_lista))
                        
                        verifica_população = verifica_população + 1
                        
                        tentativas = tentativas - 5
                        
                    else:
                        print("Você não tem tentativas suficientes")    
                    
                    break    
                else:
                    print("Opção invalida")
            
            if opc == 5:
                
                if verifica_continente == 0:
                    
                    if tentativas > 7:
                        print(continente_escolhido)
                        
                        continente_lista.append(str(continente_escolhido))
                        print(fun.dica_menu(lista_cor,lista_letras,area_lista,populacao_lista,continente_lista))
                        
                        verifica_continente = verifica_continente + 1
                        tentativas = tentativas - 7
                    
                    else:
                        print("Você não tem tentativas suficientes")
                    
                    break
                    
                else:
                    print("Opção invalida")
            
            if opc == 0:
                print(fun.dica_menu(lista_cor,lista_letras,area_lista,populacao_lista,continente_lista))
                break


# FALTA
#   - arrumar erro das dicas (quando o usuario consegue pedir mais cores/letras do que tem disponiveis )