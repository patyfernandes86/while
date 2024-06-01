# Inicializando variáveis para contar números, somar e armazenar a entrada do usuário
contador = 0
soma = 0

# Loop para receber entrada do usuário até que 0 seja digitado
while True:
    entrada = int(input("Digite um número inteiro (ou 0 para sair): "))
    
    # Se 0 for digitado, sair do loop
    if entrada == 0:
        break
    
    # Adicionar 1 ao contador a cada número digitado
    contador += 1
    
    # Adicionar o número à soma total
    soma += entrada

# Verificar se pelo menos um número foi digitado para evitar divisão por zero
if contador > 0:
    # Calcular a média
    media = soma / contador
    
    # Exibir resultados
    print("Quantidade de números digitados:", contador)
    print("Soma dos números:", soma)
    print("Média aritmética dos números:", media)
else:
    print("Nenhum número foi digitado.")