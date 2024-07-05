import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import copy as cp
from time import time
from MainGraph0 import G
#from MainGraph1 import G
#from MainGraph2 import G
#from MainGraph3 import G

store= []
count=0
def k_shortest_paths(G, source, target, k = 1, weight = 'weight'):
    global count
    global store

    # G is a networkx graph.
    # source and target are the labels for the source and target of the path.
    # k is the amount of desired paths.
    # weight = 'weight' assumes a weighed graph. If this is undesired, use weight = None.
    C=nx.bidirectional_dijkstra(G, source,target,weight = 'weight')
    D=list(C)
    
    A = []
    A.append(D[-1])
    
    #To calulate the length of the shortest path
    A_len = [sum([G[A[0][l]][A[0][l + 1]]['weight'] for l in range(len(A[0]) - 1)])]
    B = []

    for i in range(1, k):
        
        for j in range(0 , len(A[-1])-1):
            Gcopy = cp.deepcopy(G)
            spurnode = A[-1][j]
            rootpath = A[-1][:j + 1]
            
            for path in A:
              #and len(path) > j?
              if rootpath == path[0:j + 1]:
                if Gcopy.has_edge(path[j], path[j + 1]):
                   Gcopy.remove_edge(path[j],path[j+1])
     
#To remove the root nodes(here n is equal to NODE)            
            for n in rootpath:
                if n != spurnode:
                    Gcopy.remove_node(n)
            try:
                count=count+1
                E = nx.bidirectional_dijkstra(Gcopy, spurnode, target, weight = 'weight')
                F =list(E)
                spurpath=F[-1]
                
            
                # In spurpath Value ranges from 1 onwards
                totalpath = rootpath + spurpath[1:]
                if totalpath not in B:
                    B += [totalpath]
                
            except nx.NetworkXNoPath:
                continue
        
        if len(B) == 0:
            break
        lenB = [sum([G[path[l]][path[l + 1]]['weight'] for l in range(len(path) - 1)]) for path in B]

        B = [p for _,p in sorted(zip(lenB, B))]
        A.append(B[0])
        A_len.append(sorted(lenB)[0])
        B.remove(B[0])
    print(f"Shortest paths found for k={k}are:\n",A)
    print(f"Length of the shortest paths for k={k}:\n",A_len)
    print(f"Dijkstra called {count} number of times")

    store.append(count)
    return store 
    

times = []
for k in range (1,16) : 
    begin = time()
    store_counts = k_shortest_paths(G, source=1, target= 5, k = k, weight = 'weight')
    end = time()
    times.append(end-begin)
    
times = times
print(times)
plt.show()

storage = store_counts

x= []
y= []
x1= []
y1= []


for k in range (1,((len(storage))+1)) :

    x.append(k)
    x1.append(k)
    y.append(storage[k-1])
    y1.append(times[k-1])
    
x=x
y=y
x1=x1
y1=y1

#plot2=plt.figure(2)
plt.bar(x,y,width=0.1)   
plt.xlabel("Number of shortest paths(k)",color='r')
plt.ylabel("Number of times Dijkstra called",color='r')
plt.title("Graph for Dijkstra calls")
plt.scatter(x,y)
plt.show()

#plot3=plt.figure(3)
plt.bar(x1,y1,width=0.1)   
plt.xlabel("Number of shortest paths(k)",color='r')
plt.ylabel("execution time in seconds",color='r')
plt.scatter(x1,y1)
plt.show()
