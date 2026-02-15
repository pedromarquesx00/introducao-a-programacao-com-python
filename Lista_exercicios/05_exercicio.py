# %% Exercicio 4.2

velocidade = int(input("Entre com a velocidade do carro: "))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"Você recemeu uma multa de: {multa}")

# %% Exercicio 4.3
a = int(input("Entre com o primeiro número: "))
b = int(input("Entre com o segundo número: "))
c = int(input("Entre com o terceiro número: "))

if a > b and a > c:
    print(f"Maior número: {a}")
elif b > a and b > c:
    print(f"Maior número: {b}")
else:
    print(f"Maior número: {c}")