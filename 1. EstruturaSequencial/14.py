# =============================================================================
# João Papo-de-Pescador, homem de bem, comprou um microcomputador 
# para controlar o rendimento diário de seu trabalho. Toda vez que 
# ele traz um peso de peixes maior que o estabelecido pelo regulamento 
# de pesca do estado de São Paulo (50 quilos) deve pagar uma multa 
# de R$ 4,00 por quilo excedente. João precisa que você faça um programa 
# que leia a variável peso (peso de peixes) e calcule o excesso. Gravar 
# na variável excesso a quantidade de quilos além do limite e na variável 
# multa o valor da multa que João deverá pagar. Imprima os dados do programa
#  com as mensagens adequadas
# =============================================================================

peso = float (input("Quantidade pescada hoje (em kg): "))
if peso > 50:
    excesso = peso-50
    multa = excesso*4
    if excesso == 1:
        print ("Passou 1kg do permitido. A multa será de R$4.00")
    else:
        print (f"Passou {excesso:,.2f}kgs do permitido. A multa será de R${multa:,.2f}")
else:
    excesso = 0
    print ("Não passou do peso permitido")
    



