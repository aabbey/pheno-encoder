import src.data.data_extraction as d
from random import sample, randint

data_dir = '../data/raw/sample_disease_phenotypes/'
num_traits_average = 20

if __name__ == "__main__":
    df, dfs = d.load_data(data_dir)


    for d in dfs:
        subset = 3

        all_terms_list = d['HPO_TERM_NAME'].tolist()
        num_traits_to_use = num_traits_average + randint(-10, 10)

        traits_to_use = sample(all_terms_list, num_traits_to_use) if len(
            all_terms_list) > num_traits_to_use else all_terms_list
        print(traits_to_use, "\n\n")
