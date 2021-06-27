from random import randint #função da biblioteca radom que escolhe um número aleatório dentro de um parametro informado pelo programador\usuário
from time import sleep #função da biblioteca time que faz uma pausa entre uma excecuçã de código e outro. O tempo de pausa é determinado pelo programador
from operator import itemgetter

print('''                           []=DICE GAME=[]
   
    COMO FUNCIONA? 
        Bom, DICE GAME ou JOGO DE DADOS é um jogo bem simples foi feito para jogar 
em gupo de 4 jogadores. Ganha quem tirar o maior número na rodada, o próprio usuário 
determina a quantidade de rodadas, no fim programa irá mostrar quem venceu mais partidas!        
''')

quantidade_rodadas = int(input('Quantas rodadas você quer jogar?\n'))
player1 = input('Qual o nome do 1º jogador?\n').capitalize()
player2 = input('Qual o nome do 1º jogador?\n').capitalize()
player3 = input('Qual o nome do 1º jogador?\n').capitalize()
player4 =  input('Qual o nome do 1º jogador?\n').capitalize()

vitoria_jgd1=vitoria_jgd2=vitoria_jgd3=vitoria_jgd4=0
empates=0

for r in range(quantidade_rodadas):
    dados = dict()
    dados = {player1:randint(1,6),player2:randint(1,6),player3:randint(1,6),player4:randint(1,6)}
    v = sorted(dados.items(), key=itemgetter(1), reverse=True)
    print("-="*25)
    print(f"{r+1}º RODADA:\n")
    for k, v in v:
        print(f'{k} tirou {v} no dado')
    print()

    if dados[player1]>= dados[player2] and dados[player1]>= dados[player3] and dados[player1] > dados[player4]:
        print(f'\n{player1} venceu está rodada!\n')
        vitoria_jgd1=+1
        
    if dados[player2] >= dados[player1] and dados[player2] >= dados[player3] and dados[player2] >= dados[player4]:
        print(f'\n{player2} venceu está rodada!\n')
        vitoria_jgd2=+1

    if dados[player3] >= dados[player2] and dados[player3] >= dados[player1] and dados[player3] >= dados[player4]:
        print(f'\n {player3} venceu está rodada!\n')
        vitoria_jgd3=+1

    if dados[player4] >= dados[player2] and dados[player4] >= dados[player3] and dados[player4] >= dados[player1]:
        print(f'\n{player4} venceu está rodada!\n')
        vitoria_jgd4=+1
    
    if dados[player1] == dados[player2]:
        print(f"\n{player1} e {player2} empataram!\n")  
        empates=+1
    if dados[player3] == dados[player4] :
        print(f"\n{player3} e {player4} empataram!\n")  
        empates=+1
    if dados[player2] == dados[player3] :
        print(f"\n {player2} e {player3} empataram!\n") 
        empates=+1
    if dados[player1] == dados[player4]:
        print(f"\n{player1} e {player4} empataram!\n")   
        empates=+1
    if dados[player1] == dados[player3]:
        print(f"\n{player1} e {player3} empataram!\n")  
        empates=+1
    if dados[player2] == dados[player4]:
        print(f"\n {player4} e {player2} empataram!\n")  
        empates=+1
    if dados[player1] == dados[player4] == dados[player3] == dados[player2]:
        print('EMPATE GERAL!!')
        empates=+1
print(f''' =========PLACAR==========
{player1} ganhou um total de {vitoria_jgd1} rodadas.
{player2} ganhou um total de {vitoria_jgd2} rodadas.
{player3} ganhou um total de {vitoria_jgd3} rodadas.
{player4} ganhou um total de {vitoria_jgd4} rodadas.
O jogo teve um total de {empates}.
''')
if vitoria_jgd1 > vitoria_jgd2 and vitoria_jgd1 > vitoria_jgd4 and vitoria_jgd1 > vitoria_jgd3:
    print(f"{player1} é o grande campeão!")
if vitoria_jgd2 > vitoria_jgd1 and vitoria_jgd2 > vitoria_jgd4 and vitoria_jgd2 > vitoria_jgd3:
    print(f"{player2} é o grande campeão!")
if vitoria_jgd3 > vitoria_jgd2 and vitoria_jgd3 > vitoria_jgd4 and vitoria_jgd3 > vitoria_jgd1:
    print(f"{player3} é o grande campeão!")
if vitoria_jgd4 > vitoria_jgd2 and vitoria_jgd4 > vitoria_jgd1 and vitoria_jgd4 > vitoria_jgd3:
    print(f"{player4} é o grande campeão!")