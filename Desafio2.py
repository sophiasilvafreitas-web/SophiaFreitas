# Solicita ao usuário que digite um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é divisível por 2 usando o operador de resto (%)
# Se o resto da divisão por 2 for igual a 0, o número é par
if numero % 2 == 0:
    # Exibe mensagem informando que o número é par
    print("O número é par.")
else:
    # Caso contrário, exibe que o número é ímpar
    print("O número é ímpar.")
