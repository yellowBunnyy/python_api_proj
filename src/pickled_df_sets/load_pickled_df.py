import pandas as pd
import os


input_cov_path = os.path.join(os.getcwd(), "src", "pickled_df_sets", "covid.pickle")
input_influenza_path = os.path.join(os.getcwd(), "src", "pickled_df_sets", "influenza.pickle")


def get_data_from_pickle(input_path):
    return pd.read_pickle(input_path)


if __name__ == '__main__':
    print(pd.read_pickle(input_cov_path))
