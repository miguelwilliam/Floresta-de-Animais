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

        self.game.tabuleiro[posY][posX].append(self)

        

    def andar(self):
        oldX = self.pos[0]
        oldY = self.pos[1]

        if self.game.turno % 2 == 0:
            if self.direcaoX == 'direita':
                if self.pos[0] + self.vel >= len(self.game.tabuleiro)-1:
                    self.pos[0] = len(self.game.tabuleiro)-1
                    self.direcaoX = 'esquerda'
                else:
                    self.pos[0] += self.vel
            else:
                if self.pos[0] - self.vel < 1:
                    self.pos[0] = 0
                    self.direcaoX = 'direita'
                else:
                    self.pos[0] -= self.vel
        
        else:
            if self.direcaoY == 'cima':
                if self.pos[1] + self.vel >= len(self.game.tabuleiro)-1:
                    self.pos[1] = len(self.game.tabuleiro)-1
                    self.direcaoY = 'baixo'
                else:
                    self.pos[1] += self.vel
            else:
                if self.pos[1] - self.vel < 1:
                    self.pos[1] = 0
                    self.direcaoY = 'cima'
                else:
                    self.pos[1] -= self.vel
        
        self.game.tabuleiro[oldY][oldX].remove(self)
        self.game.tabuleiro[self.pos[1]][self.pos[0]].append(self)
        self.game.turno += 1
    
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
        
    def getPos(self):
        return self.pos
    def setPos(self, newX, newY):
        self.pos = [newX, newY]
    
    def getNome(self):
        return self.nome
    def setNome(self, newNome):
        self.nome = newNome
    
    def getCor(self):
        return self.cor
    def setCor(self, newCor):
        self.cor = newCor

    def getSexo(self):
        return self.sexo
    def setSexo(self, newSexo):
        self.sexo = newSexo

    def getVel(self):
        return self.vel
    def setVel(self, newVel):
        self.vel = newVel

    def getPeso(self):
        return self.peso
    def setPeso(self, newPeso):
        self.peso = newPeso

    def getStamina(self):
        return self.stamina
    def setStamina(self, newStamina):
        self.stamina = newStamina



class Leao(Animal):
    def __init__(self, nome, cor, sexo, velocidade, peso, stamina, posX, posY, game, idade):
        super().__init__(nome, cor, sexo, velocidade, peso, stamina, posX, posY, game)
        self.idade = idade
    
    def rugir(self):
        print('rugido raarwwwww')
    
    def getIdade(self):
        return self.idade
    def setIdade(self, newIdade):
        self.idade = newIdade

class Cachorro(Animal):
    def __init__(self, nome, cor, sexo, velocidade, peso, stamina, posX, posY, game, idade, raca):
        super().__init__(nome, cor, sexo, velocidade, peso, stamina, posX, posY, game)
        self.idade = idade
        self.raca = raca
    
    def latir(self):
        print('latido auauauauau')
    
    def getIdade(self):
        return self.idade
    def setIdade(self, newIdade):
        self.idade = newIdade

    def getRaca(self):
        return self.raca
    def setRaca(self, newRaca):
        self.raca = newRaca

class Gato(Animal):
    def __init__(self, nome, cor, sexo, velocidade, peso, stamina, posX, posY, game, raca):
        super().__init__(nome, cor, sexo, velocidade, peso, stamina, posX, posY, game)
        self.raca = raca
    
    def miar(self):
        print('miado miauuuuuuuuu')
    
    def getRaca(self):
        return self.raca
    def setRaca(self, newRaca):
        self.raca = newRaca

class Vaca(Animal):
    def __init__(self, nome, cor, sexo, velocidade, peso, stamina, posX, posY, game, raca):
        super().__init__(nome, cor, sexo, velocidade, peso, stamina, posX, posY, game)
        self.raca = raca
    
    def mugir(self):
        print('mugido muuuuuuuuuuuu')
    
    def getRaca(self):
        return self.raca
    def setRaca(self, newRaca):
        self.raca = newRaca

class Ovelha(Animal):
    def __init__(self, nome, cor, sexo, velocidade, peso, stamina, posX, posY, game, idade):
        super().__init__(nome, cor, sexo, velocidade, peso, stamina, posX, posY, game)
        self.idade = idade
    
    def balir(self):
        print('balindo meeeeeeeeehhh')

    def getIdade(self):
        return self.idade
    def setIdade(self, newIdade):
        self.idade = newIdade

class Pulga(Animal):
    def __init__(self, nome, cor, sexo, velocidade, peso, stamina, posX, posY, game, idade):
        super().__init__(nome, cor, sexo, velocidade, peso, stamina, posX, posY, game)
        self.idade = idade
    
    def sugar(self):
        print('sugando glubglubglubglub')

    def getIdade(self):
        return self.idade
    def setIdade(self, newIdade):
        self.idade = newIdade