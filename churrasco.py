#churrasco
print("********************************************\n*              CHURRASCO	           *\n********************************************\nQuantidade de bebidas e carnes para o churrasco\n\nPara que a gente possa ajudar, vamos perdir algumas informações!\n")
qtd_homem  = input("Quantidade de homens: ")
qtd_mulher = input("Quantidade de mulheres: ")
print("\n\nAnalisamos as suas informações e abaixo está uma média de quantidade do material para o churrascão entre amgigos!\nDIVIRTAM-SE\n\n")

homem     = int(qtd_homem)
mulher    = int(qtd_mulher)
carne     = int()
pao_alho  = int()
cerveja   = int()
refri     = int()    
copo      = int()
prato     = int()
sal       = float()

#Cálculo 
carne     = ((homem * 0.200) + (mulher * 0.150))
cerveja   = ((homem * 8) + (mulher * 6))
refri     = (homem + mulher) * 400
prato     = (homem + mulher) * 2
copo      = (homem + mulher) * 3
pao_alho  = (homem + mulher) * 2
sal       = (carne * 0.18)
   

#Resultado
print("Quantidade de carne: {}Kg".format(carne))
print("Quantidade de cerveja em lata: {} latinha(s)".format(cerveja))
print("Quantidade de pratinhos: {} unidade(s)".format(prato))
print("Quantidade de Refrigerante: {}ml".format(refri))
print("Quantidade de copos: {} unidade(s) de 280ml".format(copo))
print("Quantidade de sal: {}g".format(sal))
