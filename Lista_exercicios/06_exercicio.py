# %% Exercicio 5.1
x = 1

while x <= 100:
    print(x)
    x += 1

# %% Exercicio 5.2
x = 50

while x <= 100:
    print(x)
    x += 1

# %% Exercicio 5.3
# Import time para ficar legal

import time as t
x = 10

while x > 0:
    t.sleep(1)
    print(x)
    x -= 1
print("FOGO")

# %% Exercicio 5.4
fim = int(input("Digite o último número a imprimir: "))

x = 1
while x <= fim:
   print(x)
   x += 2

# %% Exercidio 5.5
fim = int(input("Digite o último número a imprimir: "))

x = 0
while x <= fim:
   print(x)
   x += 3

# %% Exercicio 5.6

n = int(input("Tabuada de: "))

x = 1

while x <= 10:
    print(f"{n} x {x} = {n * x}")
    x = x + 1

# %% Exercicio 5.7

n = int(input("Tabuada de: "))
inicio = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))

x = inicio

while x <= fim:
    print(f"{n} x {x} = {n * x}")
    x = x + 1

# %% Exercicio 5.8
a = int(input("Entre com o primeiro número: "))
b = int(input("Entre com o segundo número: "))

