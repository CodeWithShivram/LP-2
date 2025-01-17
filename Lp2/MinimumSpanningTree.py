import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def prim_mst(self):
        key = [sys.maxsize] * self.V
        mst_set = [False] * self.V
        parent = [None] * self.V

        # Start with the first vertex
        key[0] = 0
        parent[0] = -1

        for _ in range(self.V):
            # Find the vertex with the minimum key value
            u = self._min_key(key, mst_set)
            mst_set[u] = True

            # Update key and parent values of adjacent vertices
            for v in range(self.V):
                if (
                    self.graph[u][v] > 0
                    and not mst_set[v]
                    and self.graph[u][v] < key[v]
                ):
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self._print_mst(parent)

    def _min_key(self, key, mst_set):
        min_value = sys.maxsize
        min_index = -1

        for v in range(self.V):
            if not mst_set[v] and key[v] < min_value:
                min_value = key[v]
                min_index = v

        return min_index

    def _print_mst(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(f"{parent[i]} - {i} \t{self.graph[i][parent[i]]}")


# Example usage
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

g.prim_mst()
