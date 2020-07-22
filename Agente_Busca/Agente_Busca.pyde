from cell import Cell
from grid import create_adj_list
from search_module import breadth_first_graph_search, depth_first_search
from astar_search_module import astar_search
from greedy_search_module import greedy_dijkstra_search

from copy import copy, deepcopy

import random
from pprint import pprint
import heapq

# https://py.processing.org/tutorials/2dlists/

# Number of columns and rows in the grid
nCols = 20;
nRows = 20;
nObstaculos = 50
tam_cell = 20
busca_finalizada = False

start = (0,0)
target = (15,11)

matrix_adjc = {}
matrix=[]

#######################################
# Inicializando 
#######################################
def setup():
    global nCols, nRows, grid 
    global caminho_final
    global busca_finalizada
    global start, target
    
    frameRate(1)
    smooth(4);
       
    
    #size(400, 400)
    size(nCols * tam_cell, nRows * tam_cell)
    grid = makeGrid(start, target)
    drawGrid()
    caminho_final = inicia_busca()
    
 
##################################
# Atualizando a tela
##################################
def draw():

    global nCols, nRows, grid
    global busca_finalizada
       
    #background(0)
    
    drawGrid()
    
    # iniciando a busca
    #caminho_final = inicia_busca()
    #draw_path(caminho_final)
    
    # delay()    


#########################
# Função de busca
#########################
def inicia_busca():
    global busca_finalizada
    global start, target
    global nRows, nCols
    global matrix
        
    # converte a matriz em lista de adjacencias
    #grid_adj_list = create_adj_list(grid)
    #pprint(grid_adj_list)
    
    # busca em largura (funcionando)
    #caminho_final = breadth_first_graph_search(matrix_adjc, start, target)
    
    # busca em profundidade (funcionando)
    # caminho_final = depth_first_search(matrix_adjc, start, target)
    
    # busca em Astar (funcionando)
    #caminho_final = astar_search(matrix, 1, start, target, nRows, nCols)
    
    # busca Greedy Dijkstra (funcionando)
    caminho_final = greedy_dijkstra_search(matrix_adjc, start, target)
    
    
    #print(caminho_final)
    #caminho_final = caminho_final[0]
    caminho_final.pop(0)
    caminho_final.pop()
    
    #drawGrid()
    delay(600)
    
    print(caminho_final)
    draw_path(caminho_final)
    
    return caminho_final 

#############################
# Imprime caminho na tela
#############################
def draw_path(caminho):
    global grid
    for i,j in caminho:
        grid[i][j]= Cell(i * tam_cell, j * tam_cell, tam_cell, tam_cell, cor=(255, 204, 0), type="move")
    
################################################
# Criando um grid   
# Creates a 2D List of 0's, nCols x nRows large
################################################
def makeGrid(start, target):
    global nCols, nRows
    global matrix_adjc
    global grid
    global nObstaculos
    global matrix
    
    # criando a matriz
    #matrix = []
    for i in xrange(nRows):
        # Create an empty list for each row
        matrix.append([])
        for j in xrange(nRows):
            # Pad each column in each row with a 0
            matrix[i].append(0)
            
    # criando os obstáculos
    import random
    for i in range(nObstaculos):
        x = random.randint(0,nCols-1) #index X
        y = random.randint(0,nCols-1) #index Y
        matrix[x][y] = 1
    
    # set agent
    #matrix[start[0]][start[1]] = 0#2   
    # target 
    #matrix[target[0]][target[1]] = 0#3
    
    matrix_adjc = create_adj_list(matrix)
                                    
    # criando o grid
    #grid = list(matrix)
    #grid = copy(matrix)
    grid = [row[:] for row in matrix]
     
       
    #print("esse grid")
    #pprint(grid)
    for i in xrange(nCols): #nCols
        for j in xrange(nRows): #nRows
                      
            if grid[i][j] == 0:
                grid[i][j] = Cell(i * tam_cell, 
                                  j * tam_cell, 
                                  tam_cell, 
                                  tam_cell,
                                  type="clear",
                                  cor=(255, 255, 255)) 
            #elif grid[i][j] == 2:
            #    # Initialize each object
            #    grid[i][j] = Cell(i * tam_cell, 
            #                      j * tam_cell, 
            #                      tam_cell, 
            #                      tam_cell, 
            #                      type="agent",
            #                      cor=(102, 153, 153))
            #elif grid[i][j] == 3:
            #    grid[i][j] = Cell(i * tam_cell, 
            #                      j * tam_cell, 
            #                      tam_cell, 
            #                      tam_cell,
            #                      type="target",
            #                      cor=(0, 153, 51))
            elif grid[i][j] == 1:
                #print("Bloco em", i,j)
                grid[i][j] = Cell(i * tam_cell, 
                                  j * tam_cell, 
                                  tam_cell, 
                                  tam_cell,
                                  type="block",
                                  cor=(153, 153, 102))     
    
    # ajustando cor de inicio / fim
    grid[start[0]][start[1]].cor = (102, 153, 153)
    grid[target[0]][target[1]].cor = (0, 153, 51)
    
    
    drawGrid()
    
    print("distancias")
    
    print(grid[start[0]][start[1]].x, grid[start[0]][start[1]].y)    
    print(grid[target[0]][target[1]].x, grid[target[0]][target[1]].y)
    print(int(dist(grid[start[0]][start[1]].x, grid[start[0]][start[1]].y,grid[target[0]][target[1]].x, grid[target[0]][target[1]].y)))         
                    
    return grid


####################
# Desenha o grid
####################
def drawGrid():
    
    #global grid
    background(0)
    for i in xrange(nCols): #nCols
        for j in xrange(nRows): #nRows
            #print("cores")
            #print(i,j, "cor", grid[i][j].cor) 
            grid[i][j].display()
