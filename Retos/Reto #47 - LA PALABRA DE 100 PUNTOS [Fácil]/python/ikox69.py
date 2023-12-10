letras = ["ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"]

def letra_con_acento(accento: str):
    match accento:
        case "Á":
            letra = "A"
        case "É":
            letra = "E"
        case "Í":
            letra = "I"
        case "Ó":
            letra = "O"
        case "Ú":
            letra = "U"
    return letra
def sustutuir_por_valor(letra):
    if letra in ["Á", "É", "Í", "Ó", "Ú"]:
            letra = letra_con_acento(letra)
    return letras[0].find(letra) + 1 #comienza en cero


def realiza_calculos(palabra):
    resultado = map(sustutuir_por_valor, palabra.upper())
    return sum(resultado)


while(True):
    palabra_introducida = input("Escribe una palabra: ")
    puntuacion = realiza_calculos(palabra_introducida)
    if (puntuacion) == 100:
        print(f"¡¡¡GRANDE!!!. Has conseguido la puntuación de {puntuacion} con la palabra: {palabra_introducida}")
        break
    else: 
        print(f"Sigue jugando. La puntuación de la palabra {palabra_introducida} es: {puntuacion}") 
        

