import pandas as pd


def index_as_columns(df):
    # Returns df.index as a DataFrame with only columns and no index.
    return df.index.to_frame().reset_index(drop=True)


def join_index(df, labels):
    # Similar to joining `df` against `labels`, but columns from `labels` are added as index levels to `df`, instead of columns.
    # Particularly useful when touching columns risks wreaking havoc in a multi-level column index.
    #
    # For example, given `df`:
    #   C0
    # A
    # i  1
    #    2
    # j  3
    #    4
    #
    # And `labels`:
    #   C1 C2
    # A
    # i 1i 2i
    # j 1j 2j
    #
    # Then the result will be:
    #         C0
    # A C1 C2
    # i 1i 2i  1
    #          2
    # j 1j 2j  3
    #          4
    return df.align(
        labels.set_index(list(labels.columns.values), append=True),
        axis='index')[0]


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
