import src.data.data_preprocessing as pp
import src.data.data_extraction as d


data_dir = '../data/raw/sample_disease_phenotypes/'
num_traits_average = 20


if __name__ == "__main__":
    df, dfs = d.load_data(data_dir)

    train_data = pp.preprocess_data(df, dfs)


