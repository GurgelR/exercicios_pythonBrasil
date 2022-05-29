# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

n1 = float (input("Digite a nota do primeiro bimestre: "))
n2 = float (input("Digite a nota do segundo bimestre: "))
n3 = float (input("Digite a nota do terceiro bimestre: "))
n4 = float (input("Digite a nota do quarto bimestre: "))  

mean = (n1+n2+n3+n4)/4

if mean < 7:
    print (f"\nA média do aluno foi: {mean:,.2f}... ficou de recuperação")
else:
    print (f"\nA média do aluno foi: {mean:,.2f}... não fez mais que a obrigação")




