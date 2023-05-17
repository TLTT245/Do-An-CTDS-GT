class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbors_value = []
        self.neighbors_vertex = []

    def add_neighbor(self, vertex):
        for i in self.neighbors_value:
            if vertex.value == i:
                print("Phần tử", vertex.value, "đã liên kết với", self.value)
                return
        self.neighbors_value.append(vertex.value)
        vertex.neighbors_value.append(self.value)
        ##
        self.neighbors_vertex.append(vertex)
        vertex.neighbors_vertex.append(self)


class UndirectedGraph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        new_vertex = Vertex(value)
        self.vertices[new_vertex] = new_vertex.neighbors_vertex

    def add_edge(self, first_value, second_value):
        first_vertex = None
        second_vertex = None
        for i in self.vertices:
            if i.value == first_value:
                first_vertex = i
            if i.value == second_value:
                second_vertex = i
        if (first_vertex is None) or (second_vertex is None):
            print("Ít nhất 1 đỉnh không tồn tại")
            return
        first_vertex.add_neighbor(second_vertex)
        self.vertices[first_vertex] = first_vertex.neighbors_vertex
        self.vertices[second_vertex] = second_vertex.neighbors_vertex

    def adjacency_list(self):
        for i in self.vertices:
            print(i.value, "->", i.neighbors_value)

    def breadth_first_search(self, start_value):
        ##
        start_vertex = None
        for i in self.vertices:
            if i.value == start_value:
                start_vertex = i
        if start_vertex is None:
            print("Đỉnh không tìm thấy")
            return
        ##
        visited = self.vertices.copy()
        for i in visited:
            visited[i] = False
        queue = []
        queue.append(start_vertex)
        visited[start_vertex] = True
        while queue:
            u = queue.pop(0)
            print(u.value, end=" ")

            for i in u.neighbors_vertex:
                if visited[i] is False:
                    queue.append(i)
                    visited[i] = True

    def depth_first_search(self, start_value):
        ##
        start_vertex = None
        for i in self.vertices:
            if i.value == start_value:
                start_vertex = i
        if start_vertex is None:
            print("Đỉnh không tìm thấy")
            return
        ##
        visited = self.vertices.copy()
        for i in visited:
            visited[i] = False
        stack = []
        stack.append(start_vertex)
        visited[start_vertex] = True
        while stack:
            u = stack.pop()
            print(u.value, end=" ")

            for i in u.neighbors_vertex:
                if visited[i] is False:
                    stack.append(i)
                    visited[i] = True


if __name__ == "__main__":
    graph = UndirectedGraph()
    graph.add_vertex(15)
    graph.add_vertex(2)
    graph.add_vertex(6)
    graph.add_vertex(9)
    graph.add_vertex(13)
    graph.add_edge(2, 6)
    graph.add_edge(2, 9)
    graph.add_edge(9, 15)
    graph.add_edge(13, 15)
    graph.add_edge(13, 9)
    graph.adjacency_list()
    graph.breadth_first_search(13)
    print()
    graph.depth_first_search(13)
