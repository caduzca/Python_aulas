'''
Titulo:Ocupação de Profissão    
Autor: Cadu
Data: 01/10/2024
Descrição:Faça um programa para exibir a ocupação de um funcionário a partir de 
seu código de
profissão, de acordo com a tabela abaixo;

Código de Profissão       Ocupação
1                         Matemático
2                         Analista de Sistemas
3                           Físico
4                           Arquiteto
5                          Piloto de Aeronaves
'''

#entrada de dados

profissao = int(input('Digite o código de profissão:'))

#processamento de dados
if profissao == 1 :
    ocupação = 'Matemático'
elif profissao == 2 :
    ocupação = 'Analista de Sistema'
elif profissao == 3 :
    ocupação = 'Físico'
elif profissao == 4 :
    ocupação = 'Arquiteto'
elif profissao == 5 :
    ocupação = 'Piloto de Aeronaves'
else:
    ocupação = 'profissao nao existe'            
#saida de dados
print('profissao', ocupação)