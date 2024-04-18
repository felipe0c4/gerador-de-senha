import random

alfabeto = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
    "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
    ]


numeros = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9"
]

simbs = [
    "!", "@", "#", "$", "%", "&", "*", "_", 
]


lista = []


for _ in range(10):
    c = random.choice(alfabeto)
    d = random.choice(numeros)
    e = random.choice(simbs)
    lista.append(c)
    lista.append(e)
    lista.append(d)
    
string = ''.join(lista)

print(string)