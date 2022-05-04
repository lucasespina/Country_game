def esta_na_lista(pais, lista):
    for lugar in lista:
        if pais in lugar[0]:
            return True
    else:
        return False