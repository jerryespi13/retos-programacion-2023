teclado = {
    "1":[",",".","?","!"],
    "2":["a","b","c"],
    "3":["d","e","f"],
    "4":["g","h","i"],
    "5":["j","k","l"],
    "6":["m","n","o"],
    "7":["p","q","r","s"],
    "8":["t","u","v"],
    "9":["w","x","y","z"],
    "0":[" "]
}

def tranformar(cadena):
    key = ""
    texto_final = ""
    for i in cadena.split("-"):
        for k in range(len(i)):
            if i[k] != i[0]:
                exit( print("Por favor usa el formato correcto"))

        key = i[0]
        pos = len(i) % len(teclado[key])
        texto_final += (teclado[key][pos - 1])
    return texto_final.upper()


print(tranformar("5-33-777-777-999"))
print(tranformar("2222"))