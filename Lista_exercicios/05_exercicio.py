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

# %% Excercicio 4.4
# salárioacima de 1250 aumento de 10%
# inferiores ou iguais, acumento de 15%

salario = float(input("Entre com seu salário: "))

if salario > 1250:
    aumento = salario * 0.10
    salario2 = aumento + salario
    print(f"Com aumento de 10%, seu salário de {salario}, foi para {salario2}")
elif salario <= 1250:
    aumento = salario * 0.15
    salario2 = aumento + salario
    print(f"Com aumento de 15%, seu salário de {salario}, foi para {salario2}")