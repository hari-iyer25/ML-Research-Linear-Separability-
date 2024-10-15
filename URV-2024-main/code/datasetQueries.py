import sqlite3
from dimacs_to_graph import dimacs_to_var_clause_graph, extract_features_from_graph
from torch_geometric.data import Data
import torch
from random import shuffle

conn = sqlite3.connect("./db/SAT.sqlite")
cursor = conn.cursor()
cursor.execute("SELECT * FROM linsep_formulas")
all_data = cursor.fetchall()
conn.close()

shuffle(all_data)

train_end = int(len(all_data) * 0.6)
val_end = train_end + int(len(all_data) * 0.15)

training_data = all_data[:train_end]
validation_data = all_data[train_end:val_end]
test_data = all_data[val_end:]

def create_data_objects(data):
    data_objects = []
    for dimacs_formula, num_vars, num_clauses, num_sols in data:
        G = dimacs_to_var_clause_graph(dimacs_formula)
        features = extract_features_from_graph(G)
        label = 1 if num_sols > 0 else 0 
        node_features = [[features['num_nodes']]] * features['num_nodes']
        edge_index = list(G.edges())
        data_object = Data(x=torch.tensor(node_features, dtype=torch.float),
                           edge_index=torch.tensor(edge_index, dtype=torch.long).t().contiguous(),
                           y=torch.tensor([label], dtype=torch.long))
        data_objects.append(data_object)
    return data_objects

training_data_objects = create_data_objects(training_data)
validation_data_objects = create_data_objects(validation_data)
test_data_objects = create_data_objects(test_data)

# print(training_data_objects)

