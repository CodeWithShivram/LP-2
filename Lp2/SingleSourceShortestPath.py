import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight

    def dijkstra(self, src):
        distance = [sys.maxsize] * self.V
        distance[src] = 0
        visited = [False] * self.V

        for _ in range(self.V):
            u = self._min_distance(distance, visited)
            visited[u] = True

            for v in range(self.V):
                if (
                    not visited[v]
                    and self.graph[u][v] > 0
                    and distance[u] + self.graph[u][v] < distance[v]
                ):
                    distance[v] = distance[u] + self.graph[u][v]

        self._print_solution(distance)

    def _min_distance(self, distance, visited):
        min_value = sys.maxsize
        min_index = -1

        for v in range(self.V):
            if not visited[v] and distance[v] < min_value:
                min_value = distance[v]
                min_index = v

        return min_index

    def _print_solution(self, distance):
        print("Vertex \tDistance from Source")
        for v in range(self.V):
            print(f"{v} \t{distance[v]}")


# Example usage
g = Graph(6)
g.add_edge(0, 1, 2)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 1)
g.add_edge(1, 3, 7)
g.add_edge(2, 4, 3)
g.add_edge(3, 4, 1)
g.add_edge(3, 5, 5)
g.add_edge(4, 5, 2)

g.dijkstra(0)
