import random
import copy
from util import *
class PercolationPlayer:
	# `graph` is an instance of a Graph, `player` is an integer (0 or 1).
    # Should return a vertex `v` from graph.V where v.color == -1
    def ChooseVertexToColor(graph, player):
        return random.choice([v for v in graph.V if v.color == -1])


    # `graph` is an instance of a Graph, `player` is an integer (0 or 1).
    # Should return a vertex `v` from graph.V where v.color == player
    def ChooseVertexToRemove(graph, player):
        # for v in [i for i in graph.V if i.color == player]:
        #     neighbors = Neighbors(graph, v)
        #     print(v, neighbors)
        #     for n in [i for i in neighbors if i.color == player]:
        #         if countEdges(graph, n) != 1:
        #             print("works")
        #             for n in [i for i in neighbors if i.color != player]:
        #                 if countEdges(graph, n) == 1:
        #                     print("works")
        #                     return v
        # return random.choice([v for v in graph.V if v.color == player])
        original = graph
        percentage = -1
        bestVertex = None
        for v in [i for i in graph.V if i.color == player]:
            neighbors = Neighbors(graph, v)
            print(neighbors)
            for n in neighbors:
                if n.color != player:
                    print("WORKING")
                    # Percolate(graph,v)
                    wins = Benchmark(0, graph)
                    print(wins)
                    if wins[0] > 60:
                        bestVertex = v
                        break
                    if wins[0] > percentage:
                        percentage = wins[0]
                        bestVertex = v
            graph = original
        return bestVertex
            # run simulation for v which returns win percentage

    # Feel free to put any personal driver code here.
    def main():
        pass

    class Vertex:
        # `index` is a unique integer identifier, `color` is an integer in [-1, 0, 1].
        # Silver vertices have color=0, and teal vertices have color=1.
        # Unmarked vertices have color=-1.
        def __init__(self, index, color=-1):
            self.index = index
            self.color = color

    class Edge:
        # `a` and `b` are Vertex objects corresponding to the endpoints of this edge.
        def __init__(self, a, b):
            self.a = a
            self.b = b

    class Graph:
        # `vertices` and `edges` are iterables of Vertex and Edge objects respectively
        # Internally, we store these as set()s on the graph class.
        def __init__(self, vertices, edges):
            self.V = set(vertices)
            self.E = set(edges)

        if __name__ == "__main__":
            main()

def Neighbors(graph, v):
    set1 = set()
    for e in graph.E:
        if e.a == v:
            set1.add(e.b)
        elif e.b == v:
            set1.add(e.a)
    return set1
def countEdges(graph, v):
    numEdges = 0
    for e in graph.E:
        if (e.a == v or e.b == v):
            numEdges += 1
    print("works2")
    return numEdges

def Simulate(graph, active_player):
    graph_copy = copy.deepcopy(graph)

    # Phase 1: Coloring Phase
    while any(v.color == -1 for v in graph_copy.V):
        # First, try to just *run* the player's code to get their vertex.
    
        chosen_vertex = random.choice([v for v in graph_copy.V if v.color == -1])

        # If output is reasonable, color this vertex.
        chosen_vertex.color = active_player
        # Only case when this should fire is if chosen_vertex.index does not exist or similar error.
        
        # Swap current player.
        active_player = 1 - active_player

    # Check that all vertices are colored now.
    assert all(v.color != -1 for v in graph_copy.V)
    # Phase 2: Removal phase
    # Continue while both players have vertices left to remove.
    while len([v for v in graph_copy.V if v.color == active_player]) > 0:
        # First, try to just *run* the removal code.
    
        chosen_vertex = random.choice([v for v in graph_copy.V if v.color == active_player])
                
        # If output is reasonable, remove ("percolate") this vertex + edges attached to it, as well as isolated vertices.
        Percolate(graph_copy, chosen_vertex)
        # Only case when this should fire is if chosen_vertex.index does not exist or similar error.
        
        # Swap current player
        active_player = 1 - active_player

    # Winner is the non-active player.
    return 1 - active_player

def Benchmark(activePlayer, graph):
    # graphs = (
    #     BinomialRandomGraph(random.randint(1, 20), random.random())
    #     # BinomialRandomGraph(2, random.random())
    #     for _ in range(iters)
    # )
    # a = Vertex(0)
    # b = Vertex(1)
    # e = Edge(a,b)
    # graphs = [Graph({a,b},{e})]
    wins = [0, 0]
    # for graph in graphs:
    # print(graph)
    # g1 = copy.deepcopy(graph)
    # g2 = copy.deepcopy(graph)
    # Each player gets a chance to go first on each graph.
    for i in range(100):
        winnerPlayer = Simulate(graph, activePlayer)
        wins[winnerPlayer] += 1
    # winner_b = PlayGraph(p2, p1, graph)
    # wins[1-winner_b] += 1
    print(wins)
    return wins

# Removes the given vertex v from the graph, as well as the edges attached to it.
# Removes all isolated vertices from the graph as well.
def Percolate(graph, v):
    # Get attached edges to this vertex, remove them.
    for e in IncidentEdges(graph, v):
        graph.E.remove(e)
    # Remove this vertex.
    graph.V.remove(v)
    # Remove all isolated vertices.
    to_remove = {u for u in graph.V if len(IncidentEdges(graph, u)) == 0}
    graph.V.difference_update(to_remove)

# Returns the incident edges on a vertex.
def IncidentEdges(graph, v):
    return [e for e in graph.E if (e.a == v or e.b == v)]