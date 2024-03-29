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
        self.animal4 = Leao('jorge','azul','macho',3,150,20,randint(0,9),randint(0,9),self,15)
        self.animal1 = Pulga('aipim','preto','femea',0,0.4,6,randint(0,9),randint(0,9),self,2)
        self.animal2 = Vaca('aurora','malhada','femea',0,100,50,randint(0,9),randint(0,9),self,'malhada')
        self.animal3 = Cachorro('gostoso','preto','macho',2,17,50,randint(0,9),randint(0,9),self,5,'caramelo')
        self.player = Gato('mingau','branco','femea',2,5,20,randint(0,9),randint(0,9),self,'frajola')
        self.animal5 = Ovelha('fluminosa','branca','femea',1,80,50,randint(0,9),randint(0,9),self,4)

        self.player.setPos(0,0)
        
        self.GAMESTATE = 'jogo'
        self.fase_de_jogo = 0
    
    def rodar(self):
        while self.running:
            # CHECAR EVENTOS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                if event.type == pygame.KEYDOWN:

                    if self.GAMESTATE == 'jogo':
                        
                        if event.key in [pygame.K_UP, pygame.K_DOWN] and self.turno % 2 != 0 and self.player.stamina > 0:
                            self.player.andar(event.key)
                            self.checar_colisoes = True
                        elif event.key in [pygame.K_LEFT, pygame.K_RIGHT] and self.turno % 2 == 0 and self.player.stamina > 0:
                            self.player.andar(event.key)
                            self.checar_colisoes = True
                        elif event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN] and self.player.stamina <= 0:
                            self.textos_temporarios.append(['SEM STAMINA!', 36,(300,300), True, (87, 54, 52), 60])
                        
                        if event.key == pygame.K_t:
                            self.debug()
                        if event.key == pygame.K_r:
                            self.novoJogo()

                        
                    if self.GAMESTATE == 'gameover':
                        if event.key == pygame.K_RETURN:
                            self.novoJogo()

            
            # ------------- TICK -------------
            if self.GAMESTATE == 'jogo':

                for animal in self.animais:
                    if self.checar_colisoes == False:
                        break
                    if animal == self.player or animal in self.player.evitar_animais:
                        continue # Ou seja, esse loop pega todos os animais menos o jogador
                    if self.player.checar_colisao(animal,self.player.pos) == True:
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
                self.player.evitar_animais = []

                self.checar_colisoes = False

                if self.player.pos == [9,9] and self.fase_de_jogo == 0:
                    self.fase_de_jogo += 1
                elif self.player.pos == [0,0] and self.turno != 1 and self.fase_de_jogo == 1:
                    self.fase_de_jogo += 1
                if self.fase_de_jogo == 2:
                    self.GAMESTATE = 'gameover'
                if self.player not in self.animais:
                    self.GAMESTATE = 'gameover'
            
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

                dir_path = 'Images/dir_'
                if self.turno % 2 == 0:
                    dir_path += 'h.png'
                else:
                    dir_path += 'v.png'
                dir_img = pygame.image.load(dir_path)
                
                dir_imgRect = dir_img.get_rect()
                dir_imgRect.bottomright = (600,600)
                self.screen.blit(dir_img,dir_imgRect)

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
                player_img = pygame.transform.scale(self.player.img, (100,100))
                img_rect = player_img.get_rect()
                img_rect.center = [300,250]
                self.screen.blit(player_img, img_rect)

                self.mostrar_texto('Obrigado por jogar!',18,(300,180), True, (140, 239, 182))
                self.mostrar_texto('Floresta de Animais',36,(300,150), True, (181, 255, 212))
                self.mostrar_texto('Aperte ENTER para um novo jogo!',18,(300,330), True, (181, 255, 212))
            
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
game.novoJogo()
game.rodar()
pygame.quit()