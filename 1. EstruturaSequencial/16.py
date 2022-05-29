# =============================================================================
# Faça um programa para uma loja de tintas. O programa deverá
# pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3
# metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de
# tinta a serem compradas e o preço total.
# =============================================================================

area_parede = float(input("Digite o tamanho da parede em m²: "))

latas = area_parede/54
   

if float.is_integer(latas): # verifica se a variável de tipo float representa um número inteiro
    latas = int (latas)
else:
    latas = int(latas)+1

preco = latas * 80

print (f"\nVocê precisará de {latas} latas, o que custará R${preco:,.2f}")


