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


# def adiciona_em_ordem(pais, distancia, lista):
    
#     pais_escolhido = [pais, distancia]
#     lista_ordenada = []

#     if len(lista) == 0:
#         lista_ordenada.append(pais_escolhido)
#         return lista_ordenada

#     for i in range(len(lista)):
        
#         if lista[i][1] < pais_escolhido[1]:
#             lista_ordenada.append(lista[i])
    
#         else:
#             if pais_escolhido not in lista_ordenada:
#                 lista_ordenada.append(pais_escolhido)
#                 i = i - 1
#             else:
#                 lista_ordenada.append(lista[i])
        
#     if pais_escolhido not in lista_ordenada:
#         lista_ordenada.append(pais_escolhido)
        

#     return lista_ordenada