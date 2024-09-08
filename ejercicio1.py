#Elabore un programa para la Universidad de Florida que calcule los primeros 100 números de la siguiente serie 5, 8, 13, 21, ... sin mostrar el 13, y muestre la lista del resultado de los números.

def genSerie(n):
    serie = [5, 8]
    while len(serie) < n:
        sigNum = serie[-1] + serie[-2]
        serie.append(sigNum)
    return serie

def filtrarSerie(serie,numOmitir):
    return [num for num in serie if num != numOmitir]

primNum = genSerie (100)

resultado = filtrarSerie(primNum, 13)

print(f'El resultado de los 100 números de la serie son: {resultado}, recuerda que el número 13 se omitió.')