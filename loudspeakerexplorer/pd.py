import pandas as pd


def set_index(df, index):
    df = df.copy()
    df.index = index
    return df


def set_columns(df, columns):
    df = df.copy()
    df.columns = columns
    return df


def remap_columns(df, mapper):
    # Renames columns in `df` according to `columns_mapper`.
    #
    # Columns that don't appear in `columns_mapper` are dropped.
    #
    # Note: contrary to DataFrame.rename(), in the case of MultiIndex columns,
    # `columns_mapper` keys are matched against the full column name (i.e. a
    # tuple), not individual per-level labels.
    return df.loc[:, list(mapper.keys())].pipe(
        lambda df: df.pipe(set_columns, df.columns.map(mapper=mapper)))


def index_as_columns(df):
    # Returns df.index as a DataFrame with only columns and no index.
    return df.index.to_frame().reset_index(drop=True)


def implode(df):
    # Merge identical index entries, resulting in list-valued cells. The
    # opposite of df.explode().
    #
    # For example, given `df`:
    #   C0 C1
    # i 10 11
    # i 20 21
    # j 30 31
    #
    # This will return:
    #   C0       C1
    # i [10, 11] [11, 21]
    # j [30]     [31]
    return (df
            .groupby(level=list(range(0, df.index.nlevels)))
            # Wrap in a tuple to avoid Pandas interpreting the return value
            # as a list of rows.
            .apply(lambda df: df.aggregate(lambda column: (list(column.values),)))
            .applymap(lambda column: column[0]))


def join_index(df, labels):
    # Similar to joining `df` against `labels`, but columns from `labels` are added as index levels to `df`, instead of columns.
    # Particularly useful when touching columns risks wreaking havoc in a multi-level column index.
    # Rows that don't have a corresponding match in `labels` are removed from `df`.
    #
    # For example, given `df`:
    #   C0
    # A
    # i  1
    #    2
    # j  3
    #    4
    # k  5
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
    return df.drop(index=df.index.difference(labels.index)).pipe(
        lambda df: df.pipe(set_index, pd.MultiIndex.from_frame(
            pd.concat([df.index.to_frame(), labels], axis='columns'))))


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
    return df.pipe(set_index, pd.MultiIndex.from_frame(
        index_df.drop(columns=index_common_names))), common_info
