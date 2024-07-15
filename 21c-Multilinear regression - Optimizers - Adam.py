import torch
import torch.optim as optim

# Define a simple model
model = torch.nn.Linear(10, 1)

# Define the Adam optimizer
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Example training loop
for epoch in range(10):
    optimizer.zero_grad()
    outputs = model(torch.randn(5, 10))
    loss = torch.nn.functional.mse_loss(outputs, torch.randn(5, 1))
    loss.backward()
    optimizer.step()
