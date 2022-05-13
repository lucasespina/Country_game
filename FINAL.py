import math
import random
import banco_de_dados
import fun 

dic = banco_de_dados.DADOS
EARTH_RADIUS = 6371

# PAIS ESCOLHIDO
continentes = list(dic.keys())
continente_escolhido = random.choice(continentes)
pais_escolhido = fun.sorteia_pais(dic[continente_escolhido])
print('pais_escolhido: ', pais_escolhido)

# INFO do pais
info_pais= dic[continente_escolhido][pais_escolhido]
area = info_pais['area']
populacao = info_pais['populacao']
capital = info_pais['capital']
bandeira = info_pais['bandeira']

# LETRA(CAPITAL) PARA DICA
letras_possiveis = []
letras_capital = list(capital)
for letra in capital:
    if letra != ' ' and letra != "'":
        letras_possiveis.append(letra)
print('letras_possiveis: ', letras_possiveis)

# CORES PARA DICA
cores_presentes = []
cores = list(bandeira.keys())
# print(cores)
for cor in cores:
    if bandeira[cor] != 0:
        cores_presentes.append(cor)
print('cores_presentes: ', cores_presentes)

# para as dicas, pegar os valores (area, populacao,letras_possiveis,cores_presentes)
print('\n')

tentativas = 20
lista_cor = []
lista_letras = []
area_lista = []
populacao_lista = []
continente_lista = []
verifica_area = 0
verifica_população = 0
verifica_continente = 0

while tentativas > 0:

    print(fun.menu(tentativas))
    
    continuar_jogando = True
    
    # CONTINUAR JOGANDO
    while continuar_jogando:

        comando = input('Qual seu palpite? ' )


        if comando == pais_escolhido:
            print('*** Parabéns! Você acertou após {0} tentativas!'.format(20 - tentativas+1))
            # arrumar o jogar outra rodada do desisto e copiar o codigo aqui
            # isso eh como ta atualmente(incompleto) o "jogar novamente?"
            outra_rodada = input('Jogar novamente? [s|n] ' )
            if outra_rodada == 's':
                tentativas = 20
                print(fun.menu(tentativas))
                print('\n \n')
                # comando = input('Qual seu palpite? ' )
            elif outra_rodada != 's':       # nao jogar denovo
                continuar_jogando == False
                exit()

        if comando != pais_escolhido and comando != 'desisto' and comando != 'inventario' and comando != 'dica':
            tentativas -= 1
            # PRINTAR BAGO DO DICAS + CHUTES COM DISTANCIAS
            print('Você tem {0} tentativa(s)'.format(tentativas))





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
                    tentativas = 20
                    print(fun.menu(tentativas))
                    print('\n \n')
                    # comando = input('Qual seu palpite? ' )
                elif outra_rodada != 's':       # nao jogar denovo
                    continuar_jogando == False
                    exit()

        # INVENTARIO (FALTA ESPINA, FALAR COM BETO)
        if comando == 'inventario':
            print('Distâncias: \n Dicas: \n  - Cores da bandeira: {0} \n  - Letras da capital: {1} \n  - Área: {2} \n  - População: {3} habitantes'.format(cores_presentes,letras_possiveis,area,populacao))
            comando = input('Qual seu palpite? ' )

        if comando == "dica":
            print(fun.mercado(verifica_area,verifica_população,verifica_continente))
        
        # DICA (FALTA ESPINA, FALAR COM BETO)
        while comando == 'dica':
          
            opc = int(input('Escolha sua opção [0|1|2|3|4|5]: '))
            
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