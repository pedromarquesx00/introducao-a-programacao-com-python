# %% Exercicio 3.7
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

soma = a + b

print(f"O valor da soma é: {soma}")
# %% Exercicio 3.8
m = float(input("Digite o valor em metros: "))

mili = m * 1000

print(f"O valor em milimetros é: {mili}")

# %% Exercicio 3.9
dia = int(input("digite o número de dias: "))
horas = int(input("digite as horas"))
min = int(input("digite os minutos: "))
seg = int(input("digite os segundos: "))

total_seg = (dia * 24 * 3600) + (horas * 3600) + (min * 60) + seg

print(f"O total de segundos é: {total_seg}")

# %% Exercicio 3.10
salario = float(input("Entre com o salário: "))
aumento = int(input("Entre com a procentagem de aumento: "))

valor_aumento = salario * (aumento / 100)

salario_novo = salario + valor_aumento
print(f"Com o aumento de {aumento}%, o salário foi de {salario} para novo {salario_novo}")

# %% Exercicio 3.11
merc = float(input("Digite o preço da mercadoria: "))
desc = int(input("Digite o valor do desconto: "))

valor_desc = merc * (desc / 100)

merc_novo = merc - valor_desc

print(f"O valor do desconto: {round(valor_desc, 2)}%. Novo preço: {merc_novo}")

# %% Exercicio 3.12
dist = float(input("Digite a distância: "))
veloci = float(input("Digite a velocidade média: "))

tempo = dist / veloci

print(f"O tempo da viajem é de: {round(tempo)} horas")

# %% Exercicio 3.13
celsius = int(input("Entre com o valor em Celsius: "))

f = ((9 * celsius) / 5) + 32

print(f"A temperatura {celsius} em Fahrenheit é: {f}")

# %% 