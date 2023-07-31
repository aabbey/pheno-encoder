from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import torch
import numpy as np
from random import randint, sample


sample_number = 1
n_diseases_to_use = 10
num_traits_average = 20
data_dir = '../../data/raw/sample_disease_phenotypes/'
train_size = 1000


def classes_to_vector(classes, subset):
    classes_dict = {cls: i for i, cls in enumerate(classes)}
    vector = np.zeros(len(classes))
    for cls in subset:
        vector[classes_dict[cls]] = 1
    return vector


def vector_to_classes(classes, vector):
    subset = {cls for i, cls in enumerate(classes) if vector[i] == 1}
    return subset


def make_subset(df):
    all_terms_list = df['HPO_TERM_NAME'].tolist()
    num_traits_to_use = num_traits_average + randint(-10, 10)

    traits_to_use = sample(all_terms_list, num_traits_to_use) if len(
        all_terms_list) > num_traits_to_use else all_terms_list

    return traits_to_use


def preprocess_data(df, dfs):
    """Preprocess DataFrame, return train and test DataFrames."""

    classes = list(set(df['HPO_TERM_NAME'].tolist()))

    train_data = np.zeros((train_size*n_diseases_to_use, len(classes)))
    ix = 0
    for d in dfs[:n_diseases_to_use]:
        ix += 1
        for i in range(train_size):
            n = i*ix
            subset = make_subset(d)

            vector = classes_to_vector(classes, subset)
            train_data[n] = vector

    return train_data
