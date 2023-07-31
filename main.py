from src.data.data_extraction import load_data
from src.data.data_preprocessing import preprocess_data
from src.model.autoencoder import Autoencoder
import src.model.train as train
import torch
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader, TensorDataset

# Specify the directory where your raw data resides
data_dir = './data/raw/sample_disease_phenotypes/'
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


def plot_encoded_data(model, data, device):
    model.eval() # Switch to evaluation mode

    # Ensure the data is on the correct device
    data = data.to(device)

    # Pass the data through the encoder
    encoded_data = model.encoder(data)

    # Move the data back to the CPU and convert to numpy arrays for plotting
    encoded_data = encoded_data.cpu().detach().numpy()

    # Create the scatter plot
    print(encoded_data[:, 0])
    print(encoded_data[:, 1])
    plt.scatter(encoded_data[:, 0], encoded_data[:, 1])
    plt.show()


if __name__ == "__main__":
    # Load the data
    data_df, df_list = load_data(data_dir)

    print(data_df, df_list)
    train_data = preprocess_data(data_df, df_list)

    n_features = train_data.shape[1]

    print(n_features)
    print(train_data.shape)

    train_data_tensor = torch.tensor(train_data, dtype=torch.float32).to(device)
    print(train_data_tensor)
    print(train_data_tensor.shape)
    train_loader = DataLoader(TensorDataset(train_data_tensor), batch_size=32, shuffle=True, drop_last=True)
    print(next(iter(train_loader)))

    model = Autoencoder(input_dim=n_features)

    train.train(model, train_loader, epochs=10, device=device)

    print("Model trained")

    test_data_tensor = torch.tensor(train_data, dtype=torch.float32).to(device)

    # Plot the first 100 samples of the test data
    plot_encoded_data(model, test_data_tensor[:100], device)


