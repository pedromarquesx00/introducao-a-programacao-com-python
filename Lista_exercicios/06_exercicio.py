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

dep_inicial = float(input("Entre com o valor do deposito inicial: "))
dep_mensal = float(input("Entre com o deposito mensal: "))
juros = int(input("Entre com a taxa de juros: "))

meses = 1
saldo = dep_inicial
total_juros = 0
total_depositado = dep_inicial

while meses <= 24:
    juros_mes = saldo * (juros / 100)
    saldo = saldo + juros_mes
    total_juros = total_juros + juros_mes

    print(f"Mês: {meses}: {round(saldo,2)}")

    if meses < 24:
        saldo += dep_mensal
        total_depositado += dep_mensal
    
    meses += 1


print(f"\nTotal depositado: {round(total_depositado,2)}")
print(f"Saldo final: R${round(saldo,2)}")
print(f"Total de juros ganhos: R${round(total_juros,2)}")

# %% Exercicio 5.13
valor_inicial = float(input("Entre com o valor inicial da dívida: "))
juros_mes = int(input("Entre com a taxa de juros: "))
pago_mensal = float(input("Entre com o valor que será pago mensalmente: "))

if pago_mensal <= valor_inicial * (juros_mes / 100):
    print("ATENÇÃO: Valor pago mensalmente não cobre nem os juros!")
else:
    meses = 0
    divida = valor_inicial
    total_pago = 0
    total_juros = 0

    while divida > 0:
        juros = divida * (juros_mes / 100)
        if pago_mensal >= divida + juros:
            pagamento = divida + juros
            total_pago = total_pago + pagamento
            total_juros = total_juros + juros_mes 
            meses = meses + 1
        
            print(f"Mês: {meses}",
                  f"\nPagamento final de: R$ {round(pagamento,2)}. Quitou a divida")
            divida = 0

        else:
            divida = divida + juros - pago_mensal
            total_pago = total_pago + pago_mensal
            total_juros = total_juros + juros
            meses = meses + 1
            print(f"Mês {meses}: Dívida atual: R$ {divida:.2f}")
            
    print(f"Divida quitada em {meses} meses")
    print(f"Total pago: R$ {round(total_pago,2)}")
    print(f"Total de juro pagos: R$ {round(total_juros,2)}")

# %% Exercicio 5.14
soma = 0
quantidade = 0

while True:
    num = int(input("Entre com o número: "))
    if num != 0:
        soma += num
        quantidade += 1
    else:
        break

if quantidade > 1:
    media = soma / quantidade
    print(f"Quantidade: {quantidade}")
    print(f"Soma: {soma}")
    print(f"Média: {round(media,2)}")
else:
    print("Nenhum número digitado")

# %% Exercicio 5.15
# Depois deixarei esse código mais bonito
total = 0

while True:
    codigo = int(input('Entre com o código do produto: '))
    if codigo == 0:
        break

    if codigo == 1:
        preco = 0.50
    elif codigo == 2:
        preco = 1.00
    elif codigo == 3:
        preco = 4.00
    elif codigo == 5:
        preco = 7.00
    elif codigo == 9:
        preco = 8.00
    else:
        print("Código inválido!")
        continue

quantidade = int(input(f"Quantidade do produto {codigo}: "))
subtotal = preco * quantidade
total += subtotal
    
print(f"Subtotal: R$ {subtotal}")
print(f"Total comprado: {total}")

# %% Exercicio 5.16
valor = int(input("Digite o valor a pagar: "))
cedulas = 0
atual = 50
apagar = valor

while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        print(f"{cedulas} Cédulas de R$ {atual}")
        if apagar == 0:
            break

        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0
# %%