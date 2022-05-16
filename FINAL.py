import math
import random
import banco_de_dados
import fun 

dic = banco_de_dados.DADOS
paises = banco_de_dados.paises
EARTH_RADIUS = 6371
outra_rodada_final = True
while outra_rodada_final == True:

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
    contagem_bandeira = 0
    contagem_letra = 0


    while tentativas > 0:
        if tentativas <= 0:
            break
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
                    contagem_bandeira = 0
                    contagem_letra = 0


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
                        if tentativas <= 0:
                            break
                    else:
                        print("\n \n \033[1;36m Voce ja tentou esse pais e viu que nao deu certo, ta tentando ele denovo porque? \033[0;0m \n \n ")
                        print('\033[0;0m')
                        print(fun.distancias(distancia_lista))
                        print('\033[0;0m')
                else:
                    print('Pais Desconhecido')

            # DESISTO 
            if comando == 'desisto':
                garantia = input('Tem certeza que deseja desistir da rodada? [s|n] ' )
                if garantia == 'n':
                    print('Você tem {0} tentativas'.format(tentativas))
                    comando = 0
                    
                elif garantia == 's':
                    print('Que pena, boa sorte na proxima vez.... O pais era {0}'.format(pais_escolhido))
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
                        contagem_bandeira = 0
                        contagem_letra = 0
                        print(fun.menu(tentativas))
                        print('\n \n')
                        # comando = input('Qual seu palpite? ' )

                    elif outra_rodada != 's':       # nao jogar denovo
                        print('\n \n Obrigado por jogar, volte sempre! \n \n')
                        continuar_jogando == False
                        exit()

            # INVENTARIO
            if comando == 'inventario':
                print(fun.dica_menu(lista_cor,lista_letras,area_lista,populacao_lista,continente_lista))
                print(fun.distancias(distancia_lista))

            if comando == "dica":
                print(fun.mercado(verifica_area,verifica_população,verifica_continente))
            
            # DICA (FALTA ESPINA, FALAR COM BETO)
            while comando == 'dica':
                
                opc = int(input('Escolha sua opção: {} '.format(str(fun.opc_menu(verifica_area,verifica_população,verifica_continente)))))
                if opc != 0 and opc != 1 and opc != 2 and opc != 3 and opc != 4 and opc != 5 :
                    print("Por favor responder 'Dicas' com uma das opcoes apresentadas")
                    # opc = int(input('Escolha sua opção: {} '.format(str(fun.opc_menu(verifica_area,verifica_população,verifica_continente)))))
                else:
                #Cor da bandeira
                    if opc == 1:
                        
                        if tentativas > 4:
                            if contagem_bandeira < len(cores_presentes):
                                cor_escohida = str((random.choice(cores_presentes)))
                                cores_presentes.remove(cor_escohida)
                                lista_cor.append(cor_escohida)
                            
                                print(fun.dica_menu(lista_cor,lista_letras,area_lista,populacao_lista,continente_lista))
                                contagem_bandeira += 1
                                tentativas = tentativas - 4
                            else:
                                print('\n \033[1;31m Essas sao as cores presentes  \033[0;0m \n ')
                                print('Você tem {0} tentativas'.format(tentativas))
                        else:
                            print(" \n \033[1;31mVocê não tem tentativas suficientes \033[0;0m \n")
                            print('Você tem {0} tentativas'.format(tentativas))
                        break
                    
                    elif opc == 2:
                        
                        if tentativas > 3:
                            if contagem_letra < len(letras_possiveis):
                                letra_escolhida = str((random.choice(letras_possiveis)))
                                letras_possiveis.remove(letra_escolhida)
                                lista_letras.append(letra_escolhida)
                            
                                print(fun.dica_menu(lista_cor,lista_letras,area_lista,populacao_lista,continente_lista))
                                contagem_letra += 1
                                tentativas = tentativas - 3
                            else:
                                print('\n \033[1;31m Essas sao todas as letras  \033[0;0m \n ')
                                print('Você tem {0} tentativas'.format(tentativas))
                        else:
                            print(" \n \033[1;31mVocê não tem tentativas suficientes \033[0;0m \n")
                            print('Você tem {0} tentativas'.format(tentativas))
                        break
                        
                    elif opc == 3:
                        
                        if verifica_area == 0:
                            
                            if tentativas > 6:
                                area_lista.append(str(area))
                                print(fun.dica_menu(lista_cor,lista_letras,area_lista,populacao_lista,continente_lista))
                            
                                verifica_area = verifica_area + 1
                                tentativas = tentativas - 6
                                print('Você tem {0} tentativas'.format(tentativas))
                            else:
                                print(" \n \033[1;31m Você não tem tentativas suficientes \033[0;0m \n")
                                print('Você tem {0} tentativas'.format(tentativas))
                                
                            break
                        else:
                            print("\n \033[1;31m Opção invalida \033[0;0m \n")
                            print('Você tem {0} tentativas'.format(tentativas))
                        
                    elif opc == 4:
                        
                        if verifica_população == 0:
                            
                            if tentativas > 5:
                            
                                populacao_lista.append(str(populacao))
                                print(fun.dica_menu(lista_cor,lista_letras,area_lista,populacao_lista,continente_lista))
                                
                                verifica_população = verifica_população + 1
                                tentativas = tentativas - 5
                                print('Você tem {0} tentativas'.format(tentativas))
                            else:
                                print(" \n \033[1;31m Você não tem tentativas suficientes \033[0;0m \n")
                                print('Você tem {0} tentativas'.format(tentativas))
                            
                            break    
                        else:
                            print("\n \033[1;31m Opção invalida \033[0;0m \n")
                            print('Você tem {0} tentativas'.format(tentativas))
                    
                    elif opc == 5:
                        
                        if verifica_continente == 0:
                            
                            if tentativas > 7:
                                print(continente_escolhido)
                                
                                continente_lista.append(str(continente_escolhido))
                                print(fun.dica_menu(lista_cor,lista_letras,area_lista,populacao_lista,continente_lista))
                                verifica_continente = verifica_continente + 1
                                tentativas = tentativas - 7
                                print('Você tem {0} tentativas'.format(tentativas))
                            else:
                                print(" \n \033[1;31mVocê não tem tentativas suficientes \033[0;0m \n")
                                print('Você tem {0} tentativas'.format(tentativas))
                            
                            break
                            
                        else:
                            print("\n \033[1;31m Opção invalida \033[0;0m \n")
                            print('Você tem {0} tentativas'.format(tentativas))
                    
                    elif opc == 0:
                        print(fun.dica_menu(lista_cor,lista_letras,area_lista,populacao_lista,continente_lista))
                        print('Você tem {0} tentativas'.format(tentativas))
                        break

            # else:
            #     print("Por favor responder 'Dicas' com uma das opcoes apresentadas")
# ACABOU AS TENTATIVAS
    print('ACABOU SUAS TENTATIVAS!')
    print('O pais era {0}'.format(pais_escolhido))
    outra_rodada = input('Voce quer jogar novamente? [s/n]')
    if outra_rodada == 's':
        outra_rodada_final = True
    elif outra_rodada == 'n':
        print('\n \n Obrigado por jogar, volte sempre! \n \n')
        continuar_jogando == False
        outra_rodada_final == False
        exit()
    else:
        print('Por favor responder [s/n]')
        outra_rodada = input('Voce quer jogar novamente? [s/n]')

# FALTA
#   - arrumar erro das dicas (quando o usuario consegue pedir mais cores/letras do que tem disponiveis )