import math
import random

#Adiciona em Ordem
def adiciona_em_ordem(pais, distancia, lista):
    
    
    i = 0
    pais_escolhido = [pais, distancia]
    lista_ordenada = []

    if len(lista) == 0:
        lista_ordenada.append(pais_escolhido)
        return lista_ordenada

    while i < len(lista):
        
        if lista[i][1] < pais_escolhido[1]:
            lista_ordenada.append(lista[i])
    
        else:
            if pais_escolhido not in lista_ordenada:
                lista_ordenada.append(pais_escolhido)
                i = i - 1
            else:
                lista_ordenada.append(lista[i])
                
        i += 1
        
    if pais_escolhido not in lista_ordenada:
        lista_ordenada.append(pais_escolhido)
        

    return lista_ordenada

# esta na lista
def esta_na_lista(pais, lista):
    for lugar in lista:
        if pais == lugar[0]:
            return True
    else:
        return False
    
#Haversine
def haversine(r, lat1, long1, lat2, long2):    
    d = (r*2*math.atan2(math.sqrt(math.sin(math.radians(lat2-lat1)/2.0)**2+math.cos(math.radians(lat1))*math.cos(math.radians(lat2))*math.sin(math.radians(long2-long1)/2.0)**2),math.sqrt(1-(math.sin(math.radians(lat2-lat1)/2.0)**2+math.cos(math.radians(lat1))*math.cos(math.radians(lat2))*math.sin(math.radians(long2-long1)/2.0)**2))))
    return d

#Normaliza
def normaliza(dados):
    dsd = dict()
    for cont in dados:
        for pais in dados[cont]:
            
            dsd[pais] = dados[cont][pais]
            dsd[pais]['continente'] = cont
    return dsd

#Sorteia letra
def sorteia_letra(palavra, negadas):
    especiais = ['.', ',', '-', ';', ' ', "'"]
    liberadas = []
    barradas = []

    for items in especiais:
        negadas.append(items)

    for letra in palavra:
        if letra == letra.upper():
            neutra = letra.lower()
        else:
            neutra = letra
        if neutra in negadas:
            barradas.append(letra)
        else:
            if neutra not in liberadas:
                liberadas.append(letra)

    if len(liberadas) != 0:
        escolhida = random.choice(liberadas)
        escolhida = escolhida.lower()
        return escolhida
    else:
        return ''
    
    
#Sorteia País
def sorteia_pais(dic):
    
    r = random.choice(list(dic.keys()))    
    return r


#Menu do Jogo
def menu(tentativas):
    
    menu = """
 ============================ 
|                            |
| Bem-vindo ao Insper Países |
|                            |
 ==== Design de Software ==== 
 
 Comandos:
 
    dica       - entra no mercado de dicas
    desisto    - desiste da rodada
    inventario - exibe sua posição
    
Um país foi escolhido, tente adivinhar!
Você tem {0} tentativa(s)
""".format(tentativas)
    
    return str(menu)
    
#Menu do Mercado
def mercado():
    mercado_menu = """
Mercado de Dicas
----------------------------------------
1. Cor da bandeira  - custa 4 tentativas
2. Letra da capital - custa 3 tentativas
3. Área             - custa 6 tentativas
4. População        - custa 5 tentativas
5. Continente       - custa 7 tentativas
0. Sem dica
----------------------------------------"""
    

    
    return str(mercado_menu)
  
def cor2str(lista_cor, world):
    lista_cor_string = world + ', '.join(lista_cor)
    return str(lista_cor_string+"\n")

def letra2str(lista_letras, world):
    lista_letra_str = world + ', '.join(lista_letras)
    return str(lista_letra_str+"\n")

def area2str(area_lista,world):
    lista_area_str = world + ', '.join(area_lista)
    return str(lista_area_str+" Km"+"\n")

def populacao2str(populacao_lista,world):
    lista_populacao_str = world + ', '.join(populacao_lista)
    return str(lista_populacao_str)

def continente2str(continente_lista,world):
    lista_continente_str = world + ', '.join(continente_lista)
    return str(lista_continente_str)
    

    
def dica_menu(lista_cor,lista_letras,area_lista,populacao_lista,continente_lista):
    dica = """Dicas:
  """
    if len(lista_cor) > 0:
        dica += str(cor2str(lista_cor,"  - Cores da bandeira: "))
    
    if len(lista_letras) > 0:
        dica += str(letra2str(lista_letras,"    - Letras da capital: "))
        
    if len(area_lista) > 0:
        dica += str(area2str(area_lista,"    - Área: "))
        
    if len(populacao_lista) > 0:
        dica += str(letra2str(populacao_lista,"    - População: "))
        
    if len(continente_lista) > 0:
        dica += str(letra2str(continente_lista,"    - Continente: "))
        
        
    return dica
    
    
    
