#Faça um programa que receba o salário de um funcionário, calcule e mostre o novo
#salário, sabendo-se que este sofreu um aumento de 25%.

#entrada de dados
salario_atual = int(input('inserir valor do salario:'))

#processamento de dados
aumento = salario_atual * 0.25
novo_salario = aumento + salario_atual
#saida de dados
print(salario_atual)
print(novo_salario)