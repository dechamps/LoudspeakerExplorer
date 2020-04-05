import pandas as pd


def extract_common_index_levels(df):
    # Removes index levels from `df` that have identical values throughout.
    # Also returns a Series with the index levels that were removed, along with
    # their common value.
    #
    # For example, given:
    #          COL
    #  A  B  C
    # a1  b  c   1
    # a2  b  c   2
    # a2  b  c   3
    #
    # Will return:
    #    COL
    #  A
    # a1   1
    # a2   2
    # a2   3
    #
    # And:
    # B b
    # C c
    index_df = (
        df
        .index
        .to_frame()
        .reset_index(drop=True)
    )
    index_has_distinct_values = index_df.nunique() > 1
    index_common_names = index_has_distinct_values.loc[~index_has_distinct_values].index

    def extract_unique_index_value(index_name):
        (unique_index_value,) = index_df.loc[:, index_name].unique()
        return unique_index_value
    common_info = (
        index_common_names
        .to_series()
        .apply(extract_unique_index_value)
    )
    df = df.copy()
    df.index = pd.MultiIndex.from_frame(
        index_df.drop(columns=index_common_names))
    return df, common_info
