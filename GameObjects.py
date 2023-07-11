class Animal():
    def __init__(self, nome, cor, sexo, velocidade, peso, stamina, posX, posY, game):
        self.nome = nome
        self.cor = cor
        self.sexo = sexo
        self.vel = velocidade
        self.peso = peso
        self.stamina = stamina
        self.pos = [posX, posY]

        self.game = game
        self.turno = 1
        self.direcaoX = 'direita' # direita / esquerda
        self.direcaoY = 'cima' # cima / baixo

    def andar(self):
        if self.turno % 2 == 0:
            if self.direcaoX == 'direita':
                if self.pos[0] + self.vel > len(self.game.tabuleiro):
                    self.pos[0] = len(self.game.tabuleiro)
                    self.direcaoX = 'esquerda'
                else:
                    self.pos[0] += self.vel
            else:
                if self.pos[0] - self.vel < 1:
                    self.pos[0] = 1
                    self.direcaoX = 'direita'
                else:
                    self.pos[0] -= self.vel
        
        else:
            if self.direcaoY == 'cima':
                if self.pos[1] + self.vel > len(self.game.tabuleiro):
                    self.pos[1] = len(self.game.tabuleiro)
                    self.direcaoY = 'baixo'
                else:
                    self.pos[1] += self.vel
            else:
                if self.pos[1] - self.vel < 1:
                    self.pos[1] = 1
                    self.direcaoY = 'cima'
                else:
                    self.pos[1] -= self.vel
        self.turno += 1
    
    def checar_colisao(self, nome_colisao):
        if self.name and nome_colisao in self.game.tabuleiro[self.pos[1]-1][self.pos[0]-1]:
            return True
        return False

    def imprimir_caracteristicas(self):
        print(f'''
= nome: {self.nome}
= cor: {self.cor}
= sexo: {self.sexo}
= velocidade: {self.vel}
= peso: {self.peso}
= stamina: {self.stamina}
= posiçao X: {self.pos[0]}
= posiçao Y: {self.pos[1]}
              ''')
