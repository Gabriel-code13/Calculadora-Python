# arquivo principal

# Declarando a variavel "sinal"
sinal = input("Qual operação deseja realizar ?")

# criando loop de repetição em caso de erro de digitação
while(sinal != '+' and sinal != '-' and sinal != '*' and sinal != '/'):
    print("\n Você digitou uma operação invalida!")
    sinal = input('\nQual operação deseja realizar ?')


# Declarando a variavel "numeroInicial"
numeroInicial = float(input("\nDigite o primeiro número..."))

# Declarando a variavel "numeroFinal"
numeroFinal = float(input("\nDigite p segundo número..."))

# Declarando a variavel "resultadoFinal"
resultadoFinal = 0

# Esquema de calculo 
if(sinal == '+'):
    resultadoFinal = numeroInicial + numeroFinal
    print(resultadoFinal)
elif(sinal == '-'):
    resultadoFinal = numeroInicial - numeroFinal
    print(resultadoFinal)
elif(sinal == '*'):
    resultadoFinal = numeroInicial * numeroFinal
    print(resultadoFinal)
elif(sinal == '/'):
    resultadoFinal = numeroInicial / numeroFinal
    print(resultadoFinal)