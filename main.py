from analise_combinatoria import permutacao, arranjo, combinacao

while True:
    print("-"*50)
    print("Escolha uma operação:")
    options = [
        "1. Permutação",
        "2. Arranjo",
        "3. Combinação",
        "4. Sair"
    ]

    print("-"*50)
    for option in options:
        print(option)
    print("-"*50) 

    try:
        escolha = int(input("Digite o número da operação desejada (1/2/3/4): "))
        
        if escolha == 1:
            n = int(input("Digite o valor de n: "))
            resultado = permutacao(n)
            print("-"*50)
            print(f"Permutação de {n} é: {resultado}")
            print("-"*50)

        elif escolha == 2:
            n = int(input("Digite o valor de n: "))
            k = int(input("Digite o valor de k: "))
            resultado = arranjo(n, k)
            print("-"*50)
            print(f"Arranjo de {n} em {k} é: {resultado}")
            print("-"*50)

        elif escolha == 3:
            n = int(input("Digite o valor de n: "))
            k = int(input("Digite o valor de k: "))
            resultado = combinacao(n, k)
            print("-"*50)
            print(f"Combinação de {n} em {k} é: {resultado}")
            print("-"*50)

        elif escolha == 4:
            print("-"*50)
            print("Saindo do programa.")
            print("-"*50)
            break

        else:
            print("-"*50)
            print("Opção inválida. Tente novamente.")
            print("-"*50)

    except ValueError:
        print("-"*50)
        print("Entrada inválida. Por favor, insira um número.")
        print("-"*50)
