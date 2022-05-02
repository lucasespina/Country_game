def normaliza(dados):
  
    dsd = dict()
    
    for cont in dados:
        for pais in dados[cont]:
            
            dsd[pais] = dados[cont][pais]
            dsd[pais]['continente'] = cont
            
    return dsd