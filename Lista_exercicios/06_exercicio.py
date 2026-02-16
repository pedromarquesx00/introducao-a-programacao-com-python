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