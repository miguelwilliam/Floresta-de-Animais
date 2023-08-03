from random import randint

class Animal():
    def __init__(self, nome, cor, sexo, velocidade, peso, stamina, posX, posY, game):
        self.nome = nome
        self.cor = cor
        self.sexo = sexo
        self.vel = velocidade
        self.peso = peso
        self.stamina = stamina
        self.max_stamina = stamina
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
        self.stamina -= 1
        
        #self.game.mostrar_texto('SEM STAMINA', 40, (500, 10), False, (94, 20, 15))
    
    def checar_colisao(self, obj_colisao):
        if obj_colisao in self.game.tabuleiro[self.pos[1]][self.pos[0]]:
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
    
    def rugir(self, animal_presente, resposta=False):
        print('rugido raarwwwww')
        if isinstance(animal_presente, Leao) and animal_presente.idade > self.idade:
            self.game.animais.remove(self)
            self.game.tabuleiro[self.getPos()[1]][self.getPos()[0]].remove(self)

            self.stamina = 0
            print('game over')
        else:
            self.game.animais.remove(animal_presente)
            self.game.tabuleiro[animal_presente.getPos()[1]][animal_presente.getPos()[0]].remove(animal_presente)
        
        if resposta == False:
            if isinstance(animal_presente, Leao):
                animal_presente.rugir(self, True)
            elif isinstance(animal_presente, Cachorro):
                animal_presente.latir(self, True)
            elif isinstance(animal_presente, Gato):
                animal_presente.miar(self, True)
            elif isinstance(animal_presente, Vaca):
                animal_presente.mugir(self, True)
            elif isinstance(animal_presente, Ovelha):
                animal_presente.balir(self, True)
            elif isinstance(animal_presente, Pulga):
                animal_presente.sugar(self, True)
    
    def getIdade(self):
        return self.idade
    def setIdade(self, newIdade):
        self.idade = newIdade

class Cachorro(Animal):
    def __init__(self, nome, cor, sexo, velocidade, peso, stamina, posX, posY, game, idade, raca):
        super().__init__(nome, cor, sexo, velocidade, peso, stamina, posX, posY, game)
        self.idade = idade
        self.raca = raca
    
    def latir(self, animal_presente, resposta=False):
        print('latido auauauauau')
        if isinstance(animal_presente, Gato):
            self.game.animais.remove(animal_presente)
            self.game.tabuleiro[animal_presente.getPos()[1]][animal_presente.getPos()[0]].remove(animal_presente)
        
        if resposta == False:
            if isinstance(animal_presente, Leao):
                animal_presente.rugir(self, True)
            elif isinstance(animal_presente, Cachorro):
                animal_presente.latir(self, True)
            elif isinstance(animal_presente, Gato):
                animal_presente.miar(self, True)
            elif isinstance(animal_presente, Vaca):
                animal_presente.mugir(self, True)
            elif isinstance(animal_presente, Ovelha):
                animal_presente.balir(self, True)
            elif isinstance(animal_presente, Pulga):
                animal_presente.sugar(self, True)
    
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
    
    def miar(self, animal_presente, resposta=False):
        print('miado miauuuuuuuuu')

        if resposta == False:
            if isinstance(animal_presente, Leao):
                animal_presente.rugir(self, True)
            elif isinstance(animal_presente, Cachorro):
                animal_presente.latir(self, True)
            elif isinstance(animal_presente, Gato):
                animal_presente.miar(self, True)
            elif isinstance(animal_presente, Vaca):
                animal_presente.mugir(self, True)
            elif isinstance(animal_presente, Ovelha):
                animal_presente.balir(self, True)
            elif isinstance(animal_presente, Pulga):
                animal_presente.sugar(self, True)
    
    def getRaca(self):
        return self.raca
    def setRaca(self, newRaca):
        self.raca = newRaca

