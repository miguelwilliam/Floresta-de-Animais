import pygame
from GameObjects import *

# PALETA:   
# https://lospec.com/gallery/retronova/arctic-mint
# rgb(16, 48, 64)
# rgb(113, 189, 174) - branco tabuleiro
# rgb(186, 217, 207)
# rgb(19, 128, 128) - preto tabuleiro

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
        self.animais = []

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
    
    def mostrar_texto(self,texto,tamanho,pos,centered = False, color = (255,255,255)):
        font = pygame.font.Font('Minecraft.ttf',tamanho)
        text = font.render(texto,True,color,)
        textRect = text.get_rect()
        if centered == True:
            textRect.center = (pos[0], pos[1])
        else:
            textRect.topleft = (pos[0], pos[1])
        self.screen.blit(text,textRect)
    
    def novoJogo(self):
        self.turno = 1
        self.animais = []
        self.player = Leao('jorge','azul','macho',3,150,40,1,1,self,15)
        self.animais.append(self.player)
    
    def rodar(self):
        while self.running:
            # CHECAR EVENTOS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                if event.type == pygame.KEYDOWN:

                    if self.GAMESTATE == 'jogo':
                        tecla = pygame.key.name(event.key)
                        if tecla == 'space':
                            self.player.andar()
                        if tecla == 'r':
                            self.debug()

                        
                    if self.GAMESTATE == 'gameover':
                        pass

            
            # ------------- TICK -------------
            if self.GAMESTATE == 'jogo':
                pass
            
            elif self.GAMESTATE == 'gameover':
                pass

            
            # ------------- RENDER -------------
            self.screen.fill((16, 48, 64))

            if self.GAMESTATE == 'jogo':
                for i in range(len(self.tabuleiro)):
                    for j in range(len(self.tabuleiro[i])):
                        if (j+i) % 2 == 0:
                            color = (113, 189, 174)
                        else:
                            color = (19, 128, 128)

                        tile_rect = pygame.Rect(50+self.tileSize*j, 50+self.tileSize*i, self.tileSize, self.tileSize)
                        pygame.draw.rect(self.screen, color, tile_rect)
                        
                        
                for animal in self.animais:
                    self.mostrar_texto(animal.getNome(), 20, [50+self.tileSize*animal.getPos()[0]+self.tileSize/2, 50+self.tileSize*animal.getPos()[1]+self.tileSize/2], True, (186, 217, 207)) 


                self.mostrar_texto('Floresta de Animais',36,(300,30), True, (113, 189, 174))

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
#game.debug()
game.novoJogo()
game.rodar()
pygame.quit()