import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.data import DataLoader
from torch_geometric.nn import global_mean_pool
from datasetQueries import training_data_objects, validation_data_objects, test_data_objects

batch_size = 32

train_loader = DataLoader(training_data_objects, batch_size=batch_size, shuffle=True)
val_loader = DataLoader(validation_data_objects, batch_size=batch_size, shuffle=False)
test_loader = DataLoader(test_data_objects, batch_size=batch_size, shuffle=False)

class SimpleGNN(torch.nn.Module):
    def __init__(self, feature_size, output_size):
        super(SimpleGNN, self).__init__()
        self.fc1 = nn.Linear(feature_size, 16)  
        self.fc2 = nn.Linear(16, output_size)  

    def forward(self, data):
        x = data.x.squeeze()
        x = F.relu(self.fc1(x))  
        x = F.dropout(x, training=self.training) 
        x = self.fc2(x)  
        return F.log_softmax(x, dim=1)  

feature_size = 2 # restored original value 
output_size = 2 
model = SimpleGNN(feature_size, output_size)

optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
criterion = torch.nn.CrossEntropyLoss()

num_epochs = 20

for epoch in range(num_epochs):
    model.train()  
    total_loss = 0
    for data in train_loader:
        optimizer.zero_grad() 
        out = model(data) 
        loss = criterion(out, data.y)  #Maybe loss = criterion(out, data.y.view(-1))?
        loss.backward()  
        optimizer.step() 
        total_loss += loss.item()
    print(f'Epoch {epoch+1}: Training Loss: {total_loss / len(train_loader)}')


# correct = 0
# total = len(test_loader.dataset)

# model.eval()
# with torch.no_grad():
#     for data in test_loader:
#         out = model(data)
#         pred = out.argmax(dim=1) 
#         correct += int((pred == data.y).sum())

# accuracy = correct / total
# print(f'Test Accuracy: {accuracy:.4f}')