class Vaca(Animal):
    def __init__(self, nome, cor, sexo, velocidade, peso, stamina, posX, posY, game, raca):
        super().__init__(nome, cor, sexo, velocidade, peso, stamina, posX, posY, game)
        self.raca = raca
    
    def mugir(self, animal_presente, resposta=False):
        print('mugido muuuuuuuuuuuudando todos de lugar lol')
        for animal in self.game.animais:
            newPos = [randint(0,9), randint(0,9)]
            if animal == self:
                continue
            
            self.game.tabuleiro[animal.getPos()[1]][animal.getPos()[0]].remove(animal)
            self.game.tabuleiro[newPos[1]][newPos[0]].append(animal)
            animal.setPos(newPos[0],newPos[1])
            animal.direcaoX = 'direita' 
            animal.direcaoY = 'cima' 

        if resposta == False:
            if isinstance(animal_presente, Leao):
                animal_presente.rugir(self, True)
            elif isinstance(animal_presente, Cachorro):
                animal_presente.latir(self, True)
            elif isinstance(animal_presente, Gato):
                animal_presente.miar(self, True)
            elif isinstance(animal_presente, Vaca):
                animal_presente.mugir(self, True)
            elif isinstance(animal_presente, Ovelha):
                animal_presente.balir(self, True)
            elif isinstance(animal_presente, Pulga):
                animal_presente.sugar(self, True)
    
    def getRaca(self):
        return self.raca
    def setRaca(self, newRaca):
        self.raca = newRaca

class Ovelha(Animal):
    def __init__(self, nome, cor, sexo, velocidade, peso, stamina, posX, posY, game, idade):
        super().__init__(nome, cor, sexo, velocidade, peso, stamina, posX, posY, game)
        self.idade = idade
    
    def balir(self, animal_presente, resposta=False):
        print('balindo meeeeeeeeehhh(+3 stamina)')
        animal_presente.stamina+=3

        if resposta == False:
            if isinstance(animal_presente, Leao):
                animal_presente.rugir(self, True)
            elif isinstance(animal_presente, Cachorro):
                animal_presente.latir(self, True)
            elif isinstance(animal_presente, Gato):
                animal_presente.miar(self, True)
            elif isinstance(animal_presente, Vaca):
                animal_presente.mugir(self, True)
            elif isinstance(animal_presente, Ovelha):
                animal_presente.balir(self, True)
            elif isinstance(animal_presente, Pulga):
                animal_presente.sugar(self, True)

    def getIdade(self):
        return self.idade
    def setIdade(self, newIdade):
        self.idade = newIdade

class Pulga(Animal):
    def __init__(self, nome, cor, sexo, velocidade, peso, stamina, posX, posY, game, idade):
        super().__init__(nome, cor, sexo, velocidade, peso, stamina, posX, posY, game)
        self.idade = idade
    
    def sugar(self, animal_presente, resposta=False):
        print('sugando glubglubglubglub')
        if isinstance(animal_presente, Leao):
            animal_presente.stamina -= 5
            print('A pulga sugou 5 de estamina!')
        elif isinstance(animal_presente, Cachorro):
            animal_presente.stamina -= 3
            print('A pulga sugou 3 de estamina!')
        elif isinstance(animal_presente, Gato):
            animal_presente.stamina -= 1 
            print('A pulga sugou 1 de estamina!')
        elif isinstance(animal_presente, Vaca):
            animal_presente.stamina -= 3
            print('A pulga sugou 3 de estamina!')
        elif isinstance(animal_presente, Ovelha):
            animal_presente.stamina -= 2
            print('A pulga sugou 2 de estamina!')
        elif isinstance(animal_presente, Pulga):
            print('vocês são amigos! A pulga não roubou sua stamina.')
        
        if resposta == False:
            if isinstance(animal_presente, Leao):
                animal_presente.rugir(self, True)
            elif isinstance(animal_presente, Cachorro):
                animal_presente.latir(self, True)
            elif isinstance(animal_presente, Gato):
                animal_presente.miar(self, True)
            elif isinstance(animal_presente, Vaca):
                animal_presente.mugir(self, True)
            elif isinstance(animal_presente, Ovelha):
                animal_presente.balir(self, True)
            elif isinstance(animal_presente, Pulga):
                animal_presente.sugar(self, True)

    def getIdade(self):
        return self.idade
    def setIdade(self, newIdade):
        self.idade = newIdade