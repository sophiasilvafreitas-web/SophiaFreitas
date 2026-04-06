# Solicita ao usuário o valor do capital inicial (dinheiro investido)
capital = float(input("Digite o capital inicial: "))

# Solicita ao usuário a taxa de juros (em porcentagem)
taxa = float(input("Digite a taxa de juros (%): "))

# Solicita ao usuário o tempo (em meses ou anos, conforme desejado)
tempo = float(input("Digite o tempo: "))

# Converte a taxa de porcentagem para decimal (ex: 5% -> 0.05)
taxa_decimal = taxa / 100

# Calcula o valor dos juros simples usando a fórmula: J = C * i * t
juros = capital * taxa_decimal * tempo

# Calcula o montante final (capital + juros)
montante = capital + juros

# Exibe o valor dos juros
print("Juros:", juros)

# Exibe o valor total (montante)
print("Montante final:", montante)
