import torch
import torch.optim as optim
import torch.nn as nn
from torchvision import datasets, transforms
from model import get_model

def train():
      device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
      print(f"Training on {device}")

    batch_size = 64
    epochs = 5
    learning_rate = 0.001

    transform = transforms.Compose([
              transforms.ToTensor(),
              transforms.Normalize((0.1307,), (0.3081,))
    ])

    train_loader = torch.utils.data.DataLoader(
              datasets.MNIST('data', train=True, download=True, transform=transform),
              batch_size=batch_size, shuffle=True)

    model = get_model().to(device)
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    criterion = nn.CrossEntropyLoss()

    model.train()
    for epoch in range(epochs):
              for batch_idx, (data, target) in enumerate(train_loader):
                            data, target = data.to(device), target.to(device)
                            optimizer.zero_grad()
                            output = model(data)
                            loss = criterion(output, target)
                            loss.backward()
                            optimizer.step()

                  if batch_idx % 100 == 0:
                                    print(f'Train Epoch: {epoch} [{batch_idx * len(data)}/{len(train_loader.dataset)} ({100. * batch_idx / len(train_loader):.0f}%)]\tLoss: {loss.item():.6f}')

    torch.save(model.state_dict(), "mnist_cnn.pth")
    print("Model saved to mnist_cnn.pth")

if __name__ == "__main__":
      train()
