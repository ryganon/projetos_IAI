from collections import deque


######################################################
# Busca em largura BFS (funcionando)
######################################################
def breadth_first_graph_search(graph, start, target):
    queue = deque([[start]])
    seen = set([start])
    
    while queue:
        # get the first path from the queue
        path = queue.popleft()
        # get the last node from the path
        node = path[-1]
        # path found
        if node == target:
            print("Caminho final:",path)
            return path
        else:
            print("Testando:", path)
            
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        #for adjacent in graph.get(node, []):
        for adjacent in graph[node]:
            if adjacent not in seen:
                seen.add(adjacent)
                # mantendo registro
                #queue.append(list(path).append(adjacent))
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
                
                
###########################################
# Busca em profundidade (funcionando)
# Depth First Search
###########################################
def depth_first_search(graph, start, end):
    queue = deque([[start]])

    seen = set([start])

    while queue:
        # mudando aqui
        path = queue.pop()
    
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            print("Achou:", path)
            return path
        else:
            print("Testando:", path)

        # enumerate all adjacent nodes, construct a new path and push it into the queue
        #for adjacent in graph.get(node, []):
        for adjacent in graph[node]:
            if adjacent not in seen:
                seen.add(adjacent)
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
