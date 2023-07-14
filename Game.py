#import pygame
from GameObjects import *


class Game:
    def __init__(self):
        self.turno = 1
        #tabuleiro 10x10
        #ordem das nested lists: [linha][coluna](essa ultima é formada por listas dentro, porque pode ter mais de um animal na mesma casa)
        self.tabuleiro =  [
            [['oooooo'], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], ['000000']]
            ]
    
    def debug(self):
        for linha in self.tabuleiro:
            linha_atual = ''
            for coluna in linha:
                if len(coluna) == 0:
                    linha_atual+='X'
                else:
                    linha_atual+=str(len(coluna))
                linha_atual+=' '
            print(linha_atual)

game = Game()
game.debug()