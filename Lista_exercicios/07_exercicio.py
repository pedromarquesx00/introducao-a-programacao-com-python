# %% Exercicio 6.1
notas = [0,0,0,0,0,0,0]
soma = 0
x = 0

while x < 7:
    notas[x] = float(input("Nota %d:" % x))
    soma += notas[x]
    x += 1
x = 0
while x < 7:
    print("Nota %d: %6.2f" % (x, notas[x]))
    x += 1
print("Média: %6.5f" % (soma/x))

# %% Listagem 6.7
numero = [0,0,0,0,0]
x = 0

while x < 5:
    numero[x] = int(input(f"Número: {x + 1}"))
    x += 1
while True:
    escolhido = int(input("Que posição você quer imprimir (o para sair): "))
    if escolhido == 0:
        break
    print("Você escolheu o número: %d" % (numero[escolhido-1]))

# %% Exercicio 6.2
# feito com lista pré-definida

l = [1,2,3]
v = [4,5,6]
j = l + v

j

# %% Exercicio 6.3
l = [1, 2, 3, 4, 5, 3, 2]
k = [1, 5, 6, 7, 8, 8, 9]

j = list(set(k + l))
j

# %%
