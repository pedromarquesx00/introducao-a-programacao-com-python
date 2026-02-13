# %% Exercicio 3.5
a = 5
b = 1
c = True
d = True

a > b and c or d
# %% Exercicio 3.6

materia1 = float(input("Digite sua nota da materia 1: "))
materia2 = float(input("Digite sua nota da materia 2: "))
materia3 = float(input("Digite sua nota da materia 3: "))

nota_final = (materia1 + materia2 + materia3) / 3

if nota_final >= 7:
    print(f"Sua nota é: {nota_final}. Parabéns! Você está aprovado!!!")
else:
    print(f"Sua nota é: {nota_final}. Você está reprovado.")

