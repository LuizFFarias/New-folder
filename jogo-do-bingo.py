#Douglas Magalhães de Araujo - Rm 552008
#Luiz Fillipe Farias - Rm 99519
#Rafaella Monique do Carmo Bastos - Rm 552425

import random

"""
FINALIZADO 1 - Função que solicita o número de jogadores e seus nomes
"""  
def definicao_jogadores():
    num_jogadores = int(input("Quantos jogadores (1 a 5)? "))

    if num_jogadores >= 1 and num_jogadores <= 5:
        jogadores = []

        for i in range(num_jogadores):
            nome_jogador = input(f"Nome do jogador {i + 1}: ")
            jogadores.append({"nome": nome_jogador, "cartelas": [], "vitorias": 0})
    else:
        print('O número mínimo é 1 e o máximo é 5.')

    return jogadores

"""
FINALIZADO 2 - Função que gera os números das tabelas dos jogadores
"""
def criar_cartela(num_jogadores):
    cartelas = []
    
    for i in range(num_jogadores):
        cartela = []
        for a in range(5):
            linha = random.sample(range(1, 51), 5)
            cartela.append(linha)
        cartelas.append(cartela)

    return cartelas
  
"""
FINALIZADO 3 - Função para interface gráfica
"""
def interface_cartela(cartela):
    for i in range(len(cartela)):
        for j in range (len(cartela[0])):
            print(cartela[i][j], end="\t")
        print()

"""
FINALIZADO 4 - Função para sortear os números do bingo
""" 
num_sorteados = []
 
def sortear_numeros():
    if len(num_sorteados) < 50:
        input("Pressione a tecla Enter para sortear um número...")
        while True:
            num_sorteado = random.randint(1, 50)
            if num_sorteado not in num_sorteados:
                num_sorteados.append(num_sorteado)
                print(f'Número sorteado: {num_sorteado}')
                break
            else:
                print("Todos os números já foram sorteados!")

"""
FINALIZADO 5 - Função que verifica vencedor do bingo
"""
def vencedor_cartela(cartela, num_sorteado, jogadores):
    for i in range(5):
        if all(cartela[i][j] == 'XX' for j in range(5)):
            print('Venceu na linha ', i + 1)
            
    for j in range(5):
        if all(cartela[i][j] == 'XX' for i in range(5)):
            print('Jogador', jogadores[j]["nome"], 'Venceu na coluna ', j + 1)       

"""
6- Função para criar um ranking de ganhadores(nome do jogador e quantas vezes ele venceu o jogo). 
"""  
def ranking(jogadores):
    vitorias = {}

    for jogador in jogadores:
        nome = jogador['nome']
        vitorias[nome] = vitorias.get(nome, 0) + jogador['vitorias']

    ranking = sorted(vitorias.items(), key=lambda x: x[1], reverse = True)

    with open('ranking.txt', 'w') as arquivo:
        arquivo.write('Ranking:\n')
        for i, (nome, vitoria) in enumerate (ranking, start = 1):
            arquivo.write(f'{i}º lugar: {nome} - {vitoria} vitorias\')

   

"""     
Menu que chamará as funções
"""
while True:     
    print('\nJOGO DE BINGO')
    print('1 - Iniciar partida')
    print('2 - Sair')

    try: 
        opcaomenu = int(input('\nEscolha uma opção: '))
    except ValueError:
        print('O valor deve ser um número inteiro.')
        continue

    if opcaomenu == 1:
        jogadores = definicao_jogadores()
        
        if jogadores:
            criar_cartela(len(jogadores))
            print("\nCartelas Geradas:")
            
            for jogador in jogadores:
                print(f"Cartelas de {jogador['nome']}:")
                interface_cartela(jogador['cartelas'])
            input("\nPressione Enter para começar o sorteio...")
            while True:
                num_sorteado = sortear_numeros()
                print(f'Número sorteado: {num_sorteado}')
                for jogador in jogadores:
                    vencedor_cartela(jogador['cartelas'], num_sorteado, jogador['nome'])
                input('\nPressione Enter para continuar o sorteio ou digite "fim" para encerrar...')
                if input().strip().lower() == 'fim':
                    ranking(jogadores)
                    ranking()
                    break
    elif opcaomenu == 2:
        print('Até a próxima!')
        break
    else:
        print('Opção incorreta. Escolha uma opção válida.')
        