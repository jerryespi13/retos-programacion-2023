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

def tranformar(str):
    descomposicion = str.split("-")
    key = ""
    texto_final = ""
    for i in descomposicion:
        key = i[0]
        pos = len(i)
        texto_final += (teclado[key][pos - 1])
    print(texto_final)

cadena = "6-666-88-777-33-3-33-888"

tranformar(cadena)