from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


sample_number = 1
disease_name = "Biotinidase"
sample_pheno_path = 'data/raw/sample_disease_phenotypes/terms_for_Biotinidase Deficiency.csv'
num_traits_to_use = 20


def preprocess_data(df):
    """Preprocess DataFrame, return train and test DataFrames."""

    # Handle missing data if necessary
    # df = df.fillna(value)

    # One-hot encoding if necessary
    # df = pd.get_dummies(df)

    # Scaling if necessary
    # scaler = MinMaxScaler()
    # df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

    # Split data into training and validation sets
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

    return train_df, test_df
