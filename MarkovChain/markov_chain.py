class MarkovChain:
    def __init__(self):
        self.graph = {}
    
    def transition_matrix(self) -> list:
        edges = self.get_edges()
        nodes = self.get_nodes()

        matrix = [[0 for i in range(len(nodes))] for i in range(len(nodes))]

        for edge in edges:
            starting = edge[0]
            ending = edge[1][0]
            cost  = edge[1][1]

            matrix[starting-1][ending-1] = cost

        return matrix
    
    def matrix_to_str(self, matrix: list = None) -> str:
        if matrix == None:
            matrix = self.transition_matrix()
        
        nodes = self.get_nodes()
        nodes.sort()
        nodes = [str(node) for node in nodes]

        sorted = '   ' + '  '.join(nodes) + '\n'
        
        final_str = [sorted]
        for i in range(len(matrix)):
            temp_str = ""
            for j in range(len(matrix[i])):
                temp_str += str(matrix[i][j]) + "  "
            
            final_str.append(temp_str + '\n')

        for i in range(1, len(final_str)):
            final_str[i] = f'{nodes[i-1]}| ' + final_str[i]

        return ''.join(final_str)
    
    def add_edge(self, starting: int, ending: int, cost: int) -> None:
        if starting not in self.graph.keys():
            self.graph.update({starting: []})
        if ending not in self.graph.keys():
            self.graph.update({ending: []})

        self.graph[starting].append((ending, cost))
    
    def get_edges(self) -> list:
        edges = []

        for key, val in self.graph.items():
            for i in range(len(val)):
                edges.append((key, val[i]))
        
        return edges
    
    def get_nodes(self) -> list:
        edges = self.get_edges()

        nodes = {key: False for key, val in self.graph.items()}

        for edge in edges:
            if not nodes[edge[0]]:
                nodes.update({edge[0]: True})
            if not nodes[edge[1][0]]:
                nodes.update({edge[1][0]: True})
        
        return list(nodes.keys())