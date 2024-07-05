# Finding Loopless Multiple Optimal Paths in Road Network  
## Introduction 
The problem of finding the shortest path between two vertices in a graph is fundamental in various applications. It involves minimizing the sum of weights of edges along the path. This report explores the extension of this problem to find the k shortest paths, known as the k shortest path problem. Among the algorithms designed for this purpose, Yen’s algorithm stands out due to its efficiency, particularly in worst-case scenarios.  

## Yen’s Algorithm and Variations  
In this project, we focus on Yen’s algorithm and propose two variations: One to One Yen’s and Bidirectional Yen’s algorithm. These variations aim to enhance the original Yen’s algorithm by addressing specific aspects of path computation efficiency and accuracy.  

## Execution and Result
The execution of Yen’s algorithm and its variations yields k shortest paths, accompanied by their respective lengths. The results are visualized through graphs that compare the performance of these algorithms based on two critical parameters:  

**Time Required:** Represents the computational efficiency of each algorithm variant.  
**Number of Times Dijkstra Called:** Indicates the computational load and efficiency in terms of algorithmic steps. 

## Analysis  
Comparative Analysis of graph is done based on nodes in the graph and the number of paths to be found(i.e k).Here the 25 nodes graph is considered and result is shown in the result_graph file.From the analysis presented in the graphs, it is observed that both One to One Yen’s and Bidirectional Yen’s algorithms improve upon the original Yen’s algorithm. These variations offer enhancements in terms of computational efficiency and effectiveness in finding k shortest paths.  









