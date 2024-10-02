# Faça um programa que recebe um número em Pés, faça as conversões a seguir e
# mostre os resultados.
# Polegadas;
# - Jardas;
# - Milhas;
# Sabe –se que:
# 1 Pé = 12 polegadas;
# 1 Jarda = 3 Pés;
# 1 Milha = 1.760 Jarda;

#entrtada de dados 
pes = int(input('inserir o valorem pés:'))
#processamento de dados 
polegadas = pes * 12 
jardas = pes / 3
milhas = jardas / 1760
#saida de dados Faça um programa que recebe um número em Pés, faça as conversões a seguir e
print('polegadas:', polegadas)
print('jardas:', jardas)
print('milhas', milhas)