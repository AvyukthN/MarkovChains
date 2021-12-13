from Algorithm.MarkovChain.steady_state_vector import steady_state_vector
from Algorithm.MarkovChain.steady_state_vector import visualize 
from Algorithm.MarkovChain.markov_chain import MarkovChain
import numpy as np
import matplotlib.pyplot as plt

def construct_transition_matrix(move_freq: list, moves: list) -> np.ndarray:
    prob_hash = {}
    move_freq = move_freq
    moves = moves
    sum_moves = sum(move_freq)

    for i in range(len(moves)):
        prob_hash.update({moves[i]: move_freq[i]/sum_moves})

    for i in range(0, 38):
        next_nodes = []

        if i == 30:
            next_nodes = [[10, 1.0]]
        else:
            for j in range(len(moves)):
                ending_node = i+moves[j]
                if ending_node > 38:
                    ending_node = ending_node - 38
                
                cost = prob_hash[moves[j]]

                next_nodes.append([ending_node, cost])
        
        for next_node in next_nodes:
            mc.add_edge(i, next_node[0], next_node[1])
    
    transition_matrix = np.array(mc.transition_matrix())

    return transition_matrix

if __name__ == '__main__':
    mc = MarkovChain()
    
    move_freq = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
    moves = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    transition_matrix = construct_transition_matrix(move_freq, moves)

    starting_vector = [0 for i in range(39)]
    starting_vector[28] = 1

    eigen_vector = steady_state_vector(transition_matrix, np.array(starting_vector)) 

    x = []
    for i in range(len(eigen_vector)):
        x.append(i+1) 
        print(f'{i+1} {eigen_vector[i]}')
    
    nodes = mc.get_nodes()
    edges = [(edge[0], edge[1][0]) for edge in mc.get_edges()]

    visualize(nodes, edges, './assets/graphs/MonopolyGraph.png')