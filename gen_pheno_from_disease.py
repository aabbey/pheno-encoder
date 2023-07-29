import pandas as pd
from random import sample


sample_number = 1
disease_name = "Biotinidase"
sample_pheno_path = 'sample disease phenotypes/terms_for_Biotinidase Deficiency.csv'
num_traits_to_use = 20


if __name__ == '__main__':
    full_example_traits = pd.read_csv(sample_pheno_path)
    all_terms_list = full_example_traits['HPO_TERM_NAME'].tolist()
    traits_to_use = sample(all_terms_list, num_traits_to_use) if len(all_terms_list) > num_traits_to_use else all_terms_list
    print(traits_to_use, "\n\n")