# %% Exercicio 4.2

velocidade = int(input("Entre com a velocidade do carro: "))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"Você recemeu uma multa de: {multa}")