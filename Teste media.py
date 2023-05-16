#Pedindo as notas!
import os


n1 = float(input("Digite a nota do Primeiro Bimeste: "))
n2 = float(input("Digite a nota do Primeiro Segundo: "))
n3 = float(input("Digite a nota do Primeiro Terceiro: "))
n4 = float(input("Digite a nota do Primeiro Quarto: "))

#Calcular a média

media = (n1 + n2 + n3 + n4) / 4

print("A sua média foi: ",media)

#Condição

if media < 7.0:
    print('Reprovado! \nVamos para a prova final!')
    #print('')
elif media <= 10:
    print('Aprovado! \nBoas Férias!')
    #print('Boas Férias!')


os.system("pause")
