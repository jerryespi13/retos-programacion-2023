import random
intentos = random.randrange(5,10)
palabras = {
    1:"bombero",
    2:"colegio",
    3:"hospital",
    4:"mercado",
    5:"gallina",
    6:"escoba",
    7:"azucar",
    8:"panaderia"
}
palabra_elegida = random.choice(palabras)
letras_ocultas = int(len(palabra_elegida) * 0.6)
posicion_oculta = random.sample(range(len(palabra_elegida)), letras_ocultas)
palabra_oculta = ""

for index, letra in enumerate(palabra_elegida):
    palabra_oculta += "_" if index in posicion_oculta else letra
while intentos > 0:
    print(f"Adivina la palabra {palabra_oculta}, tienes {intentos} intentos.")
    text = input("introduce una letra o la solución completa: ")
    if len(text) == 1:
        nueva_palabra_oculta = ""
        flag = False
        for index, letra in enumerate(palabra_elegida):
            if text == letra and palabra_oculta[index] == "_":
                nueva_palabra_oculta += text
                flag = True
            else:
                nueva_palabra_oculta += palabra_oculta[index]
        
        palabra_oculta = nueva_palabra_oculta

        if flag:
            if palabra_elegida == palabra_oculta:
                print(f"Has acertado, la palabra era: {palabra_elegida}.")
                break
            else:
                print("Has acertado la letra")
        else:
            print("Letra no encontrada o ya visible")
            intentos -= 1
    elif len(text) == len(palabra_elegida):
        if text == palabra_elegida:
            print(f"Has acertado, la palabra era: {palabra_elegida}.")
            break
        else:
            print("La palabra no es correcta")
            intentos -= 1
    else:
        print("Texto invalido")
if intentos == 0:
    print(f"Has perdido. La palabra oculta era {palabra_elegida}.")