# inmportamos el modulo random para ocupar algunas de sus funciones
import random
# elegimos con la funcion random.randrange el numero de intentos
intentos = random.randrange(5,10)
# creamos una lista con las palabras que se podrian adivinar
palabras = ["bombero","colegio","hospital","mercado","gallina","escoba","azucar","panaderia"]
# elegimos aleatoriamente una palabra de la lista que creamos antes
palabra_elegida = random.choice(palabras)
# elegimos aleatoriamente la cantidad de letras ocultas
letras_ocultas = int(len(palabra_elegida) * 0.6)
# elegimos aleatoriamente las posiciones de las letras que se ocultaran de la palabra
posicion_oculta = random.sample(range(len(palabra_elegida)), letras_ocultas)
# variable donde guardaremos la palabra elegida con algunas posiciones ocultas
palabra_oculta = ""

# obtenemos cada letra con su indice de la palabra a adivinar
for index, letra in enumerate(palabra_elegida):
    # se crea la palabra oculta cambiando la letra por _ siempre que el indice de la
    # palabra elegida coincida con la posicion a ocultar obtenida en la variable posicion oculta
    # si no, se mantiene la letra
    palabra_oculta += "_" if index in posicion_oculta else letra

# siempre que no se hayan acabado los intentos
while intentos > 0:
    print(f"Adivina la palabra {palabra_oculta}, tienes {intentos} intentos.")
    text = input("introduce una letra o la solución completa: ")
    # si el texto ingresado es un caracter se compara solo un caracter
    if len(text) == 1:
        # creamos una nueva varible para ir revelando los aciertos
        nueva_palabra_oculta = ""
        flag = False
        # compara la letra ingresada con cada letra de la palabra a adivinar
        for index, letra in enumerate(palabra_elegida):
            # si la letra ingresada coincide con alguna letra de la palabra a adivinar
            # y en la posicion de esa letra en la palabra oculta, la letra esta oculta
            # se reescribe en otra variable, revelando la palabra que estaba oculta
            if text == letra and palabra_oculta[index] == "_":
                nueva_palabra_oculta += text
                flag = True
            # si no, se reescribe en otra variable sin revelar la letra
            else:
                nueva_palabra_oculta += palabra_oculta[index]
        
        # se hace un intercambio entre variables
        palabra_oculta = nueva_palabra_oculta

        # si flag es True quiere decir que se adivino almenos una letra
        if flag:
            # si la palabra elegida es igual a la palabra oculta quiere decir que se adivinaron todas las letras
            if palabra_elegida == palabra_oculta:
                print(f"Has acertado, la palabra era: {palabra_elegida}.")
                break
            # si no, solo se ha adivinado una letra
            else:
                print("Has acertado la letra")
        # si flag es False quiere decir que no se adivino la letra
        else:
            print("Letra no encontrada o ya visible")
            # y se resta un intento, cuando los intentos lleguen a cero, la condicion del
            # while ya no se cumple y se sale del ciclo
            intentos -= 1
    # si el texto ingresado es igual al tamaño de la letra, se compara toda la cadena
    elif len(text) == len(palabra_elegida):
        # si las cadenas son iguales
        if text == palabra_elegida:
            # ha ganado
            print(f"Has acertado, la palabra era: {palabra_elegida}.")
            break
        # si no, quiere decir que la palabra ingresada no era la que se tiene que adivinar
        else:
            print("La palabra no es correcta")
            # se resta un intento
            intentos -= 1
    # si el texto ingresado no es un solo caracter y tampoco es igual al tamaño de la palabra a adivinar 
    # decimos que la entrada es invalida
    else:
        print("Texto invalido")
# cuando sale del ciclo quiere decir que no ha adivinado la palabra por lo tanto imprimimos el siguiente mensaje
if intentos == 0:
    print(f"Has perdido. La palabra oculta era {palabra_elegida}.")