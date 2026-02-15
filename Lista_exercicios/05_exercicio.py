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
salario = float(input("Entre com seu salário: "))

if salario > 1250:
    aumento = salario * 0.10
    salario2 = aumento + salario
    print(f"Com aumento de 10%, seu salário de {salario}, foi para {salario2}")
elif salario <= 1250:
    aumento = salario * 0.15
    salario2 = aumento + salario
    print(f"Com aumento de 15%, seu salário de {salario}, foi para {salario2}")

# %% Exercicio 4.5
idade = int(input("Digite a idade do seu carro: "))

if idade <= 3:
    print("Seu carro é novo")
else:
    print("Seu carro é velho")

# %% Exercicio 4.6

distancia = int(input("Digite a distância que você quer percorrer(em km): "))

if distancia <= 200:
    preco = distancia * 0.50
    print(f"O preço a ser pago: {preco}")
else:
    preco = distancia * 0.45
    print(f"O preço a ser pago: {preco}")

# %% Excercicio 4.7
categoria = int(input("Digite a categória do produto: "))

if categoria == 1:
    proco = 10
else:
    if categoria == 2:
        preco = 18
    else:
        if categoria == 3:
            preco = 23
        else:
            if categoria == 4:
                preco = 26
            else:
                if categoria == 5:
                    preco = 31
                else:
                    print("Categoria inválida, digite um valor entre 1 e 5!")
                    preco = 0
                
print(f"O preço do produto é: R${preco}")

# %% 