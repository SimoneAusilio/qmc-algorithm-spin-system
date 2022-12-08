import Projet_Code
from breakup_graph import plaquette_graph
import numpy as np
import numpy.random as rnd
import weights
import matplotlib.pyplot as plt
from matplotlib import collections  as mc 
from square import Square
import configuration
import vertex


class Graph_chessboard():
    def __init__(self,chess):
        self.size = chess.size
        self.m = chess.m
        self.graph_chessboard = self._update_graph_chessboard(chess)
        self.lines = self._get_lines_graphboard(chess)
        

    def _update_graph_chessboard(self,chess):
        tab = np.empty((2*self.m,self.size), dtype=plaquette_graph)
        for j in range(self.size):
            for i in range(2*self.m):
                if (i+j)%2 == 0:
                    "if there are black square, no information is needed"
                    tab[i][j] = np.nan
                else:
                    "instantiating white graphs"
                    n = chess.worldsquare_board[i][j]._get_square_type()
                    if n == 1 or n == 2:
                        if rnd.random() < weights.prob(n,1, chess.Dtau, chess.Jx, chess.Jz):
                            tab[i][j] = plaquette_graph(1)
                        else : 
                            tab[i][j] = plaquette_graph(2)
                    elif n == 3 or n == 4:
                        if rnd.random() < weights.prob(n,2, chess.Dtau, chess.Jx, chess.Jz):
                            tab[i][j] = plaquette_graph(2)
                        else : 
                            tab[i][j] = plaquette_graph(4)
                    elif n == 5 or n == 6:
                        if rnd.random() < weights.prob(n,1, chess.Dtau, chess.Jx, chess.Jz):
                            tab[i][j] = plaquette_graph(1)
                        else : 
                            tab[i][j] = plaquette_graph(4)
        self.graph_chessboard = tab
        return tab
        
    def _get_lines_graphboard(self,chess):
        "return a liste line with all the worldlines in it"
        config = self.graph_chessboard 
        lines = []

        b,a = len(config),len(config[0])
        
        for i in range(0,a):
            for j in range(0,b):
                if (j+i)%2 == 1:
                    #scanning all the white square
                    #add to lines[] the corresponding segment for a given position and type of square
                    bu_t = config[j][i]._get_breakup_type()
                    if bu_t == 1:
                        #vertical lines
                        lines.append([(i,j),(i,(j+1))]) 
                        lines.append([(i+1,j),(i+1,j+1)])
                    if bu_t == 2:
                        #horizontal lines
                        lines.append([(i,j),(i+1,j)])
                        lines.append([(i,j+1),(i+1,j+1)])
                    if bu_t == 4:
                        #diagonal lines
                        lines.append([(i,j),(i+1,j+1)])
                        lines.append([(i,j+1),(i+1,j)])
        return lines

    def _plot_graph_chessboard(self,chess):   
        "plot the chessboard with its current wordlines"
        "Beginning figure"
        fig, ax = plt.subplots()
        z1 = chess.binary_chessboard
        extent1 = chess.extent
        lines = self.lines
        #plotting the chessboard without the worldlines yet
        plt.imshow(z1, cmap='binary_r', interpolation='nearest', extent=extent1, alpha=1, aspect=1)
        
        #getting and plotting the lines in lines[]
        color_red = (1, 0, 0, 1)

        lc = mc.LineCollection(lines, colors=color_red, linewidths=4)
        ax.add_collection(lc)
        ax.xaxis.tick_top()

        plt.show()
    
    """ IS NOT WORKING    
    def _get_loops(self):
        "return a list of all differents loops with corresponding coordinates"
        config = self.graph_chessboard 
        L = self.size
        m = self.m
        loop = []
        lines = self.lines
        #reorganizing the lines list modulo L and 2*m
        for number_line in range(len(lines)):
            for coordinate1 in range(2):
                if lines[number_line][coordinate1][0] == L:
                    lines[number_line][coordinate1] = (0,lines[number_line][coordinate1][1])
                if lines[number_line][coordinate1][1] == 2*m:
                    lines[number_line][coordinate1] = (lines[number_line][coordinate1][1],1)   
        
        b,a = len(config),len(config[0])
        
        #browse all points
        for j in range(0,b):
            for i in range(0,a):
                #checking if the current coordinates is already in a loop
                not_in_a_loop = True
                for loop_number in range (len(loop)):
                    if (i,j) in loop[loop_number]:
                        not_in_a_loop = False

                #if not finding the new loop associated with this coordinates
                if not_in_a_loop:
                    (k,p) = (i,j)
                    local_loop = [(k,p)]

                    safety = 0
                    while True: 
                        #seaching the next k,l
                        in_lines = False
                        point = 0
                        print("we are searching:", k, p )
                        while not (in_lines) and point<len(lines):
                            if lines[point][0] == (k,p):
                                next_k,next_p= lines[point][1]
                                print("prevision next boucle 1:",next_k,next_p)
                                #verifying the next point is not already registered
                                if len(local_loop)>=2:
                                    past_k,past_p = local_loop[-2]
                                    if (past_k,past_p) !=(next_k,next_p):  
                                        in_lines = True
                                        print("previsin confirm")
                                else : 
                                    in_lines = True
                                    print("prevision confirm")
                                
                            if lines[point][1] == (k,p):
                                next_k,next_p = lines[point][0]
                                print("prevision next boucle 2:",next_k,next_p)
                                #verifying the next point is not already registered
                                if len(local_loop)>=2:
                                    if len(local_loop)>=2:
                                        past_k,past_p= local_loop[-2]
                                        if (past_k,past_p) !=(next_k,next_p): 
                                            in_lines = True
                                            print("prevision confirm")
                                else : 
                                    in_lines = True
                                    print("prevision confirm")
                            
                            if in_lines:
                                k,p = next_k,next_p
                                local_loop.append((k,p))
                                print(local_loop)
                                break
                            
                            point+=1
                            

                        #si on a trouvé (i,j) dans la liste on continue sinon on passe au i,j suivant
                        if in_lines:
                            if (k,p) == (i,j):
                                loop.append(local_loop)
                                break
                        
                        else : 
                            print("did not find", k, p)
                            break
                        
                        if safety == 200:
                            print("echec loop boucle")
                            break
                        safety +=1
            print("in the branche i,j: ",i,j)
        return loop """

    def _get_loops2(self,chess):
        "return a list of all differents loops with corresponding coordinates"
        config_graph = self.graph_chessboard 
        L = self.size
        m = self.m
        config_square = chess.worldsquare_board
        
        loop = []
        
        #browse all points
        for j in range(0,L):
            for i in range(1,2*m):
                if (i+j)%2 == 1:
                    

                    #checking if the current coordinates is already in a loop
                    not_in_a_loop = True
                    for loop_number in range (len(loop)):
                        if (i,j,0,0) in loop[loop_number]:
                            not_in_a_loop = False

                    #if not finding the new loop associated with this coordinates
                    if not_in_a_loop:
                        
                        local_loop = [(i,j,0,0)]

                        a,b = i,j #a, b the changing indices
                        if i == 2*m:
                            a = 2*m-1 if b%2 ==0 else 0
                        if j == L:
                            b = L-1 if a%2 == 0 else 0
                        rho, sigma = 0,0 #starting with the left top arrow
                        key = 0

                        # emulation of do-while loop to create the path
                        while True:
                            track_outward = True #to verify in which case we are
                            key +=1 #a verification that the algorithm will not loop infinitly,if key>500 return False
                            
                            #if we already have that coordonates in the local_loop we break
                            if (a,b,rho,sigma) == (i,j,0,0) and len(local_loop)>1:
                                if local_loop[-1] == local_loop[0]:
                                    local_loop = local_loop[1:]
                                loop.append(local_loop)
                                break
                            

                            v=vertex.to_vertices(config_square[a][b])
                            # outward arrow
                            if v[rho][sigma] == -1:
                                
                                # upper square
                                if rho == 0:
                                    
                                    a=a-1 if a!=0 else 2*m-1
                                    # left
                                    if sigma==0:
                                        b=b-1 if b!=0 else L-1
                                        rho, sigma=1, 1
                                    #right
                                    else:
                                        b=(b+1)%L
                                        rho, sigma=1, 0
                                
                                # lower square
                                else:
                                    
                                    a=(a+1)%(2*m)
                                    if sigma == 0:
                                        b=b-1 if b!=0 else L-1
                                        rho, sigma=0, 1
                                    else:
                                        b=(b+1)%L
                                        rho, sigma=0, 0
                            

                            # inward arrow 
                            else:
                                
                                track_outward = False
                                # find the outward arrows according to the graph_board

                                bu_t =  config_graph[a][b]._get_breakup_type()
                                if bu_t == 1:
                                    if rho == 0:
                                        rho = 1
                                    elif rho == 1:
                                        rho = 0
                                if bu_t == 2: 
                                    if sigma == 0:
                                        sigma = 1
                                    elif sigma == 1:
                                        sigma = 0
                                if bu_t == 4:
                                    if rho == 0 and sigma == 0:
                                        rho,sigma = 1,1
                                    elif rho == 1 and sigma == 1:
                                        rho, sigma = 0,0
                                    else: 
                                        rho,sigma = sigma, rho
                                

                            
                            local_loop.append((a,b,rho,sigma))
                                

                            if key == 1000: 
                                print("échec du while true")
                                return False

         
        
        return loop 

    def _do_loop_update(self,chess):
        "do a loop update"
        #config_graph = self.graph_chessboard 
        L = self.size
        m = self.m
        loop = self._get_loops2(chess)
        
        #do the change with prob 1/2
        for i in range (len(loop)):
            test = rnd.randint(1,3)
            
            if test == 1:
                path = loop[i]

                #if the first arrow is inward we delete it and place it at the end of the loop
                #the first arrow is then always outward and we can flip two by two
                
                a,b = path[0][0],path[0][1]

                v=vertex.to_vertices(chess.worldsquare_board[a][b])
                
                 #putting the inward and outward arrow near each other
                if v[path[0][2]][path[0][3]]== -1:
                    path = np.vstack((path,path[0]))
                    path = path[1:]
                
                
               
                
                # flip the arrows and change the squares
                for k in range(0,len(path),2):
                    a,b = path[k][0],path[k][1]
                        
                    v=vertex.to_vertices(chess.worldsquare_board[a][b])
                    v[path[k][2]][path[k][3]]*=-1
                    v[path[k+1][2]][path[k+1][3]]*=-1
                    
                    n=vertex.to_square(v)
                    if n!=0:
                        chess.worldsquare_board[a][b]._update(n)
            
                    
        chess._update_wordlines_board()
        self._update_graph_chessboard(chess)
        



                        
                       


