# from MarkovChain.markov_chain import MarkovChain
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def visualize(nodes: list, edges: list, filepath: str) -> None:
    graph = nx.Graph()

    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)

    nx.draw(graph)
    plt.savefig(filepath)
    plt.show()

def steady_state_vector(matrix: np.ndarray, starting: np.ndarray) -> np.ndarray:
    new = np.array([0, 0, 0])

    while True:
        new = np.matmul(starting, matrix)
        
        if (starting[0] == new[0]) and (starting[1] == new[1]) and (starting[2] == new[2]):
            break
            
        starting = new
    
    return new

if __name__ == '__main__':
    chain = MarkovChain()

    chain.add_edge(1, 2, 0.6)
    chain.add_edge(2, 1, 0.3)
    chain.add_edge(1, 1, 0.2)
    chain.add_edge(2, 3, 0.7)
    chain.add_edge(3, 3, 0.5)
    chain.add_edge(3, 1, 0.5)
    chain.add_edge(1, 3, 0.2)


    edges = [(edge[0], edge[1][0]) for edge in chain.get_edges()]
    nodes = chain.get_nodes()

    visualize(nodes, edges, './assets/graphs/graph1.png')

    print(edges)
    print(nodes)
    print()

    matrix = np.array(chain.transition_matrix())

    # sum of vector for the starting paramater should always equal 1!!!! 
    eigen_vector = steady_state_vector(matrix, np.array([0, 1, 0]))

    print(eigen_vector)
    print(np.matmul(eigen_vector, matrix))
    print(sum(eigen_vector))
    print(sum(np.matmul(eigen_vector, matrix)))

    '''
    eigen_val, eigen_vector = np.linalg.eig(matrix  )
    steady_state_vector = eigen_vector[:, 0]
    steady_state_vector = steady_state_vector/sum(steady_state_vector)

    print(steady_state_vector)
    print(np.matmul(steady_state_vector, matrix))
    '''

    # visualize(nodes, edges, './assets/graphs/')