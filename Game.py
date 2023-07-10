#import pygame
from GameObjects import *

#tabuleiro 10x10
#ordem das nested lists: [linha][coluna](essa ultima é formada por listas dentro, porque pode ter mais de um animal na mesma casa)
tabuleiro = [
            [['leao','zebro'], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], ['leao'], [], [], []],
            [[], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], []],
            [[], ['gato','tigre'], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], []]
            ]

for linha in tabuleiro:
    linha_atual = ''
    for coluna in linha:
        if len(coluna) == 0:
            linha_atual+='X'
        else:
            linha_atual+=str(len(coluna))
        linha_atual+=' '
    print(linha_atual)