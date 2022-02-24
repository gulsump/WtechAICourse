import numpy
import csv
import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()

##key is city name in sozluk
##values is neighbours of city and their distances list
sozluk = {}

##name of cities list
listcity=[]
## all csv file rows in satirlar list
satirlar=[]      
  

def aStarAlgorithm(route, files):
        # open_list is a list of cities which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of cities which have been visited
        # and who's neighbors have been inspected
    open_list = set([route[0]])
    closed_list = set([])

    
    ##open csv file and save values as a dictionary
    with open(files) as dosyam:

        file = csv.reader(dosyam)
        for string in file:
            ct1 = string[0]
            ct2 = string[1]
            dist = int(string[2])
            sozluk.setdefault(ct1, []).append([ct2, dist])
            sozluk.setdefault(ct2, []).append([ct1, dist])
            listcity.append(ct1)
            listcity.append(ct2)
            satirlar.append(string)
            
        ##list of all cities         
        unique_city = list(set(listcity))

    ##draw cities a graph with their weight(distances)
    G.add_weighted_edges_from(satirlar)

    pos=nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    edge_weight = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_weight)
    
    #control of input values in given city list
    if route[0] not in unique_city:
        print("Starting city is not found!!!" )
    elif route[1] not in unique_city:
        print("Ending city is not found!!!" )
    else:
        

            
        adjacency_list=sozluk 

        #Heuristic values equal 1
        #we assumed that
        def h(n):
            
            H = {}
            one=numpy.ones(len(unique_city ))
               
                  
            H=dict(zip(unique_city ,one))
             
            return H[n]

        # g contains current distances from start city to all other cities
        
        g = {}

        g[route[0]] = 0

        ## came_from contains an adjacency map of all cities
        came_from = {}
        came_from[route[0]] = route[0]

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f()  evaluation function
            for v in open_list:
                if n == None or g[v] + h(v) < g[n] + h(n):
                    n = v;


            # if the current node is the stop city
            # then we begin reconstructin the path from it to the start city
            if n == route[1]:
                path = []

                while came_from[n] != n:
                    path.append(n)
                    n = came_from[n]

                path.append(route[0])

                path.reverse()

                ## print output desired format
                outputs=''
                for q in range(len(path)):
                    
                    outputs= outputs + '-' + path[q]
                outputs=outputs + ',' + str(g[path[-1]])
                ##print(outputs)



                # paint route cities with red colur
                nc = nx.draw_networkx_nodes(G, pos, nodelist=path, node_color="red", 
                            with_labels=False, node_size=75, cmap=plt.cm.jet)

                
                return outputs

            # for all neighbors of the current node do
            #for (m, weight) in get_neighbors(n):
            for (m, weight) in adjacency_list[n]:
                    # if the current node isn't in both open_list and closed_list
                    # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    came_from[m] = n
                    g[m] = g[n] + int(weight)

                    

                    # otherwise, check if it's quicker to first visit n, then m
                    # and if it is, update parent data and g data
                    # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        came_from[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

                # remove n from the open_list, and add it to closed_list
                # because all of his neighbors were inspected

            
            open_list.remove(n)
            closed_list.add(n)
        
        print('Path does not exist!')
        return None

        
aStarAlgorithm(['Bursa','Kayseri'],"distances.csv")
plt.show()
