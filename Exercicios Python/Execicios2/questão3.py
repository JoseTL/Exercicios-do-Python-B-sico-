#Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os
# dicionários em uma lista. No final, mostre:
#   a. Quantas pessoas foram cadastradas;
#   b. A média de idade do grupo;
#   c. Uma lista com todas as mulheres;
#   d. Uma lista com todas as pessoas com idade acima da média;

galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO...! Por favor, digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO...! Responda apenas S ou N ')
        if resp == 'N':
         break
print('='*80)
print(f' A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f' B) A média de idade é de {media:5.2f} anos.')
print(' C) As melheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das Pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('     ', end='')
        for k,v in p.items():
            print(f'{k}={v};', end='')
        print()
print('<<<<<<<< ENCERRADO >>>>>>')









