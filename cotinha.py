#cotinha
def cotinha():
    print(13*"*")
    print("*--cotinha--*")
    print(13*"*")
    print("\nPara facilitar e evitar entre os coleguinhas, vamos fazer uma cotinha!!!!")

    vl_orcamento    = float(input("Informe o valor das compras: "))
    qtd_pessoas     = int(input("Para quantas pessoas será feita a divisão? "))

    #Outra forma de converter
    #valor   = int(vl_orcamento)
    #pessoas = int(qtd_pessoas)

    cota    = vl_orcamento / qtd_pessoas

    print("O valor por pessoa ficou de R$%.2f!"%(cota))
    again()

def again():
    import os  # import para a usar o cls / Limpar a tela
    rodar_cotinha = input("\n\nQuer calcular novamente: [S] Sim ou [N] Não: \n")
    if rodar_cotinha.upper().strip()[0] == "S":
        os.system('cls') # Usado no import
        cotinha()
    elif rodar_cotinha.upper().strip()[0] == "N":
        print("Encerrando...")
    else:
        print('Valor invalido!')
        again()
cotinha()
