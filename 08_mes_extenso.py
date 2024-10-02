'''
Titulo: Mes por extenso  
Autor: Cadu
Data: 26/09/2024
Descrição:Faça um programa que receba o mês em número e apresente-o por extenso.
'''

#entrada de dados
#recebo o valor pelo usuário e converto para inteiro
mes = int(input('Inserir o mes:')) 

#processamento de dados

if mes == 1:
    mes_extenso = 'janeiro'
elif mes == 2:
    mes_extenso = 'feveiro'
elif mes == 3:
    mes_extenso = 'março'
elif mes == 4:
    mes_extenso = 'abril'
elif mes == 5:
    mes_extenso = 'maio'
elif mes == 6:
    mes_extenso = 'junho'
elif mes == 7:
    mes_extenso = 'julho'
else:
    mes_extenso = 'mes nao existe'    
#saida de dados 

print(mes_extenso)
  