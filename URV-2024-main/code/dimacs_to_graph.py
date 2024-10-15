from cnfgen.utils.parsedimacs import from_dimacs_file
from sat_tools import generate_random_ksat
from cnfgen import CNF
from io import StringIO
import networkx as nx
import matplotlib.pyplot as plt

def dimacs_to_var_var_graph(dimacs):
    with StringIO() as f:
        f.write(dimacs)
        f.seek(0)
        formula = from_dimacs_file(CNF, f)
        graph = nx.Graph()

        for literal in range(1, formula.number_of_variables() + 1):
            graph.add_nodes_from([literal, -literal])

        for clause in formula:
            clause_subgraph = nx.complete_graph(clause)
            graph = nx.compose(graph, clause_subgraph)

        return graph

def dimacs_to_var_clause_graph(dimacs):
    with StringIO() as f:
        f.write(dimacs)
        f.seek(0)
        formula = from_dimacs_file(CNF, f)
        graph = nx.Graph()

        for literal in range(1, formula.number_of_variables() + 1):
            graph.add_nodes_from([literal, -literal])

        for i, clause in enumerate(formula, start=1):  # Start counting clauses from 1
            clause_num = formula.number_of_variables() + i
            graph.add_node(clause_num)  # Add clause node
            for literal in clause:
                graph.add_edge(literal, clause_num)  # Add edge between literal and clause node

        return graph

def extract_features_from_graph(G):
    features = {
        'num_nodes': G.number_of_nodes(),
        'num_edges': G.number_of_edges(),
    }
    return features

#dimacs = "p cnf 5 3\n1 -5 4 0\n-1 5 3 2 0\n-3 -4 0\n"
#var_var_graph = dimacs_to_var_var_graph(dimacs)
#var_clause_graph = dimacs_to_var_clause_graph(dimacs)
# nx.draw(var_clause_graph, with_labels=True)
# plt.show()
