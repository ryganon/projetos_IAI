# coding=utf8

# Projeto de Agente Inteligente
# Descrição: Classe que representa o Agente no ambiente/cenário.
# Autor: Danilo

# Baseado no código em:
# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

class Agente():

    def __init__(self, x, y):
        self.acceleration = PVector(0, 0)
        self.velocity = PVector(0, -2)
        self.position = PVector(x, y)
        self.r = 6
        self.maxspeed = 1 # 4
        self.maxforce = 0.2
        self.itens_encontrados = 0 
        
    ####################################################
    # Atualizando a localização e movimentação do agente
    # no ambiente.
    ####################################################
    def update(self):
        # Update velocity
        self.velocity.add(self.acceleration)
        # Limit speed
        self.velocity.limit(self.maxspeed)
        self.position.add(self.velocity)
        # Reset accelerationelertion to 0 each cycle
        self.acceleration.mult(0)

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)

    #################################################
    # Função principal de busca pelo item na tela
    #################################################
    def procurar(self, item):
        # Iniciando a busca
        # A vector pointing from the location to the target
        desired = item - self.position
        d = desired.mag()

        # Scale with arbitrary damping within 100 pixels
        if (d < 100):
            m = map(d, 0, 100, 0, self.maxspeed)
            desired.setMag(m)
        else:
            desired.setMag(self.maxspeed)

        # Steering = Desired minus velocity
        steer = desired - self.velocity
        steer.limit(self.maxforce)  # Limit to maximum steering force

        self.applyForce(steer)    
                       
    #####################################################
    # Checando se houve colisão entre os objetos.
    # Nessa caso, o agente encontrou o item no ambiente
    #####################################################
    def encontrou(self, item):
        if(dist(self.position.x, self.position.y, item.x, item.y) < 20):
            return True    

    
    #################################################
    # Atualiza o agente na tela.
    #################################################
    def display(self):
        # Draw a triangle rotated in the direction of velocity
        theta = self.velocity.heading() + PI / 2
        fill(127)
        stroke(200)
        strokeWeight(1)
        
        with pushMatrix():
            translate(self.position.x, self.position.y)
            rotate(theta)
            beginShape()
            vertex(0, -self.r * 2)
            vertex(-self.r, self.r * 2)
            vertex(self.r, self.r * 2)
            endShape(CLOSE)
