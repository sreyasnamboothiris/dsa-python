from collections import deque


class Graph:

    def __init__(self):
        self.graph = {}

    def insert(self, vertex, edge, bidirctional=True):

        if vertex not in self.graph:
            self.add_vertex(vertex)
        if edge not in self.graph:
            self.add_vertex(edge)

        self.graph[vertex].append(edge)
        if bidirctional:
            self.graph[edge].append(vertex)

    def add_vertex(self, data):
        self.graph[data] = []

    def display(self):
        for key, value in self.graph.items():
            print('vertex: ', key, ' edge: ', value)

    def bfs(self,start):
        visted = set()
        ar = [start]
        visted.add(start)
        while ar:
            val = ar.pop(0)
            print(val, end=' ')
            for edge in self.graph[val]:
                if edge not in visted:
                    visted.add(edge)
                    ar.append(edge)

    def dfs(self,start,visted = None):
        if visted is None:
            visted = set()
        visted.add(start)
        print(start,end=' ')
        for edge in self.graph.get(start,[]):
            if edge not in visted:
                self.dfs(edge,visted)




gr = Graph()
gr.insert('A', 'B',False)
gr.insert('A', 'C',False)
gr.insert('B', 'D', False)
gr.insert('B', 'E')
gr.insert('C', 'F')
gr.display()
gr.dfs('A')
gr.bfs('B')





