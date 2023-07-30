from src.data.data_extraction import load_data
from src.data.data_preprocessing import preprocess_data

# Specify the directory where your raw data resides
data_dir = './data/raw/sample_disease_phenotypes/'

if __name__ == "__main__":
    # Load the data
    data = load_data(data_dir)

    print(data)
    # Preprocess the data
    #train_data, test_data = preprocess_data(data)

    # Rest of the pipeline goes here...
