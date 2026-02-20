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
n = int(input("Tabuada de: "))
a = int(input("Entre com o primeiro número: "))
b = int(input("Entre com o segundo número: "))

if a <= b:
    x = a
    while x <= b:
        soma1 = (f"{n} + " * (x - 1) + f"{n}").strip()
        soma2 = (f"{x} + " * (n - 1) + f"{x}").strip()
        print(f"{n} x {x} = {soma1} = {soma2} = {n * x}")
        x = x + 1
    
else:
    print("Erro")

# %% Exercicio 5.9
dividendo = int(input("Entre com o dividendo: "))
divisor = int(input("Entre com o divisor: "))

if divisor == 0:
    print("Não se faz divisão por zero!")
else:
    quociente = 0
    resto = dividendo

while resto >= divisor:
    resto = resto - divisor
    quociente = quociente + 1

print(f"Divisão inteira: {dividendo} ÷ {divisor} = {quociente}")
print(f"Resto: {resto}")

# %% Exercicio 5.10
pontos = 0
questao = 1

while questao <= 3:
    resposta = input(f"Resposta da questão: {questao}")
    if questao == 1 and (resposta == "B" or resposta == "b"):
        pontos += 1
    if questao == 2 and (resposta == "A" or resposta == "a"):
        pontos += 1
    if questao == 3 and (resposta == "D" or resposta == "d"):
        pontos += 1
    questao += 1
print(f"O aluno fez {pontos} ponto(s)")

# %% Exercicio 5.11

dep_inicial = float(input("Entre com o valor do deposito inicial: "))
juros = int(input("Entre com a taxa de juros: "))

meses = 1
saldo = dep_inicial
total_juros = 0

while meses <= 24:
    juros_mes = saldo * (juros / 100)
    saldo = saldo + juros_mes
    total_juros = total_juros + juros_mes

    print(f"Mês: {meses}: {round(saldo,2)}")
    meses += 1

print(f"\nSaldo final: R${round(saldo,2)}")
print(f"Total de juros ganhos: R${round(total_juros,2)}")

# %% 
