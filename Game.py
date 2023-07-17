import pygame
from GameObjects import *


class Game:
    def __init__(self):
        self.turno = 1
        self.SCREENSIZE = (600,600)
        pygame.init()
        self.screen = pygame.display.set_mode(self.SCREENSIZE)
        pygame.display.set_caption('Forca')
        self.clock = pygame.time.Clock()
        self.running = True
        self.GAMESTATE = 'jogo'
        self.tileSize = 50

        #tabuleiro 10x10
        #ordem das nested lists: [linha][coluna](essa ultima é formada por listas dentro, porque pode ter mais de um animal na mesma casa)
        self.tabuleiro =  [
            [[], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], []]
            ]
    
    def rodar(self):
        while self.running:
            # CHECAR EVENTOS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                if event.type == pygame.KEYDOWN:

                    if self.GAMESTATE == 'jogo':
                        tecla = pygame.key.name(event.key)
                        
                    if self.GAMESTATE == 'gameover':
                        pass

            
            # ------------- TICK -------------
            if self.GAMESTATE == 'jogo':
                pass
            
            elif self.GAMESTATE == 'gameover':
                pass

            
            # ------------- RENDER -------------
            self.screen.fill((153, 75, 29))
            if self.GAMESTATE == 'jogo':
                for i in range(len(self.tabuleiro)):
                    for j in range(len(self.tabuleiro[i])):
                        if (j+i) % 2 == 0:
                            color = (255,255,255)
                        else:
                            color = (0,0,0)
                        
                        pygame.draw.rect(self.screen, color, (75+self.tileSize*j, 50+self.tileSize*i, self.tileSize, self.tileSize))
            
            elif self.GAMESTATE == 'gameover':
                pass
            
            pygame.display.flip()
            self.clock.tick(60)
    
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
game.rodar()
pygame.quit()