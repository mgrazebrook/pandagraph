import pytest
import pandas as pd


def ages_df():
    return pd.DataFrame({'name': ['Alice', 'Bill', 'Charlie'], 'age': [27, 42, 39]})


def test_introspection_reads_function_name_params_columns_types():
    """
    pandagraph introspects a function creating a dataframe.

    The GraphQL type is the function name.
    The query parameters are the function parameters.
    The type's attribute are the column names.
    The attribute types map from Pandas types to GraphQL types.
    """
    assert False
