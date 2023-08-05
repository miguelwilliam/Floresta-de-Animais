import pygame
from GameObjects import *
from random import randint

# PALETA 1:   
# https://lospec.com/gallery/retronova/arctic-mint
# rgb(16, 48, 64)
# rgb(113, 189, 174) - branco tabuleiro
# rgb(186, 217, 207)
# rgb(19, 128, 128) - preto tabuleiro

# PALETA 2:   
# https://lospec.com/palette-list/leopolds-dreams
# rgb(55, 33, 52)
# rgb(71, 68, 118)
# rgb(72, 136, 183)
# rgb(109, 188, 185)
# rgb(140, 239, 182)

class Game:
    def __init__(self):
        self.turno = 1
        self.SCREENSIZE = (600,600)
        pygame.init()
        self.screen = pygame.display.set_mode(self.SCREENSIZE)
        pygame.display.set_caption('Floresta')
        self.clock = pygame.time.Clock()
        self.running = True
        self.GAMESTATE = 'jogo'
        self.tileSize = 50
        self.animais = []
        self.checar_colisoes = False

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
        
        self.textos_temporarios = [['BEM VINDOS',36,(300,300), True, (255, 255, 255), 60*3]] #Usado pra armazenar textos que mostrarão por uma quantia de tempo pré-determinada
    
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
        self.turno = 1
        self.animais = []
        self.player = Leao('jorge','azul','macho',3,150,40,0,0,self,15)
        self.animais.append(self.player)
        self.animal1 = Pulga('aipim','preto','femea',0,0.4,6,randint(0,9),randint(0,9),self,2)
        self.animais.append(self.animal1)
        '''
        self.animal2 = Vaca('aurora','malhado','femea',0,100,50,randint(0,9),randint(0,9),self,'malhada')
        self.animais.append(self.animal2)
        self.animal3 = Cachorro('gostoso','preto','macho',2,17,50,randint(0,9),randint(0,9),self,5,'caramelo')
        self.animais.append(self.animal3)
        self.animal4 = Gato('mingau','branco','femea',0,5,50,randint(0,9),randint(0,9),self,'frajola')
        self.animais.append(self.animal4)
        self.animal5 = Ovelha('fluminosa','branca','femea',1,80,50,randint(0,9),randint(0,9),self,4)
        self.animais.append(self.animal5)
        '''
    
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
                            if self.player.stamina > 0:
                                self.player.andar()
                                self.checar_colisoes = True
                            else:
                                self.textos_temporarios.append(['SEM STAMINA!', 36,(300,300), True, (94, 20, 15), 60])
                        if tecla == 'r':
                            self.debug()
                        if tecla == 't':
                            self.novoJogo()

                        
                    if self.GAMESTATE == 'gameover':
                        pass

            
            # ------------- TICK -------------
            if self.GAMESTATE == 'jogo':

                for animal in self.animais:
                    if self.checar_colisoes == False:
                        break
                    if animal == self.player:
                        continue
                    if self.player.checar_colisao(animal) == True:
                        if isinstance(self.player, Leao):
                            self.player.rugir(animal)
                        elif isinstance(self.player, Cachorro):
                            self.player.latir(animal)
                        elif isinstance(self.player, Gato):
                            self.player.miar(animal)
                        elif isinstance(self.player, Vaca):
                            self.player.mugir(animal)
                        elif isinstance(self.player, Ovelha):
                            self.player.balir(animal)
                        elif isinstance(self.player, Pulga):
                            self.player.sugar(animal)
                    self.checar_colisoes = False
            
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
                    img = animal.img
                    rect = img.get_rect()
                    rect.center = [50+self.tileSize*animal.getPos()[0]+self.tileSize/2, 50+self.tileSize*animal.getPos()[1]+self.tileSize/2]
                    self.screen.blit(img, rect)
                    
                    self.mostrar_texto(animal.getNome(), 15, [50+self.tileSize*animal.getPos()[0]+self.tileSize/2, 72+self.tileSize*animal.getPos()[1]+self.tileSize/2], True, (50, 41, 71)) 

                self.mostrar_texto('Floresta de Animais',36,(300,30), True, (113, 189, 174))
                self.mostrar_texto(f'Turno: {self.turno} - Stamina: {self.player.stamina}/{self.player.max_stamina}',24,(50,570), False, (113, 189, 174))

                if len(self.textos_temporarios) > 0:
                    for texto in self.textos_temporarios:
                        if texto[-1] <= 0: #se tiver acabado o tempo do texto na tela
                            self.textos_temporarios.remove(texto)
                        else:
                            self.mostrar_texto(texto[0],texto[1],texto[2],texto[3],texto[4])
                            texto[-1] -= 1


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
        print(f'animais = {self.animais}')
        print('')
        print('')
        for i in self.animais:
            print(f'{i.getNome()} - {i.getPos()}')

game = Game()
#game.debug()
game.novoJogo()
game.rodar()
pygame.quit()