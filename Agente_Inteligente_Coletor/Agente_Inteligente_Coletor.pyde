# Projeto de Agente Inteligente
# Objetivo: Agente deve coletar items no cenário
# Autor: Danilo

# Código baseado em: 
# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Implements Craig Reynold's autonomous steering behaviors
# One vehicle "seeks"
# See: http://www.red3d.com/cwr/

from Agente import Agente
from Item import Item

#################################################
# Este código representa o ambiente onde o agente
# deve atuar.
#
# Configuração inicial do ambiente:
# 1 Agente
# 1 Item    
#################################################
def setup():
    global agente
    global item 
    
    # tamanho da tela
    size(800, 400)
    
    # criando agente na tela (triângulo)
    agente = Agente(width / 2, height / 2)
    
    # Criando objeto item. 
    # Um item inicial é criado de forma automática.                       
    item = Item()
     

#################################################
# Loop de execução do ambiente
#################################################
def draw():
    background(255)
    
    # Adiciona o item no ambiente atual.
    #item.posicionar(item.item_atual)
    item.posicionar()
    
    # O agente deve procurar pelo item na tela.
    agente.procurar(item.item_atual)

    # Verificando se o agente atingiu seu objetivo.
    # Se o obetivo for atingido, o sistema deve
    # criar um novo item no ambiente.
    if agente.encontrou(item.item_atual):
        item.item_atual = item.criar_novo()
        agente.itens_encontrados += 1
        print("Total de itens encontrados:", agente.itens_encontrados)
        
    # Atualizando o agente no ambiente.
    agente.update()
    agente.display()
    
    
def adicionar(item):
    # Configurando o item
    fill(127)
    stroke(200)
    strokeWeight(2)
    
    # Desenhando o item como elipse
    circle(item.x, item.y, item.z)
