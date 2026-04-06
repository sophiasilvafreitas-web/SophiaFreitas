# Solicita ao usuário o primeiro número
numero1 = float(input("Digite o primeiro número: "))

# Solicita ao usuário o segundo número
numero2 = float(input("Digite o segundo número: "))

# Solicita ao usuário a operação desejada (+, -, *, /)
operacao = input("Digite a operação (+, -, *, /): ")

# Verifica qual operação foi escolhida
if operacao == "+":
    # Realiza a soma
    resultado = numero1 + numero2
    # Exibe o resultado
    print("Resultado:", resultado)

elif operacao == "-":
    # Realiza a subtração
    resultado = numero1 - numero2
    # Exibe o resultado
    print("Resultado:", resultado)

elif operacao == "*":
    # Realiza a multiplicação
    resultado = numero1 * numero2
    # Exibe o resultado
    print("Resultado:", resultado)

elif operacao == "/":
    # Verifica se o segundo número é diferente de zero para evitar erro
    if numero2 != 0:
        # Realiza a divisão
        resultado = numero1 / numero2
        # Exibe o resultado
        print("Resultado:", resultado)
    else:
        # Exibe mensagem de erro caso tente dividir por zero
        print("Erro: divisão por zero não é permitida.")

else:
    # Caso a operação digitada seja inválida
    print("Operação inválida.")
