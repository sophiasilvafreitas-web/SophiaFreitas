# Solicita ao usuário que digite o tempo total em segundos
segundos = int(input("Digite o tempo em segundos: "))

# Calcula quantas horas existem no total de segundos
horas = segundos // 3600  # 1 hora = 3600 segundos

# Calcula o restante de segundos após retirar as horas
resto = segundos % 3600

# Calcula quantos minutos existem no restante
minutos = resto // 60  # 1 minuto = 60 segundos

# Calcula os segundos restantes após retirar os minutos
segundos_restantes = resto % 60

# Exibe o resultado da conversão
print("Tempo convertido:")
print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos_restantes)
