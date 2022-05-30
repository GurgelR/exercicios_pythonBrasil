# =============================================================================
# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em 
# metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de
# 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 
# litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# 
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
# preços em 3 situações:
# 
#       a) comprar apenas latas de 18 litros;
#       b) comprar apenas galões de 3,6 litros;
#       c) misturar latas e galões, de forma que o desperdício de tinta seja menor. 
#       Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, 
#       considere latas cheias.
# =============================================================================


area_parede = float(input("Digite o tamanho da parede em m²: "))
tinta_necessaria = area_parede/6
print (f"Você precisará de {tinta_necessaria:,.2f} litros de tinta")

preco_litro_galao = 25/3.6
preco_litro_lata = 80/18

###########   SITUAÇÃO 1   ###########

latas = area_parede/(6*18)
if float.is_integer(latas): # verifica se a variável de tipo float representa um número inteiro
    latas = int (latas)
    sobra_lata = 0
else:
    latas = int(latas)+1
    sobra_lata = (latas*18) - (tinta_necessaria)

preco_a = latas * 80

print (f"""
SITUAÇÃO 1 - SOMENTE LATAS:
Latas: {latas}
Preço: R${preco_a:,.2f}
Sobra: {sobra_lata:,.2f} litro(s)
""")
###########   SITUAÇÃO 2   ###########

galoes = area_parede/(6*3.6)
if float.is_integer(galoes): # verifica se a variável de tipo float representa um número inteiro
    galoes = int (galoes)
    sobra_galao = 0
else:
    galoes = int(galoes)+1
    sobra_galao = (galoes*3.6) - (tinta_necessaria)

preco_b = galoes * 25

print (f"""
SITUAÇÃO 2 - SOMENTE GALÕES:
Galões: {galoes}
Preço: R${preco_b:,.2f}
Sobra: {sobra_galao:,.2f} litro(s)
""")
###########   SITUAÇÃO 3   ###########

area_folga = (area_parede + area_parede*0.1) # 10% de folga
tinta_folga = area_folga/6 # litros de tinta necessários para a pintura
latas_folga = int(tinta_folga/18) # latas que serão utilizadas
tinta_sobra = latas_folga*18 - tinta_folga
galoes_folga = tinta_sobra/3.6 # galões que serão utilizados
print (latas_folga)
print (tinta_sobra)

tinta_sobra_final = (latas_folga*18 + galoes_folga*3.6) - tinta_folga

print(f"""
SITUAÇÃO 3 - LATAS E GALÕES:
Latas: {latas_folga}
Galões: {galoes_folga}
Sobra: {tinta_sobra_final:,.2f}
""")

##### RESOLUÇÃO DA SITUAÇÃO 3 ESTÁ ERRADA


