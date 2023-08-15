leet = {
    "A":"4",
    "B":"I3",
    "C":"[",
    "D":")",
    "E":"3",
    "F":"|=",
    "G":"&",
    "H":"#",
    "I":"1",
    "J":",_|",
    "K":">|",
    "L":"1",
    "M": "/\/\\",
    "N": " ^/",
    "O": "0", 
    "P": " |*", 
    "Q": "(_,)",
    "R": "I2", 
    "S": "5", 
    "T": "7", 
    "U": "(_)", 
    "V": "\/", 
    "W": "\/\/", 
    "X": "><", 
    "Y": "j", 
    "Z": "2",
    "1": "L", 
    "2": "R", 
    "3": "E", 
    "4": "A", 
    "5": "S", 
    "6": "b", 
    "7": "T", 
    "8": "B", 
    "9": "g", 
    "0": "o"
}
texto_traducido = ""
texto_a_traducir = input("Ingrese texto a traducir: ")

for i in texto_a_traducir:
    if i.upper() in leet.keys():
        texto_traducido += leet[i.upper()]
    else:
        texto_traducido += i
print(texto_traducido)