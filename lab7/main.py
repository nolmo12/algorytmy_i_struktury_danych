from Graph import *

def visit(data: Any) -> None:
    print(data)

def main():
    graf = Graph()
    graf.create_vertex('A')
    graf.create_vertex('B')
    graf.create_vertex('C')
    graf.create_vertex('D')
    graf.create_vertex('E')
    #graf.create_vertex('F')

    vertex_a = list(graf.adjacencies.keys())[0]
    vertex_b = list(graf.adjacencies.keys())[1]
    vertex_c = list(graf.adjacencies.keys())[2]
    vertex_d = list(graf.adjacencies.keys())[3]
    vertex_e = list(graf.adjacencies.keys())[4]
   #vertex_f = list(graf.adjacencies.keys())[5]

    graf.add_directed_edge(vertex_a, vertex_b)
    graf.add_directed_edge(vertex_b, vertex_c)
    graf.add_directed_edge(vertex_c, vertex_a)
    graf.add_directed_edge(vertex_c, vertex_b)
    #graf.add_directed_edge(vertex_f, vertex_f)

    graf.add_undirected_edge(vertex_c, vertex_d)
    graf.add_undirected_edge(vertex_d, vertex_e)
    #graf.add_undirected_edge(vertex_f, vertex_f)

    graf.traverse_depth_first(vertex_a, [], visit)

    graf.traverse_breadth_first(visit)

if __name__ == '__main__':
    main()