# Search methods
import search

####################
tests = (('A', 'B'), ('O', 'E'), ('G', 'Z'), ('N', 'D'), ('M', 'F'))

for inicio, objetivo in tests:
    print(f"\n\n--------------- RUTA {inicio}->{objetivo} ---------------\n")
    problem = search.GPSProblem(inicio, objetivo
                       , search.romania)

    print("\n- Búsqueda en amplitud:")
    print("Ruta: ",search.breadth_first_graph_search(problem)[0].path())
    print("Generados: ", search.breadth_first_graph_search(problem)[1])
    print("Visitados: ", search.breadth_first_graph_search(problem)[2])
    print("Coste total: ", search.breadth_first_graph_search(problem)[3])

    print("\n- Búsqueda en profundidad:")
    print("Ruta:",search.depth_first_graph_search(problem)[0].path())
    print("Generados: ", search.depth_first_graph_search(problem)[1])
    print("Visitados: ", search.depth_first_graph_search(problem)[2])
    print("Coste total: ", search.depth_first_graph_search(problem)[3])
