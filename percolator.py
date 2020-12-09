import random
import copy
import time
#hi
class PercolationPlayer:
	# `graph` is an instance of a Graph, `player` is an integer (0 or 1).
    # Should return a vertex `v` from graph.V where v.color == -1
    def ChooseVertexToColor(graph, player):
        return random.choice([v for v in graph.V if v.color == -1])
        # bestVertex = None
        # mostEdges = 0
        
        # for v in 

    # `graph` is an instance of a Graph, `player` is an integer (0 or 1).
    # Should return a vertex `v` from graph.V where v.color == player

    def ChooseVertexToRemove(graph, player):
        bestWinRate = 0.0
        bestVertex = None
        myV = [i for i in graph.V if i.color == player]
        for v in myV:
            graph_copy = copy.deepcopy(graph)
            Percolate(graph_copy,v.index)
            wins = Benchmark(1-player, graph_copy, .3/len(myV))
            winRate = wins[player]/sum(wins)
           
            if winRate > bestWinRate:
                bestWinRate = winRate
                bestVertex = v
           
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
    return numEdges

def Simulate(graph_copy, active_player):
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
        Percolate(graph_copy, chosen_vertex.index)
        # Only case when this should fire is if chosen_vertex.index does not exist or similar error.
        
        # Swap current player
        active_player = 1 - active_player

    # Winner is the non-active player.
    return 1 - active_player

def Benchmark(activePlayer, graph, timeBudget):
    wins = [0, 0]
    start = time.time()
    elapsed = 0
    while time.time() - start < timeBudget:

        winnerPlayer = Simulate(graph, activePlayer)
        wins[winnerPlayer] += 1

    # winner_b = PlayGraph(p2, p1, graph)
    # wins[1-winner_b] += 1
    return wins

# Removes the given vertex v from the graph, as well as the edges attached to it.
# Removes all isolated vertices from the graph as well.
def Percolate(graph, index):
    v = None
    for j in graph.V:
        if j.index == index:
            v = j
    # Get attached edges to this vertex, remove them.
    to_remove = set()
    # edges = IncidentEdges(graph, v)
    for e in [edges for edges in graph.E if (edges.a == v or edges.b == v)]:
        neigbor = None
        if e.a == v:
            neighbor = e.b
        else:
            neighbor = e.a
        if countEdges(graph, neighbor) == 1:
            to_remove.add(neighbor)
        graph.E.remove(e)
    # Remove this vertex.
    graph.V.remove(v)
    
    graph.V.difference_update(to_remove)

# Returns the incident edges on a vertex.
# def IncidentEdges(graph, v):
#     return [e for e in graph.E if (e.a == v or e.b == v)]