'''Titulo: Aumento Salarial 
Autor: Cadu
Data: 26/09/2024
Descrição: Faça um programa que receba o salário de um funcionário, calcule e mostre o novo
salário, sabendo-se que:
Salário &lt; R$ 1000,00 aumento de 25%.
Salário &gt;= R$ 1000,00 e &lt; R$ 2000,00 aumento de 15%.
Salário &gt;= R$ 2000,00 aumento de 10%. 
'''

#entrada de dados
salario = float(input('digite o salario :'))

#processamento de dados 
if salario < 1000: 
    salario_reajuste = salario * 1.25
    print('25%')
if salario >=1000 and salario < 2000:
    print('15%')
    reajuste = salario * 0.15
    salario_reajuste = salario + reajuste 
if salario >=2000:
    print('10%')
    salario_reajuste = salario * 1.1        

#saida de dados 
print('seu novo salario:', salario_reajuste)