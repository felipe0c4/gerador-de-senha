import random

caracteres = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
    "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "1", "2", "3", "4", "5", "6", "7", "8", "9","!", "@", "#", "$", "%",
     "&", "*", "_", 
    ]


lista = []


for _ in range(16):
    c = random.choice(caracteres)
    lista.append(c)
    
string = ''.join(lista)

print(string)
