# Faça um Programa que pergunte quanto você ganha por hora
# e o número de horas trabalhadas no mês. Calcule e mostre
# o total do seu salário no referido mês.

hour = float (input ("Digite o seu salário por hora: "))
hour_month = float (input ("Quantas horas você trabalha por mês? "))

salary = hour *hour_month

print (f"Você recebe R${salary:,.2f} por mês")