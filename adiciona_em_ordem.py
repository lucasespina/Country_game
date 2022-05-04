def adiciona_em_ordem(pais, distancia, lista):
    
    list = []
    list.append(pais)
    list.append(distancia)
    i = 0
    
    list1 = []
    
    while i < len(lista):
        
        if lista[i][1] < distancia:
           list1.append(lista[i])
        list1.append(list)
        
        i = i + 1
    
    return list1



lista = [
    ['libia', 3678],
    ['franca', 3998],
    ['egito', 5008],
    ['india', 9919],
    ['japao', 13836]
]

pais = "siria"
distancia = 5919

print(adiciona_em_ordem(pais,distancia,lista))