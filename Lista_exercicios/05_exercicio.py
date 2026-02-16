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

# %% Exercicio 4.8
a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))
operacao = input("Entre com a operação: soma (+), subtração (-), multiplicação (*), divisão (/)")

if operacao == "+":
    print(f"Soma: {a + b}")
elif operacao == "-":
    print(f"Subtração: {a - b}")
elif operacao == "*":
    print(f"Multlicação: {a * b}")
elif operacao == "/":
    print(f"Divisão: {a / b}")
else:
    print("Operação inválida. Entre com o símbolo correto!")

# %% Exercicio 4.9
valor_casa = float(input("Entre com o valor da casa: "))
salario = float(input("Entre com seu salário: "))
meses = int(input("Entre com o número de meses a serem pagos: "))

prestacao = valor_casa / meses

base = salario * 0.30

if prestacao > base:
    print("Emprestimo recusado")
else:
    print("Emprestimo aprovado")

# %% Exercicio 4.10
kwh = float(input("Entre com a quantidade de kWh consumido: "))
tipo = input("Entre com o tipo de intalação: ",
             "R para residências;",
             "I para industrias",
             "C para comércio.")

if tipo == "R":
    if kwh <= 500:
        preco = kwh * 0.40
        print(f"Preço a ser pago: R$ {preco}")
    else:
        preco = kwh * 0.65
        print(f"Preço a ser pago: R$ {preco}")
elif tipo == "C":
    if kwh <= 1000:
        preco = kwh * 0.55
        print(f"Preço a ser pago: R$ {preco}")
    else:
        preco = kwh * 0.60
        print(f"Preço a ser pago: R$ {preco}")
elif tipo == "I":
    if kwh <= 5000:
        preco = kwh * 0.55
        print(f"Preço a ser pago: R$ {preco}")
    else:
        preco = kwh * 0.60
        print(f"Preço a ser pago: R$ {preco}")
else:
    print("Entre com o tipo válido.")