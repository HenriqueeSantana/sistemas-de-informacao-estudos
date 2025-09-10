# aula7.py
# Aula 7 - Condicionais e Comparações

# Solicita dois números ao usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Verifica qual número é maior ou se são iguais
if num1 > num2:
    print(f"O primeiro número ({num1}) é maior.")
elif num2 > num1:
    print(f"O segundo número ({num2}) é maior.")
else:
    print("Os números são iguais.")

# Verifica se a soma é par ou ímpar
soma = num1 + num2
if soma % 2 == 0:
    print(f"A soma {soma} é par.")
else:
    print(f"A soma {soma} é ímpar.")

# Verifica se ambos são positivos
if num1 > 0 and num2 > 0:
    print("Ambos os números são positivos.")
