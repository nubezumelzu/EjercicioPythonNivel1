def casoToList(caso):
    def getSubString(i, string):
        subString, j = "", i
        for char in string:
            if char == ")":
                break
            else:
                subString += char
            j+=1
        return subString, j
    final = []
    cadena = ""
    i, flag = 0, False
    while( i < len(caso)):
        if caso[i] == "(":
            cadena, i = getSubString(i=i+1, string=caso[i+1:])
            final.append(cadena)
        else:
            final.append(caso[i])
        i+=1
    return [list(element) for element in final]

def producto(elemento, lista):
    if len(lista) == 0:
        return elemento
    else:
        aux = []
        for char in elemento:
            for char2 in lista[0]:
                aux.append(char+char2)
        return producto(elemento=aux, lista=lista[1:])

#resultados = producto(elemento=caso[0], lista=caso[1:]) 

def proceso (caso, diccionario):   
    casoLimpio = casoToList(caso)
    tokenSeparados = producto(casoLimpio[0], casoLimpio[1:])
    contador = 0
    for token in tokenSeparados:
        if token in diccionario:
            contador +=1

    return contador  


datos = input()              #Ingresar Longitud, Lineas y casos de prueba, ejemplo: 3 5 4
lineaSeparada = datos.split()
l = int(lineaSeparada[0])
d = int(lineaSeparada[1])
n = int(lineaSeparada[2])

diccionario = []
for i in range(d):
    linea = input()  #Ingresar Lineas de diccionario
    diccionario.append(linea)

casoPrueba = []
for i in range(n):
    linea = input()  #Ingresar Casos de Pruebas
    casoPrueba.append(linea)

for i in range(len(casoPrueba)):
    contador = proceso (casoPrueba[i], diccionario)
    caso = i+1
    print("Case #" + str(caso) + ": " + str(contador))



