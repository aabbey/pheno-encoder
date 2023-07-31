import torch
from torch.utils.data import DataLoader, TensorDataset
from torch import optim, nn

from src.model.autoencoder import Autoencoder


def train(model, train_loader, epochs, device):
    """Train the Autoencoder model."""

    cosine_loss = nn.CosineEmbeddingLoss()

    optimizer = optim.Adam(model.parameters(), lr=0.001)

    model.to(device)

    target = torch.ones(train_loader.batch_size, ).to(device)

    for epoch in range(epochs):
        model.train()
        train_loss = 0

        for data in train_loader:
            data = data[0].to(device)

            optimizer.zero_grad()

            outputs = model(data)

            loss = cosine_loss(outputs, data, target)

            loss.backward()
            optimizer.step()

            train_loss += loss.item()

        train_loss = train_loss / len(train_loader)

        print(f"Epoch {epoch + 1} of {epochs}, Train Loss: {train_loss}")
