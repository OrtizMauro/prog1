def merge(lista1, lista2):
    """
    merge se encargara de intercalar los elementos de las dos
    divisiones.
    """
    i, j = 0, 0 # Variables de incremento
    result = [] # Lista de resultado
 
   # Intercalar ordenadamente
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            result.append(lista1[i])
            i += 1
        else:
            result.append(lista2[j])
            j += 1
 
   # Agregamos los resultados a la lista
    result += lista1[i:]
    result += lista2[j:]
 
    # Retornamos el resultados
    return result