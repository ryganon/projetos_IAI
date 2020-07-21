# coding=utf8

# coding=utf8

# Projeto de Agente Inteligente
# Descrição: Classe que representa um item que será colocado no ambiente.
# Autor: Danilo


class Item():
    
    def __init__(self):
        self.max_x = 750
        self.max_y = 350
        self.raio = 20
        self.item_atual = self.criar_novo()
        
    def posicionar(self):
        
        item = self.item_atual
    
        # Configurando o item
        fill(127)
        stroke(200)
        strokeWeight(2)
        
        # Desenhando o item como círculo
        circle(item.x + 10, item.y + 10, item.z)
    
    def criar_novo(self):
        return PVector(random(10, self.max_x), random(10, self.max_y), self.raio)
