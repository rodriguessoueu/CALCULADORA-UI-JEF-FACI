while True:
    print("--- Calculadora ---")
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))    
    operacao = input("Escolha a operação (+, -, *, /): ") 

    if operacao == "+":
        resultado = numero1 + numero2
        print("O resultado da soma é: ", resultado)
        break
    elif operacao == "-":
        resultado = numero1 - numero2
        print("O resultado da subtração é: ", resultado)
        break
    elif operacao == "*":
        resultado = numero1 * numero2
        print("O resultado da multiplicação é: ", resultado)
        break  
    elif operacao == "/":
        if numero2 != 0:
            resultado = numero1 / numero2
            print("O resultado da divisão é: ", resultado)
        else:
            print("Erro: Divisão por zero não é permitida.")
        break
    else:
        print("Operação inválida! Tente novamente.\n")