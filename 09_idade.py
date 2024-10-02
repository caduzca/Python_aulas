'''
Titulo: faixa etária   
Autor: Cadu
Data: 01/10/2024
Descrição:Escreva um programa que leia a idade de um indivíduo e escreva a faixa etária a que
pertence, de acordo com a tabela abaixo; 

           Faixa etaria   Classificação
           <=12            criança
           12~17           Adolescente
           18^59           Adulto
           60>             Especialista

'''

#entrada de dados
  
idade = int(input('Digita a idade do usuário: '))
#processamento de dados 

if idade <= 12:
    categoria = 'criança' 
elif idade >= 13 and idade <= 17:
    categoria = 'adolescente'
elif idade >= 18 and idade <= 57:
    categoria = 'adulto'
elif idade >= 60:
    categoria = 'especialista'  

#saida de dados 
print('categoria do usuário:', categoria)